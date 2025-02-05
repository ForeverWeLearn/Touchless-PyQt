# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'settingpage.ui'
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
from PySide6.QtWidgets import (QApplication, QCheckBox, QComboBox, QFrame,
    QHBoxLayout, QLabel, QSizePolicy, QSpacerItem,
    QVBoxLayout, QWidget)

class Ui_SettingPageFrame(object):
    def setupUi(self, SettingPageFrame):
        if not SettingPageFrame.objectName():
            SettingPageFrame.setObjectName(u"SettingPageFrame")
        SettingPageFrame.resize(346, 181)
        SettingPageFrame.setStyleSheet(u"background-color: rgb(30, 30, 30);")
        self.verticalLayout = QVBoxLayout(SettingPageFrame)
        self.verticalLayout.setObjectName(u"verticalLayout")
        self.verticalLayout.setContentsMargins(24, 0, -1, -1)
        self.PageNameLabel = QLabel(SettingPageFrame)
        self.PageNameLabel.setObjectName(u"PageNameLabel")
        self.PageNameLabel.setMinimumSize(QSize(0, 50))
        font = QFont()
        font.setPointSize(18)
        font.setBold(True)
        self.PageNameLabel.setFont(font)
        self.PageNameLabel.setStyleSheet(u"color: rgb(231, 231, 231);")
        self.PageNameLabel.setAlignment(Qt.AlignBottom|Qt.AlignLeading|Qt.AlignLeft)

        self.verticalLayout.addWidget(self.PageNameLabel)

        self.SettingPageContentFrame = QFrame(SettingPageFrame)
        self.SettingPageContentFrame.setObjectName(u"SettingPageContentFrame")
        self.SettingPageContentLayout = QVBoxLayout(self.SettingPageContentFrame)
        self.SettingPageContentLayout.setObjectName(u"SettingPageContentLayout")
        self.SettingPageContentLayout.setContentsMargins(0, 20, 0, 0)
        self.ThemeFrame = QFrame(self.SettingPageContentFrame)
        self.ThemeFrame.setObjectName(u"ThemeFrame")
        sizePolicy = QSizePolicy(QSizePolicy.Policy.Fixed, QSizePolicy.Policy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.ThemeFrame.sizePolicy().hasHeightForWidth())
        self.ThemeFrame.setSizePolicy(sizePolicy)
        self.ThemeFrame.setMinimumSize(QSize(200, 0))
        self.ThemeLayout = QHBoxLayout(self.ThemeFrame)
        self.ThemeLayout.setSpacing(24)
        self.ThemeLayout.setObjectName(u"ThemeLayout")
        self.ThemeLayout.setContentsMargins(0, 0, 0, 0)
        self.ThemeLabel = QLabel(self.ThemeFrame)
        self.ThemeLabel.setObjectName(u"ThemeLabel")
        self.ThemeLabel.setStyleSheet(u"color: rgb(231, 231, 231);")

        self.ThemeLayout.addWidget(self.ThemeLabel)

        self.ThemeBox = QComboBox(self.ThemeFrame)
        self.ThemeBox.addItem("")
        self.ThemeBox.addItem("")
        self.ThemeBox.addItem("")
        self.ThemeBox.setObjectName(u"ThemeBox")
        sizePolicy.setHeightForWidth(self.ThemeBox.sizePolicy().hasHeightForWidth())
        self.ThemeBox.setSizePolicy(sizePolicy)
        self.ThemeBox.setCursor(QCursor(Qt.CursorShape.PointingHandCursor))
        self.ThemeBox.setStyleSheet(u"color: rgb(231, 231, 231);")

        self.ThemeLayout.addWidget(self.ThemeBox)


        self.SettingPageContentLayout.addWidget(self.ThemeFrame)

        self.AutoStartFrame = QFrame(self.SettingPageContentFrame)
        self.AutoStartFrame.setObjectName(u"AutoStartFrame")
        sizePolicy.setHeightForWidth(self.AutoStartFrame.sizePolicy().hasHeightForWidth())
        self.AutoStartFrame.setSizePolicy(sizePolicy)
        self.AutoStartFrame.setMinimumSize(QSize(200, 0))
        self.AutoStartLayout = QHBoxLayout(self.AutoStartFrame)
        self.AutoStartLayout.setSpacing(24)
        self.AutoStartLayout.setObjectName(u"AutoStartLayout")
        self.AutoStartLayout.setContentsMargins(0, 0, 0, 0)
        self.AutoStartLabel = QLabel(self.AutoStartFrame)
        self.AutoStartLabel.setObjectName(u"AutoStartLabel")
        self.AutoStartLabel.setStyleSheet(u"color: rgb(231, 231, 231);")

        self.AutoStartLayout.addWidget(self.AutoStartLabel)

        self.AutoStartBox = QCheckBox(self.AutoStartFrame)
        self.AutoStartBox.setObjectName(u"AutoStartBox")
        sizePolicy.setHeightForWidth(self.AutoStartBox.sizePolicy().hasHeightForWidth())
        self.AutoStartBox.setSizePolicy(sizePolicy)
        self.AutoStartBox.setCursor(QCursor(Qt.CursorShape.PointingHandCursor))

        self.AutoStartLayout.addWidget(self.AutoStartBox)


        self.SettingPageContentLayout.addWidget(self.AutoStartFrame)

        self.verticalSpacer = QSpacerItem(20, 40, QSizePolicy.Policy.Minimum, QSizePolicy.Policy.Expanding)

        self.SettingPageContentLayout.addItem(self.verticalSpacer)


        self.verticalLayout.addWidget(self.SettingPageContentFrame)


        self.retranslateUi(SettingPageFrame)

        QMetaObject.connectSlotsByName(SettingPageFrame)
    # setupUi

    def retranslateUi(self, SettingPageFrame):
        SettingPageFrame.setWindowTitle(QCoreApplication.translate("SettingPageFrame", u"Frame", None))
        self.PageNameLabel.setText(QCoreApplication.translate("SettingPageFrame", u"Settings", None))
        self.ThemeLabel.setText(QCoreApplication.translate("SettingPageFrame", u"Theme", None))
        self.ThemeBox.setItemText(0, QCoreApplication.translate("SettingPageFrame", u"Dark", None))
        self.ThemeBox.setItemText(1, QCoreApplication.translate("SettingPageFrame", u"Light", None))
        self.ThemeBox.setItemText(2, QCoreApplication.translate("SettingPageFrame", u"Purple", None))

        self.AutoStartLabel.setText(QCoreApplication.translate("SettingPageFrame", u"Auto start on launch", None))
        self.AutoStartBox.setText("")
    # retranslateUi

