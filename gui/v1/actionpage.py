# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'actionpage.ui'
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
from PySide6.QtWidgets import (QApplication, QFrame, QHBoxLayout, QLabel,
    QPushButton, QSizePolicy, QSpacerItem, QVBoxLayout,
    QWidget)

class Ui_ActionPageFrame(object):
    def setupUi(self, ActionPageFrame):
        if not ActionPageFrame.objectName():
            ActionPageFrame.setObjectName(u"ActionPageFrame")
        ActionPageFrame.resize(835, 604)
        ActionPageFrame.setStyleSheet(u"background-color: rgb(30, 30, 30);")
        self.ActionPageLayout = QVBoxLayout(ActionPageFrame)
        self.ActionPageLayout.setSpacing(6)
        self.ActionPageLayout.setObjectName(u"ActionPageLayout")
        self.ActionPageLayout.setContentsMargins(0, 0, 0, 0)
        self.ActionPageTitleFrame = QFrame(ActionPageFrame)
        self.ActionPageTitleFrame.setObjectName(u"ActionPageTitleFrame")
        self.ActionPageTitleFrame.setMaximumSize(QSize(16777215, 50))
        self.ActionPageTitleLayout = QHBoxLayout(self.ActionPageTitleFrame)
        self.ActionPageTitleLayout.setSpacing(0)
        self.ActionPageTitleLayout.setObjectName(u"ActionPageTitleLayout")
        self.ActionPageTitleLayout.setContentsMargins(24, 0, 24, 0)
        self.PageTitle = QLabel(self.ActionPageTitleFrame)
        self.PageTitle.setObjectName(u"PageTitle")
        sizePolicy = QSizePolicy(QSizePolicy.Policy.Preferred, QSizePolicy.Policy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.PageTitle.sizePolicy().hasHeightForWidth())
        self.PageTitle.setSizePolicy(sizePolicy)
        self.PageTitle.setMinimumSize(QSize(0, 50))
        font = QFont()
        font.setFamilies([u"Segoe UI"])
        font.setPointSize(18)
        font.setBold(True)
        self.PageTitle.setFont(font)
        self.PageTitle.setStyleSheet(u"color: rgb(231, 231, 231);")
        self.PageTitle.setAlignment(Qt.AlignBottom|Qt.AlignLeading|Qt.AlignLeft)

        self.ActionPageTitleLayout.addWidget(self.PageTitle)


        self.ActionPageLayout.addWidget(self.ActionPageTitleFrame)

        self.NewFrame = QFrame(ActionPageFrame)
        self.NewFrame.setObjectName(u"NewFrame")
        self.NewLayout = QHBoxLayout(self.NewFrame)
        self.NewLayout.setObjectName(u"NewLayout")
        self.NewLayout.setContentsMargins(24, 0, 24, 0)
        self.NewSpacer = QSpacerItem(40, 20, QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Minimum)

        self.NewLayout.addItem(self.NewSpacer)

        self.NewBtn = QPushButton(self.NewFrame)
        self.NewBtn.setObjectName(u"NewBtn")
        sizePolicy1 = QSizePolicy(QSizePolicy.Policy.Maximum, QSizePolicy.Policy.Fixed)
        sizePolicy1.setHorizontalStretch(0)
        sizePolicy1.setVerticalStretch(0)
        sizePolicy1.setHeightForWidth(self.NewBtn.sizePolicy().hasHeightForWidth())
        self.NewBtn.setSizePolicy(sizePolicy1)
        self.NewBtn.setMinimumSize(QSize(60, 36))
        font1 = QFont()
        font1.setFamilies([u"Segoe UI"])
        font1.setBold(True)
        self.NewBtn.setFont(font1)
        self.NewBtn.setCursor(QCursor(Qt.CursorShape.PointingHandCursor))
        self.NewBtn.setStyleSheet(u"color: rgb(231, 231, 231);")
        self.NewBtn.setFlat(True)

        self.NewLayout.addWidget(self.NewBtn)

        self.SaveBtn = QPushButton(self.NewFrame)
        self.SaveBtn.setObjectName(u"SaveBtn")
        sizePolicy1.setHeightForWidth(self.SaveBtn.sizePolicy().hasHeightForWidth())
        self.SaveBtn.setSizePolicy(sizePolicy1)
        self.SaveBtn.setMinimumSize(QSize(60, 36))
        self.SaveBtn.setFont(font1)
        self.SaveBtn.setCursor(QCursor(Qt.CursorShape.PointingHandCursor))
        self.SaveBtn.setStyleSheet(u"color: rgb(231, 231, 231);")
        self.SaveBtn.setFlat(True)

        self.NewLayout.addWidget(self.SaveBtn)


        self.ActionPageLayout.addWidget(self.NewFrame)

        self.ActionsFrame = QFrame(ActionPageFrame)
        self.ActionsFrame.setObjectName(u"ActionsFrame")
        sizePolicy2 = QSizePolicy(QSizePolicy.Policy.Preferred, QSizePolicy.Policy.Expanding)
        sizePolicy2.setHorizontalStretch(0)
        sizePolicy2.setVerticalStretch(0)
        sizePolicy2.setHeightForWidth(self.ActionsFrame.sizePolicy().hasHeightForWidth())
        self.ActionsFrame.setSizePolicy(sizePolicy2)
        self.ActionsLayout = QVBoxLayout(self.ActionsFrame)
        self.ActionsLayout.setObjectName(u"ActionsLayout")
        self.ActionListFrame = QFrame(self.ActionsFrame)
        self.ActionListFrame.setObjectName(u"ActionListFrame")
        sizePolicy.setHeightForWidth(self.ActionListFrame.sizePolicy().hasHeightForWidth())
        self.ActionListFrame.setSizePolicy(sizePolicy)
        self.ActionListLayout = QVBoxLayout(self.ActionListFrame)
        self.ActionListLayout.setObjectName(u"ActionListLayout")

        self.ActionsLayout.addWidget(self.ActionListFrame)

        self.BindingListSpacer = QSpacerItem(20, 40, QSizePolicy.Policy.Minimum, QSizePolicy.Policy.Expanding)

        self.ActionsLayout.addItem(self.BindingListSpacer)


        self.ActionPageLayout.addWidget(self.ActionsFrame)


        self.retranslateUi(ActionPageFrame)

        QMetaObject.connectSlotsByName(ActionPageFrame)
    # setupUi

    def retranslateUi(self, ActionPageFrame):
        ActionPageFrame.setWindowTitle(QCoreApplication.translate("ActionPageFrame", u"Frame", None))
        self.PageTitle.setText(QCoreApplication.translate("ActionPageFrame", u"Actions", None))
        self.NewBtn.setText(QCoreApplication.translate("ActionPageFrame", u"New", None))
        self.SaveBtn.setText(QCoreApplication.translate("ActionPageFrame", u"Save", None))
    # retranslateUi

