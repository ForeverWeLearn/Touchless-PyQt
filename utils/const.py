from enum import Enum


FG_COLOR = (25, 25, 25)
BG_COLOR = (220, 220, 220)
CONNECTIONS = [
    [4, 3, 2, 1, 0, 5, 9, 13, 17, 0],
    [5, 6, 7, 8],
    [9, 10, 11, 12],
    [13, 14, 15, 16],
    [17, 18, 19, 20],
]


class Mode(Enum):
    NORMAL = "n"
    GESTURE = "g"
    DRAW = "d"


class Action(Enum):
    HOTKEY = "HOTKEY"
    FUNCTION = "FUNCTION"
    COMMAND = "COMMAND"


class Gesture(Enum):
    OPEN = "OPEN"
    GRAB = "GRAB"
    LEFT_ALL = "LEFT_ALL"
    RIGHT_ALL = "RIGHT_ALL"
