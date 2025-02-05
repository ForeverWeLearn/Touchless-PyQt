from PySide6.QtWidgets import (
    QApplication,
    QMainWindow,
    QFrame,
    QLineEdit,
    QComboBox,
    QKeySequenceEdit,
)
from PySide6.QtCore import Qt, Signal, Slot, QThread
from PySide6.QtGui import QPixmap, QKeySequence, QImage

from gui.v1.settingpage import Ui_SettingPageFrame
from gui.v1.bindingpage import Ui_BindingPageFrame
from gui.v1.bindingitem import Ui_BindingItemFrame
from gui.v1.actionpage import Ui_ActionPageFrame
from gui.v1.actionitem import Ui_ActionItemFrame
from gui.v1.mainwindow import Ui_MainWindow
from gui.v1.homepage import Ui_HomePageFrame

from utils.reader import ActionReader, BindingReader, read_gestures
from utils.writer import write_actions, write_bindings
from utils.const import Action
from utils.algo import generate_random_string

import sys


ID_LENGTH = 12
ACTION_READER = ActionReader()
BINDING_READER = BindingReader()
GESTURES = read_gestures()
FUNCTIONS = ["pause_ai_engine", "stop_ai_engine"]

actions = ACTION_READER.read()
bindings = BINDING_READER.read()
action_names = ACTION_READER.get_names()


def read_configs():
    global actions
    global bindings
    global action_names
    actions = ACTION_READER.read()
    bindings = BINDING_READER.read()
    action_names = ACTION_READER.get_names()


def is_valid_id(id: str):
    return len(id) == ID_LENGTH


def pause_ai_engine():
    print("This function isn't avaiable right now! (Cos I am lazy :>)")
    pass


def stop_ai_engine():
    print("This function isn't avaiable right now, too! (Cos I am lazy :>)")
    pass


class EngineThread(QThread):
    updateFrame = Signal(QImage)

    def __init__(self, parent=None):
        QThread.__init__(self, parent)

        from engine import Engine

        self.engine = Engine()

        self.status = True

    def prepare(self):
        self.engine.prepare()

    def run(self):
        while self.status:
            image = self.engine()
            if image is None:
                sys.exit(-1)

            h, w, ch = image.shape
            qimage = QImage(image.data, w, h, ch * w, QImage.Format.Format_RGB888)
            scaled_img = qimage.scaled(640, 480, Qt.KeepAspectRatio)

            self.updateFrame.emit(scaled_img)

        sys.exit(-1)


class BindingItem(QFrame, Ui_BindingItemFrame):
    def __init__(self, parent, id=""):
        super().__init__(parent)
        self.setupUi(self)

        if not is_valid_id(id):
            self.id = generate_random_string(ID_LENGTH)
        else:
            self.id = id

        self.Gesture1.addItems(GESTURES)
        self.Gesture2.addItems(GESTURES)
        self.Action.addItems(action_names)

        self.DeleteBtn.clicked.connect(self.deleteLater)

    def reload(self):
        self.Action.clear()
        self.Action.addItems(action_names)

    def load_data(self, data: dict):
        self.Name.setText(data["name"])
        self.Gesture1.setCurrentIndex(GESTURES.index(data["gesture1"]))
        self.Gesture2.setCurrentIndex(GESTURES.index(data["gesture2"]))
        action = actions.get(data["action_id"])
        if action:
            self.Action.setCurrentIndex(action_names.index(action["name"]))

    def get_data(self):
        data = {
            "name": self.Name.text(),
            "gesture1": self.Gesture1.currentText(),
            "gesture2": self.Gesture2.currentText(),
            "action_id": ACTION_READER.get_id_by_name(self.Action.currentText()),
        }
        return data


