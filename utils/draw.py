from utils.const import FG_COLOR, BG_COLOR, CONNECTIONS
import cv2


def draw_hand(image, bbox, keypoints):
    # Keypoints
    for i, point in enumerate(keypoints):
        cv2.circle(image, tuple(point), 3, BG_COLOR, 2)

    # Connections
    for path in CONNECTIONS:
        for i in range(len(path) - 1):
            cv2.line(
                image,
                tuple(keypoints[path[i]]),
                tuple(keypoints[path[i + 1]]),
                BG_COLOR,
                2,
            )

    # Bounding box
    cv2.rectangle(image, (bbox[0], bbox[1]), (bbox[2], bbox[3]), BG_COLOR, 1)

    return image


def draw_info(image, bbox, handedness, gesture):
    cv2.rectangle(image, (bbox[0], bbox[1]), (bbox[2], bbox[1] - 22), BG_COLOR, -1)

    hand_text = handedness
    if gesture != "":
        hand_text += ": " + gesture
    cv2.putText(
        image,
        hand_text,
        (bbox[0] + 5, bbox[1] - 4),
        cv2.FONT_HERSHEY_SIMPLEX,
        0.6,
        FG_COLOR,
        2,
    )

    return image
