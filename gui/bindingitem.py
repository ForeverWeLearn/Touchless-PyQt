# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'bindingitem.ui'
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
    QLabel, QLineEdit, QPushButton, QSizePolicy,
    QWidget)

class Ui_BindingItemFrame(object):
    def setupUi(self, BindingItemFrame):
        if not BindingItemFrame.objectName():
            BindingItemFrame.setObjectName(u"BindingItemFrame")
        BindingItemFrame.resize(408, 106)
        BindingItemFrame.setStyleSheet(u"background-color: rgb(30, 30, 30);")
        self.BindingItemLayout = QHBoxLayout(BindingItemFrame)
        self.BindingItemLayout.setObjectName(u"BindingItemLayout")
        self.BindingItemLayout.setContentsMargins(0, 0, 0, 0)
        self.Name = QLineEdit(BindingItemFrame)
        self.Name.setObjectName(u"Name")
        sizePolicy = QSizePolicy(QSizePolicy.Policy.Minimum, QSizePolicy.Policy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.Name.sizePolicy().hasHeightForWidth())
        self.Name.setSizePolicy(sizePolicy)
        self.Name.setMinimumSize(QSize(0, 24))
        self.Name.setStyleSheet(u"color: rgb(231, 231, 231);\n"
"border-color: rgb(206, 28, 255);")
        self.Name.setMaxLength(32)

        self.BindingItemLayout.addWidget(self.Name)

        self.Gesture1 = QComboBox(BindingItemFrame)
        self.Gesture1.setObjectName(u"Gesture1")
        sizePolicy1 = QSizePolicy(QSizePolicy.Policy.Preferred, QSizePolicy.Policy.Expanding)
        sizePolicy1.setHorizontalStretch(0)
        sizePolicy1.setVerticalStretch(0)
        sizePolicy1.setHeightForWidth(self.Gesture1.sizePolicy().hasHeightForWidth())
        self.Gesture1.setSizePolicy(sizePolicy1)
        self.Gesture1.setCursor(QCursor(Qt.CursorShape.PointingHandCursor))
        self.Gesture1.setStyleSheet(u"color: rgb(231, 231, 231);")

        self.BindingItemLayout.addWidget(self.Gesture1)

        self.RIghtLabel1 = QLabel(BindingItemFrame)
        self.RIghtLabel1.setObjectName(u"RIghtLabel1")
        self.RIghtLabel1.setMaximumSize(QSize(20, 20))
        self.RIghtLabel1.setPixmap(QPixmap(u"imgs/keyboard_double_arrow_right.png"))
        self.RIghtLabel1.setScaledContents(True)

        self.BindingItemLayout.addWidget(self.RIghtLabel1)

        self.Gesture2 = QComboBox(BindingItemFrame)
        self.Gesture2.setObjectName(u"Gesture2")
        sizePolicy1.setHeightForWidth(self.Gesture2.sizePolicy().hasHeightForWidth())
        self.Gesture2.setSizePolicy(sizePolicy1)
        self.Gesture2.setCursor(QCursor(Qt.CursorShape.PointingHandCursor))
        self.Gesture2.setStyleSheet(u"color: rgb(231, 231, 231);")

        self.BindingItemLayout.addWidget(self.Gesture2)

        self.RightLabel2 = QLabel(BindingItemFrame)
        self.RightLabel2.setObjectName(u"RightLabel2")
        self.RightLabel2.setMaximumSize(QSize(20, 20))
        self.RightLabel2.setPixmap(QPixmap(u"imgs/link.png"))
        self.RightLabel2.setScaledContents(True)

        self.BindingItemLayout.addWidget(self.RightLabel2)

        self.Action = QComboBox(BindingItemFrame)
        self.Action.setObjectName(u"Action")
        sizePolicy1.setHeightForWidth(self.Action.sizePolicy().hasHeightForWidth())
        self.Action.setSizePolicy(sizePolicy1)
        self.Action.setCursor(QCursor(Qt.CursorShape.PointingHandCursor))
        self.Action.setStyleSheet(u"color: rgb(231, 231, 231);")

        self.BindingItemLayout.addWidget(self.Action)

        self.DeleteBtn = QPushButton(BindingItemFrame)
        self.DeleteBtn.setObjectName(u"DeleteBtn")
        self.DeleteBtn.setMaximumSize(QSize(20, 20))
        self.DeleteBtn.setCursor(QCursor(Qt.CursorShape.PointingHandCursor))
        self.DeleteBtn.setStyleSheet(u"color: rgb(122, 122, 122);")
        self.DeleteBtn.setFlat(True)

        self.BindingItemLayout.addWidget(self.DeleteBtn)


        self.retranslateUi(BindingItemFrame)

        QMetaObject.connectSlotsByName(BindingItemFrame)
    # setupUi

    def retranslateUi(self, BindingItemFrame):
        BindingItemFrame.setWindowTitle(QCoreApplication.translate("BindingItemFrame", u"Frame", None))
        self.Name.setText("")
        self.Name.setPlaceholderText(QCoreApplication.translate("BindingItemFrame", u"Name", None))
        self.RIghtLabel1.setText("")
        self.RightLabel2.setText("")
        self.DeleteBtn.setText(QCoreApplication.translate("BindingItemFrame", u"\u2715", None))
    # retranslateUi

