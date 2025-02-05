from utils.const import Action
from pyautogui import hotkey
from time import time
from os import system


class ActionExecutor:
    def __init__(self, actions: dict):
        self.actions: dict = actions

        self.last_execute_time: float = 0

    def __call__(self, action_id) -> bool:
        executed = False
        action_name = self.actions[action_id]["name"]

        if self.should_execute(action_id):
            self.last_execute_time = time()
            print(f"Execute: {action_name}")
            self.execute(self.actions[action_id])
            executed = True
        else:
            print(f"Denied: {action_name}")
        
        return executed

    # Not yet completed
    def should_execute(self, action_id: str) -> bool:
        t = time()
        if t - self.last_execute_time < 2:
            return False
        return True

    def execute_hotkey(self, keys: list):
        hotkey(keys)

    def execute_built_in(self, function_name):
        try:
            eval(function_name)
        except Exception as e:
            print(e)

    def execute_command(self, command):
        try:
            system(command)
        except Exception as e:
            print(e)

    def execute(self, action_data: dict):
        match action_data["type"]:
            case Action.HOTKEY.name:
                self.execute_hotkey(action_data["value"])

            case Action.FUNCTION.name:
                self.execute_built_in(action_data["value"])

            case Action.COMMAND.name:
                self.execute_command(action_data["value"])

            case _:
                print("Invalid action type!")
