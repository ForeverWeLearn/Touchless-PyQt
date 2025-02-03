from PySide6.QtWidgets import (
    QApplication,
    QMainWindow,
    QFrame,
    QLineEdit,
    QComboBox,
    QKeySequenceEdit,
)
from PySide6.QtCore import QStringListModel
from PySide6.QtGui import QPixmap, QKeySequence

from gui.settingpage import Ui_SettingPageFrame
from gui.bindingpage import Ui_BindingPageFrame
from gui.bindingitem import Ui_BindingItemFrame
from gui.actionpage import Ui_ActionPageFrame
from gui.actionitem import Ui_ActionItemFrame
from gui.mainwindow import Ui_MainWindow
from gui.homepage import Ui_HomePageFrame

from utils.reader import ActionReader, BindingReader, read_gestures
from utils.const import Action

import sys


GESTURES = read_gestures()
FUNCTIONS = ["pause_ai_engine", "stop_ai_engine"]


def pause_ai_engine():
    print("This function isn't avaiable right now! (Cos I am lazy :>)")
    pass


def stop_ai_engine():
    print("This function isn't avaiable right now, too! (Cos I am lazy :>)")
    pass


class BindingItem(QFrame, Ui_BindingItemFrame):
    def __init__(self, parent):
        super().__init__(parent)
        self.setupUi(self)

        self.Gesture1.addItems(GESTURES)
        self.Gesture2.addItems(GESTURES)

        self.DeleteBtn.clicked.connect(self.deleteLater)

    def load_data(self, name: str, data: dict, action_names: list, actions: dict):
        self.Name.setText(name)
        self.Gesture1.setCurrentIndex(GESTURES.index(data["gesture1"]))
        self.Gesture2.setCurrentIndex(GESTURES.index(data["gesture2"]))
        self.Action.addItems(action_names)
        action_name = actions[data["action"]]["name"]
        self.Action.setCurrentIndex(action_names.index(action_name))


class ActionItem(QFrame, Ui_ActionItemFrame):
    def __init__(self, parent, id: str):
        super().__init__(parent)
        self.setupUi(self)

        self.id = id

        self.Hotkey = QKeySequenceEdit()
        self.Function = QComboBox()
        self.Function.addItems(FUNCTIONS)
        self.Command = QLineEdit()
        self.ValueList = [self.Hotkey, self.Function, self.Command]

        self.Type.currentIndexChanged.connect(self.set_type)
        self.DeleteBtn.clicked.connect(self.deleteLater)

        self.set_type(0)

    def load_data(self, data: dict):
        self.Name.setText(data["name"])
        if data["type"] == Action.HOTKEY.name:
            self.set_type(0)
            keys: list = data["value"]
            self.Hotkey.setKeySequence(QKeySequence("+".join(keys)))
        elif data["type"] == Action.FUNCTION.name:
            self.set_type(1)
            self.Function.setCurrentIndex(FUNCTIONS.index(data["value"]))
        elif data["type"] == Action.COMMAND.name:
            self.set_type(2)
            self.Command.setText(data["value"])

    def set_type(self, index=-1):
        if index == -1:
            index = self.Type.currentIndex()

        self.Type.setCurrentIndex(index)

        for item in self.ValueList:
            if item is self.ValueList[index]:
                item.setParent(self.ValueFrame)
                self.ValueLayout.addWidget(item)
            else:
                item.setParent(None)


class HomePage(QFrame, Ui_HomePageFrame):
    def __init__(self, parent):
        super().__init__(parent)
        self.setupUi(self)


class BindingPage(QFrame, Ui_BindingPageFrame):
    def __init__(self, parent):
        super().__init__(parent)
        self.setupUi(self)

        self.binding_reader = BindingReader()
        self.action_reader = ActionReader()
        self.action_names = self.action_reader.get_names()

        self.NewBtn.clicked.connect(self.add_binding)
        self.SaveBtn.clicked.connect(self.save_bindings)

        self.load_bindings()

    def load_bindings(self):
        bindings = self.binding_reader.read()
        for name, data in bindings.items():
            item = BindingItem(self.BindingListFrame)
            item.load_data(name, data, self.action_names, self.action_reader.actions)
            self.add_binding(item)
        pass

    def add_binding(self, item=0):
        if item == 0:
            item = BindingItem(self.BindingListFrame)
        self.BindingListLayout.addWidget(item)

    def save_bindings(self):
        print("Saved!")
        pass

class ActionPage(QFrame, Ui_ActionPageFrame):
    def __init__(self, parent):
        super().__init__(parent)
        self.setupUi(self)

        self.action_reader = ActionReader()

        self.NewBtn.clicked.connect(self.add_action)
        self.SaveBtn.clicked.connect(self.save_actions)

        self.load_actions()

    def load_actions(self):
        actions = self.action_reader.read()
        for id, data in actions.items():
            item = ActionItem(self.ActionListFrame, id)
            item.load_data(data)
            self.add_action(item)

    def add_action(self, item=0):
        if item == 0:
            item = ActionItem(
                self.ActionListFrame, self.action_reader.get_avaiable_id()
            )
        self.ActionListLayout.addWidget(item)

    def save_actions(self):
        print("Save")
        pass

class SettingPage(QFrame, Ui_SettingPageFrame):
    def __init__(self, parent):
        super().__init__(parent)
        self.setupUi(self)


class MainWindow(QMainWindow, Ui_MainWindow):
    def __init__(self):
        super().__init__()
        self.setupUi(self)
        self.setWindowTitle("Application")
        self.setWindowIcon(QPixmap("./imgs/icon.ico"))

        self.HomePageFrame = HomePage(self.PageContentFrame)
        self.BindingPageFrame = BindingPage(self.PageContentFrame)
        self.ActionPageFrame = ActionPage(self.PageContentFrame)
        self.SettingPageFrame = SettingPage(self.PageContentFrame)

        self.HomeBtn.clicked.connect(lambda: self.load_page(self.HomePageFrame))
        self.BindingBtn.clicked.connect(lambda: self.load_page(self.BindingPageFrame))
        self.ActionBtn.clicked.connect(lambda: self.load_page(self.ActionPageFrame))
        self.SettingBtn.clicked.connect(lambda: self.load_page(self.SettingPageFrame))

        self.load_page(self.HomePageFrame)

    def load_page(self, page):
        if self.HomePageFrame is not page:
            self.HomePageFrame.setParent(None)

        if self.BindingPageFrame is not page:
            self.BindingPageFrame.setParent(None)

        if self.ActionPageFrame is not page:
            self.ActionPageFrame.setParent(None)

        if self.SettingPageFrame is not page:
            self.SettingPageFrame.setParent(None)

        self.PageContentLayout.addWidget(page)


if __name__ == "__main__":
    app = QApplication(sys.argv)

    window = MainWindow()
    window.show()

    sys.exit(app.exec())
