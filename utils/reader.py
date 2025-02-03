from utils.const import Action
from json import load


def read_json(file_path: str) -> dict:
    with open(file_path, "r") as file:
        return load(file)


def read_gestures() -> list:
    return read_json("./model/gesture_classifier/gesture_classifier_labels.json")


class ActionReader:
    def __init__(self, file_path="./configs/actions.json"):
        self.file_path = file_path
        self.read()

    def read(self) -> dict:
        self.actions = read_json(self.file_path)
        return self.actions

    def get_actions_by_type(self, action: Action) -> dict:
        d: dict = {}
        for key, val in self.actions.items():
            if val["type"] == action.name:
                d[key] = val
        return d

    def get_names(self) -> list:
        return list(self.actions.keys())


class BindingReader:
    def __init__(self, file_path="./configs/bindings.json"):
        self.file_path = file_path
        self.read()

    def read(self) -> dict:
        self.bindings = read_json(self.file_path)
        return self.bindings


class SettingReader:
    def __init__(self, file_path="./configs/settings.json"):
        self.file_path = file_path
        self.read()

    def read(self) -> dict:
        self.settings = read_json(self.file_path)
        return self.settings
