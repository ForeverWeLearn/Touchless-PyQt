from utils.analyzer import GestureAnalyzer
from utils.const import Mode
from utils import algo, dev, draw, reader
from model import GestureClassifier

import mediapipe as mp
import cv2


class Engine:
    def __init__(
        self,
        gestures: list,
        actions: dict,
        bindings: dict,
        cap_device=0,
        cap_width=960,
        cap_height=540,
        mode=Mode.NORMAL,
        debug_window=False,
        min_detection_confidence=0.8,
        min_tracking_confidence=0.5,
    ):
        self.gestures = gestures
        self.actions = actions
        self.bindings = bindings
        self.cap_device = cap_device
        self.cap_width = cap_width
        self.cap_height = cap_height
        self.mode = mode
        self.debug_window = debug_window
        self.min_detection_confidence = min_detection_confidence
        self.min_tracking_confidence = min_tracking_confidence

        self.ready = False

    def prepare(self):
        # Camera preparation ##################################################
        print("Prepering camera...")
        self._cap = cv2.VideoCapture(self.cap_device)
        self._cap.set(cv2.CAP_PROP_FRAME_WIDTH, self.cap_width)
        self._cap.set(cv2.CAP_PROP_FRAME_HEIGHT, self.cap_height)
        print("Done!")

        # Model load ##########################################################
        print("Loading hand landmark model...")
        mp_hands = mp.solutions.hands
        self._hands = mp_hands.Hands(
            static_image_mode=False,
            max_num_hands=2,
            min_detection_confidence=self.min_detection_confidence,
            min_tracking_confidence=self.min_tracking_confidence,
        )
        print("Done!")

        print("Loading gesture classifier model...")
        self._gesture_classifier = GestureClassifier()
        print("Done!")

        print("Loading analyzers...")
        self._left_analyzer = GestureAnalyzer(
            self.gestures, self.actions, self.bindings
        )
        self._right_analyzer = GestureAnalyzer(
            self.gestures, self.actions, self.bindings
        )
        print("Done!")

        self.ready = True

    def estimate_hand_landmarks(self, image):
        image = cv2.cvtColor(image, cv2.COLOR_BGR2RGB)
        image.flags.writeable = False
        results = self._hands.process(image)
        image.flags.writeable = True
        return results

    def process_hand_landmarks(self, image, multi_hand_landmarks, multi_handedness):
        for hand_landmarks, handedness in zip(multi_hand_landmarks, multi_handedness):
            handedness = handedness.classification[0].label[0:]

            keypoints = algo.calc_keypoints(image, hand_landmarks)
            bbox = algo.calc_bounding_box(keypoints)

            # Conversion to relative coordinates - normalized coordinates
            normalized_keypoints = algo.normalize_keypoints(keypoints)

            # Gesture classification
            gesture_id = self._gesture_classifier(normalized_keypoints)

            # Gesture analyze
            if handedness == "Left":
                self._left_analyzer(gesture_id)
            else:
                self._right_analyzer(gesture_id)

            # Draw
            if self.debug_window:
                draw.draw_hand(image, bbox, keypoints)
                draw.draw_info(image, bbox, handedness, self.gestures[gesture_id])

    def __call__(self):
        if not self.ready:
            self.prepare()

        # Parse mode (ESC to exit) ########################################
        key = cv2.waitKey(20)
        if key == 27:
            return None
        self.mode, number = dev.parse_mode(self.mode, key)

        # Camera capture ##################################################
        ret, image = self._cap.read()
        if not ret:
            return None
        image = cv2.flip(image, 1)

        # Process hands ###################################################
        results = self.estimate_hand_landmarks(image)
        if results.multi_hand_landmarks is not None:
            self.process_hand_landmarks(
                image, results.multi_hand_landmarks, results.multi_handedness
            )

        # Debug window ####################################################
        if self.debug_window:
            cv2.imshow("Debug", image)

        return image


def main():
    engine = Engine(
        gestures=reader.read_gestures(),
        actions=reader.ActionReader().read(),
        bindings=reader.BindingReader().read(),
        cap_device=0,
        cap_width=960,
        cap_height=540,
        mode=Mode.NORMAL,
        debug_window=True,
        min_detection_confidence=0.8,
        min_tracking_confidence=0.5,
    )

    while True:
        result = engine()
        if result is None:
            break


if __name__ == "__main__":
    main()
