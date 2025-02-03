# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'bindingpage.ui'
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

class Ui_BindingPageFrame(object):
    def setupUi(self, BindingPageFrame):
        if not BindingPageFrame.objectName():
            BindingPageFrame.setObjectName(u"BindingPageFrame")
        BindingPageFrame.resize(835, 604)
        BindingPageFrame.setStyleSheet(u"background-color: rgb(30, 30, 30);")
        self.BindingPageLayout = QVBoxLayout(BindingPageFrame)
        self.BindingPageLayout.setSpacing(6)
        self.BindingPageLayout.setObjectName(u"BindingPageLayout")
        self.BindingPageLayout.setContentsMargins(0, 0, 0, 0)
        self.BindingPageTitleFrame = QFrame(BindingPageFrame)
        self.BindingPageTitleFrame.setObjectName(u"BindingPageTitleFrame")
        self.BindingPageTitleFrame.setMaximumSize(QSize(16777215, 50))
        self.BindingPageTitleLayout = QHBoxLayout(self.BindingPageTitleFrame)
        self.BindingPageTitleLayout.setSpacing(0)
        self.BindingPageTitleLayout.setObjectName(u"BindingPageTitleLayout")
        self.BindingPageTitleLayout.setContentsMargins(24, 0, 24, 0)
        self.PageTitle = QLabel(self.BindingPageTitleFrame)
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

        self.BindingPageTitleLayout.addWidget(self.PageTitle)


        self.BindingPageLayout.addWidget(self.BindingPageTitleFrame)

        self.NewFrame = QFrame(BindingPageFrame)
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


        self.BindingPageLayout.addWidget(self.NewFrame)

        self.BindingsFrame = QFrame(BindingPageFrame)
        self.BindingsFrame.setObjectName(u"BindingsFrame")
        sizePolicy2 = QSizePolicy(QSizePolicy.Policy.Preferred, QSizePolicy.Policy.Expanding)
        sizePolicy2.setHorizontalStretch(0)
        sizePolicy2.setVerticalStretch(0)
        sizePolicy2.setHeightForWidth(self.BindingsFrame.sizePolicy().hasHeightForWidth())
        self.BindingsFrame.setSizePolicy(sizePolicy2)
        self.BindingsLayout = QVBoxLayout(self.BindingsFrame)
        self.BindingsLayout.setObjectName(u"BindingsLayout")
        self.BindingListFrame = QFrame(self.BindingsFrame)
        self.BindingListFrame.setObjectName(u"BindingListFrame")
        sizePolicy.setHeightForWidth(self.BindingListFrame.sizePolicy().hasHeightForWidth())
        self.BindingListFrame.setSizePolicy(sizePolicy)
        self.BindingListLayout = QVBoxLayout(self.BindingListFrame)
        self.BindingListLayout.setObjectName(u"BindingListLayout")

        self.BindingsLayout.addWidget(self.BindingListFrame)

        self.BindingListSpacer = QSpacerItem(20, 40, QSizePolicy.Policy.Minimum, QSizePolicy.Policy.Expanding)

        self.BindingsLayout.addItem(self.BindingListSpacer)


        self.BindingPageLayout.addWidget(self.BindingsFrame)


        self.retranslateUi(BindingPageFrame)

        QMetaObject.connectSlotsByName(BindingPageFrame)
    # setupUi

    def retranslateUi(self, BindingPageFrame):
        BindingPageFrame.setWindowTitle(QCoreApplication.translate("BindingPageFrame", u"Frame", None))
        self.PageTitle.setText(QCoreApplication.translate("BindingPageFrame", u"Bindings", None))
        self.NewBtn.setText(QCoreApplication.translate("BindingPageFrame", u"New", None))
        self.SaveBtn.setText(QCoreApplication.translate("BindingPageFrame", u"Save", None))
    # retranslateUi