class ActionItem(QFrame, Ui_ActionItemFrame):
    def __init__(self, parent, id=""):
        super().__init__(parent)
        self.setupUi(self)

        if not is_valid_id(id):
            self.id = generate_random_string(ID_LENGTH)
        else:
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
            self.Hotkey.setKeySequence(QKeySequence(keys))
        elif data["type"] == Action.FUNCTION.name:
            self.set_type(1)
            self.Function.setCurrentIndex(FUNCTIONS.index(data["value"]))
        elif data["type"] == Action.COMMAND.name:
            self.set_type(2)
            self.Command.setText(data["value"])

    def get_data(self):
        data = {
            "name": self.Name.text(),
            "type": self.Type.currentText(),
            "value": self.get_value(),
        }
        return data

    def get_value(self):
        if self.Type.currentIndex() == 0:
            return self.Hotkey.keySequence().toString()
        elif self.Type.currentIndex() == 1:
            return self.Function.currentText()
        elif self.Type.currentIndex() == 2:
            return self.Command.text()

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

        self.NewBtn.clicked.connect(self.add_binding)
        self.SaveBtn.clicked.connect(self.save_bindings)

        self.load_bindings()

    def reload(self):
        item: BindingItem
        for item in self.findChildren(BindingItem):
            item.reload()

    def load_bindings(self):
        for id, data in bindings.items():
            item = BindingItem(self.BindingListFrame, id)
            item.load_data(data)
            self.add_binding(item)
        pass

    def add_binding(self, item=0):
        if item == 0:
            item = BindingItem(self.BindingListFrame)
        self.BindingListLayout.addWidget(item)

    def get_bindings(self):
        data = {}
        item: BindingItem
        for item in self.findChildren(BindingItem):
            item_data = item.get_data()
            data[item.id] = item_data
        return data

    def save_bindings(self):
        saved_bindings = self.get_bindings()
        write_bindings(saved_bindings)
        print(saved_bindings)
        print("Saved!")


class ActionPage(QFrame, Ui_ActionPageFrame):
    def __init__(self, parent):
        super().__init__(parent)
        self.setupUi(self)

        self.NewBtn.clicked.connect(self.add_action)
        self.SaveBtn.clicked.connect(self.save_actions)

        self.load_actions()

    def load_actions(self):
        for id, data in actions.items():
            item = ActionItem(self.ActionListFrame, id)
            item.load_data(data)
            self.add_action(item)

    def add_action(self, item=0):
        if item == 0:
            item = ActionItem(self.ActionListFrame)
        self.ActionListLayout.addWidget(item)

    def get_actions(self):
        data = {}
        item: ActionItem
        for item in self.findChildren(ActionItem):
            item_data = item.get_data()
            data[item.id] = item_data
        return data

    def save_actions(self):
        saved_actions = self.get_actions()
        write_actions(saved_actions)
        print(saved_actions)
        print("Saved!")
        read_configs()


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

        self.engineThread = EngineThread(self)
        self.engineThread.finished.connect(self.close)
        self.engineThread.updateFrame.connect(self.setImage)

        self.HomePageFrame = HomePage(self.PageContentFrame)
        self.BindingPageFrame = BindingPage(self.PageContentFrame)
        self.ActionPageFrame = ActionPage(self.PageContentFrame)
        self.SettingPageFrame = SettingPage(self.PageContentFrame)

        self.HomeBtn.clicked.connect(lambda: self.load_page(self.HomePageFrame))
        self.BindingBtn.clicked.connect(lambda: self.load_page(self.BindingPageFrame))
        self.ActionBtn.clicked.connect(lambda: self.load_page(self.ActionPageFrame))
        self.SettingBtn.clicked.connect(lambda: self.load_page(self.SettingPageFrame))

        self.HomePageFrame.StartBtn.clicked.connect(self.engineThread.run)
        self.HomePageFrame.StopBtn.clicked.connect(self.engineThread.terminate)
        self.ActionPageFrame.SaveBtn.clicked.connect(self.BindingPageFrame.reload)

        self.load_page(self.HomePageFrame)

        self.engineThread.prepare()

    @Slot(QImage)
    def setImage(self, image):
        self.HomePageFrame.VideoLabel.setPixmap(QPixmap.fromImage(image))

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
