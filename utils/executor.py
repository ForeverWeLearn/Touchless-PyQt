from utils.const import Action
from pyautogui import hotkey
from time import time
from os import system


class ActionExecutor:
    def __init__(self, actions: dict):
        self.actions: dict = actions

        self.last_execute_time: float = 0

    def __call__(self, action_list) -> bool:
        executed = False
        for action_id, action_data in self.actions.items():
            if action_id in action_list:
                if self.should_execute(action_id):
                    executed = True
                    self.last_execute_time = time()
                    print(f"Execute: {action_data}")
                    self.execute(action_data)
                else:
                    print(f"Denied: {action_id}")
        return executed

    # Not yet completed
    def should_execute(self, action_name: str) -> bool:
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
        action_type = action_data["type"]
        action_value = action_data["value"]

        match action_type:
            case Action.HOTKEY.name:
                self.execute_hotkey(action_value)

            case Action.FUNCTION.name:
                self.execute_built_in(action_value)

            case Action.COMMAND.name:
                self.execute_command(action_value)

            case _:
                print("Invalid action type!")
