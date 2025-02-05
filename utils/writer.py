import json


def write_json(data: dict, path: str):
    with open(path, "w") as json_file:
        json.dump(data, json_file, indent=2)


def write_actions(data: dict):
    write_json(data, "./configs/actions.json")


def write_bindings(data: dict):
    write_json(data, "./configs/bindings.json")


def write_settings(data: dict):
    write_json(data, "./configs/settings.json")
