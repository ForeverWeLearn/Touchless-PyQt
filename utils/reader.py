from utils.const import Action
from json import load


def read_json(file_path: str) -> dict:
    with open(file_path, "r") as file:
        return load(file)


class ActionReader:
    def __init__(self, file_path: str):
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


class BindingReader:
    def __init__(self, file_path: str):
        self.file_path = file_path
        self.read()

    def read(self) -> dict:
        self.bindings = read_json(self.file_path)
        return self.bindings


class SettingReader:
    def __init__(self, file_path: str):
        self.file_path = file_path
        self.read()

    def read(self) -> dict:
        self.settings = read_json(self.file_path)
        return self.settings
