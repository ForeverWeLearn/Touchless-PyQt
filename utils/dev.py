from utils.const import Mode
import csv


def parse_mode(mode: Mode, key: int):
    if ord("0") <= key <= ord("9"):
        key -= ord("0")

    if key == ord(Mode.NORMAL.value):
        mode = Mode.NORMAL
    if key == ord(Mode.GESTURE.value):
        mode = Mode.GESTURE
    if key == ord(Mode.DRAW.value):
        mode = Mode.DRAW

    return key, mode


def logging_csv(mode: Mode, number: int, lst: list):
    if mode == Mode.NORMAL:
        pass
    if mode == Mode.GESTURE and (0 <= number <= 9):
        csv_path = "./model/gesture_classifier/gesture_classifier_data.csv"
        with open(csv_path, "a", newline="") as file:
            fwriter = csv.writer(file)
            fwriter.writerow([number, *lst])
