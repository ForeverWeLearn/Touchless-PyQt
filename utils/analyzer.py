from utils.executor import ActionExecutor
from collections import Counter, deque
from time import time


class GestureAnalyzer:
    def __init__(
        self,
        gestures: list,
        actions: dict,
        bindings: dict,
        gesture1_thres=0.5,
        gesture2_thres=0.3,
    ):
        self.gestures = gestures
        self.bindings = bindings
        self.executor = ActionExecutor(actions)

        self.gesture1_thres = gesture1_thres
        self.gesture2_thres = gesture2_thres
        self.thres = gesture1_thres + gesture2_thres

        self.history_full = False
        self.time_history = deque(maxlen=48)
        self.gesture_id_history = deque(maxlen=48)

    def gesture_trend(self) -> tuple:
        if (
            not self.history_full
            and self.time_history[-1] - self.time_history[0] > self.thres
        ):
            self.history_full = True

        if not self.history_full:
            return None, None

        while self.time_history[-1] - self.time_history[0] > self.thres:
            self.time_history.popleft()
            self.gesture_id_history.popleft()

        if len(self.gesture_id_history) < 2:
            return None, None

        lst = list(self.gesture_id_history)
        split = round(self.gesture1_thres / self.thres * len(lst))

        res1 = Counter(lst[:split]).most_common(1)[0]
        trend1 = self.gestures[res1[0]] if res1[1] >= 0.75 * split else None

        res2 = Counter(lst[split:]).most_common(1)[0]
        trend2 = (
            self.gestures[res2[0]] if res2[1] >= 0.75 * (len(lst) - split) else None
        )

        return trend1, trend2

    def __call__(self, gesture_id: int):
        t = time()

        if len(self.time_history) > 0 and t - self.time_history[-1] > 0.2:
            self.time_history.clear()
            self.gesture_id_history.clear()

        self.time_history.append(t)
        self.gesture_id_history.append(gesture_id)

        gesture1, gesture2 = self.gesture_trend()
        if not gesture1 or not gesture2:
            return

        for _, binding_data in self.bindings.items():
            if gesture1 == binding_data["gesture1"] and gesture2 == binding_data["gesture2"]:
                success = self.executor(binding_data["action_id"])
                if success:
                    self.history_full = False
                    self.time_history.clear()
