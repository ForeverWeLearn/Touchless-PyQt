# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'actionitem.ui'
##
## Created by: Qt User Interface Compiler version 6.8.2
##
## WARNING! All changes made in this file will be lost when recompiling UI file!
################################################################################

from PySide6.QtCore import (QCoreApplication, QDate, QDateTime, QLocale,
    QMetaObject, QObject, QPoint, QRect,
    QSize, QTime, QUrl, Qt)
from PySide6.QtGui import (QBrush, QColor, QConicalGradient, QCursor,
    QFont, QFontDatabase, QGradient, QIcon,
    QImage, QKeySequence, QLinearGradient, QPainter,
    QPalette, QPixmap, QRadialGradient, QTransform)
from PySide6.QtWidgets import (QApplication, QComboBox, QFrame, QHBoxLayout,
    QLineEdit, QPushButton, QSizePolicy, QVBoxLayout,
    QWidget)

class Ui_ActionItemFrame(object):
    def setupUi(self, ActionItemFrame):
        if not ActionItemFrame.objectName():
            ActionItemFrame.setObjectName(u"ActionItemFrame")
        ActionItemFrame.resize(554, 109)
        ActionItemFrame.setStyleSheet(u"background-color: rgb(30, 30, 30);")
        self.ActionItemLayout = QHBoxLayout(ActionItemFrame)
        self.ActionItemLayout.setObjectName(u"ActionItemLayout")
        self.ActionItemLayout.setContentsMargins(0, 0, 0, 0)
        self.Name = QLineEdit(ActionItemFrame)
        self.Name.setObjectName(u"Name")
        sizePolicy = QSizePolicy(QSizePolicy.Policy.Minimum, QSizePolicy.Policy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.Name.sizePolicy().hasHeightForWidth())
        self.Name.setSizePolicy(sizePolicy)
        self.Name.setMinimumSize(QSize(140, 24))
        self.Name.setStyleSheet(u"color: rgb(231, 231, 231);\n"
"border-color: rgb(206, 28, 255);")
        self.Name.setMaxLength(32)

        self.ActionItemLayout.addWidget(self.Name)

        self.Type = QComboBox(ActionItemFrame)
        icon = QIcon()
        icon.addFile(u"imgs/keyboard.png", QSize(), QIcon.Mode.Normal, QIcon.State.Off)
        self.Type.addItem(icon, "")
        icon1 = QIcon()
        icon1.addFile(u"imgs/function.png", QSize(), QIcon.Mode.Normal, QIcon.State.Off)
        self.Type.addItem(icon1, "")
        icon2 = QIcon()
        icon2.addFile(u"imgs/terminal.png", QSize(), QIcon.Mode.Normal, QIcon.State.Off)
        self.Type.addItem(icon2, "")
        self.Type.setObjectName(u"Type")
        sizePolicy1 = QSizePolicy(QSizePolicy.Policy.Preferred, QSizePolicy.Policy.Expanding)
        sizePolicy1.setHorizontalStretch(0)
        sizePolicy1.setVerticalStretch(0)
        sizePolicy1.setHeightForWidth(self.Type.sizePolicy().hasHeightForWidth())
        self.Type.setSizePolicy(sizePolicy1)
        self.Type.setMinimumSize(QSize(100, 0))
        self.Type.setCursor(QCursor(Qt.CursorShape.PointingHandCursor))
        self.Type.setStyleSheet(u"color: rgb(231, 231, 231);")

        self.ActionItemLayout.addWidget(self.Type)

        self.ValueFrame = QFrame(ActionItemFrame)
        self.ValueFrame.setObjectName(u"ValueFrame")
        sizePolicy2 = QSizePolicy(QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Preferred)
        sizePolicy2.setHorizontalStretch(0)
        sizePolicy2.setVerticalStretch(0)
        sizePolicy2.setHeightForWidth(self.ValueFrame.sizePolicy().hasHeightForWidth())
        self.ValueFrame.setSizePolicy(sizePolicy2)
        self.ValueLayout = QVBoxLayout(self.ValueFrame)
        self.ValueLayout.setSpacing(0)
        self.ValueLayout.setObjectName(u"ValueLayout")
        self.ValueLayout.setContentsMargins(0, 0, 0, 0)

        self.ActionItemLayout.addWidget(self.ValueFrame)

        self.DeleteBtn = QPushButton(ActionItemFrame)
        self.DeleteBtn.setObjectName(u"DeleteBtn")
        self.DeleteBtn.setMaximumSize(QSize(20, 20))
        self.DeleteBtn.setCursor(QCursor(Qt.CursorShape.PointingHandCursor))
        self.DeleteBtn.setStyleSheet(u"color: rgb(122, 122, 122);")
        self.DeleteBtn.setFlat(True)

        self.ActionItemLayout.addWidget(self.DeleteBtn)


        self.retranslateUi(ActionItemFrame)

        self.Type.setCurrentIndex(-1)


        QMetaObject.connectSlotsByName(ActionItemFrame)
    # setupUi

    def retranslateUi(self, ActionItemFrame):
        ActionItemFrame.setWindowTitle(QCoreApplication.translate("ActionItemFrame", u"Frame", None))
        self.Name.setText("")
        self.Name.setPlaceholderText(QCoreApplication.translate("ActionItemFrame", u"Name", None))
        self.Type.setItemText(0, QCoreApplication.translate("ActionItemFrame", u"HOTKEY", None))
        self.Type.setItemText(1, QCoreApplication.translate("ActionItemFrame", u"FUNCTION", None))
        self.Type.setItemText(2, QCoreApplication.translate("ActionItemFrame", u"COMMAND", None))

        self.DeleteBtn.setText(QCoreApplication.translate("ActionItemFrame", u"\u2715", None))
    # retranslateUi

