# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'homepage.ui'
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
    QPushButton, QSizePolicy, QVBoxLayout, QWidget)

class Ui_HomePageFrame(object):
    def setupUi(self, HomePageFrame):
        if not HomePageFrame.objectName():
            HomePageFrame.setObjectName(u"HomePageFrame")
        HomePageFrame.resize(486, 234)
        HomePageFrame.setStyleSheet(u"background-color: rgb(30, 30, 30);")
        self.HomePageLayout = QVBoxLayout(HomePageFrame)
        self.HomePageLayout.setObjectName(u"HomePageLayout")
        self.HomePageLayout.setContentsMargins(0, 0, 0, 0)
        self.HomePageTitleFrame = QFrame(HomePageFrame)
        self.HomePageTitleFrame.setObjectName(u"HomePageTitleFrame")
        sizePolicy = QSizePolicy(QSizePolicy.Policy.Preferred, QSizePolicy.Policy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.HomePageTitleFrame.sizePolicy().hasHeightForWidth())
        self.HomePageTitleFrame.setSizePolicy(sizePolicy)
        self.HomePageTitleFrame.setMinimumSize(QSize(0, 50))
        font = QFont()
        font.setFamilies([u"Segoe UI"])
        font.setPointSize(18)
        font.setBold(True)
        self.HomePageTitleFrame.setFont(font)
        self.HomePageTitleLayout = QHBoxLayout(self.HomePageTitleFrame)
        self.HomePageTitleLayout.setSpacing(0)
        self.HomePageTitleLayout.setObjectName(u"HomePageTitleLayout")
        self.HomePageTitleLayout.setContentsMargins(24, 0, 0, 0)
        self.HomeLabel = QLabel(self.HomePageTitleFrame)
        self.HomeLabel.setObjectName(u"HomeLabel")
        self.HomeLabel.setFont(font)
        self.HomeLabel.setStyleSheet(u"color: rgb(231, 231, 231);")
        self.HomeLabel.setAlignment(Qt.AlignBottom|Qt.AlignLeading|Qt.AlignLeft)

        self.HomePageTitleLayout.addWidget(self.HomeLabel)


        self.HomePageLayout.addWidget(self.HomePageTitleFrame)

        self.HomePageHeaderFrame = QFrame(HomePageFrame)
        self.HomePageHeaderFrame.setObjectName(u"HomePageHeaderFrame")
        sizePolicy.setHeightForWidth(self.HomePageHeaderFrame.sizePolicy().hasHeightForWidth())
        self.HomePageHeaderFrame.setSizePolicy(sizePolicy)
        self.HomePageHeaderFrame.setStyleSheet(u"background-color: rgb(30, 30, 30);")
        self.HomePageHeaderLayout = QHBoxLayout(self.HomePageHeaderFrame)
        self.HomePageHeaderLayout.setSpacing(6)
        self.HomePageHeaderLayout.setObjectName(u"HomePageHeaderLayout")
        self.HomePageHeaderLayout.setContentsMargins(20, 0, 20, 0)
        self.StartBtn = QPushButton(self.HomePageHeaderFrame)
        self.StartBtn.setObjectName(u"StartBtn")
        sizePolicy1 = QSizePolicy(QSizePolicy.Policy.Fixed, QSizePolicy.Policy.Expanding)
        sizePolicy1.setHorizontalStretch(0)
        sizePolicy1.setVerticalStretch(0)
        sizePolicy1.setHeightForWidth(self.StartBtn.sizePolicy().hasHeightForWidth())
        self.StartBtn.setSizePolicy(sizePolicy1)
        font1 = QFont()
        font1.setFamilies([u"Segoe UI"])
        font1.setBold(False)
        self.StartBtn.setFont(font1)
        self.StartBtn.setCursor(QCursor(Qt.CursorShape.PointingHandCursor))
        self.StartBtn.setStyleSheet(u"border-color: rgb(35, 255, 156);\n"
"color: rgb(231, 231, 231);")
        self.StartBtn.setFlat(False)

        self.HomePageHeaderLayout.addWidget(self.StartBtn)

        self.StopBtn = QPushButton(self.HomePageHeaderFrame)
        self.StopBtn.setObjectName(u"StopBtn")
        sizePolicy1.setHeightForWidth(self.StopBtn.sizePolicy().hasHeightForWidth())
        self.StopBtn.setSizePolicy(sizePolicy1)
        font2 = QFont()
        font2.setFamilies([u"Segoe UI"])
        self.StopBtn.setFont(font2)
        self.StopBtn.setCursor(QCursor(Qt.CursorShape.PointingHandCursor))
        self.StopBtn.setStyleSheet(u"color: rgb(231, 231, 231);")
        self.StopBtn.setFlat(True)

        self.HomePageHeaderLayout.addWidget(self.StopBtn)

        self.horizontalFrame = QFrame(self.HomePageHeaderFrame)
        self.horizontalFrame.setObjectName(u"horizontalFrame")
        self.horizontalLayout = QHBoxLayout(self.horizontalFrame)
        self.horizontalLayout.setSpacing(0)
        self.horizontalLayout.setObjectName(u"horizontalLayout")
        self.horizontalLayout.setContentsMargins(10, 0, 0, 0)
        self.LogLabel = QLabel(self.horizontalFrame)
        self.LogLabel.setObjectName(u"LogLabel")
        sizePolicy2 = QSizePolicy(QSizePolicy.Policy.Preferred, QSizePolicy.Policy.Expanding)
        sizePolicy2.setHorizontalStretch(0)
        sizePolicy2.setVerticalStretch(0)
        sizePolicy2.setHeightForWidth(self.LogLabel.sizePolicy().hasHeightForWidth())
        self.LogLabel.setSizePolicy(sizePolicy2)
        self.LogLabel.setMinimumSize(QSize(0, 36))
        font3 = QFont()
        font3.setFamilies([u"Segoe UI"])
        font3.setItalic(False)
        self.LogLabel.setFont(font3)
        self.LogLabel.setStyleSheet(u"color: rgb(168, 168, 168);")
        self.LogLabel.setAlignment(Qt.AlignLeading|Qt.AlignLeft|Qt.AlignVCenter)

        self.horizontalLayout.addWidget(self.LogLabel)


        self.HomePageHeaderLayout.addWidget(self.horizontalFrame)

        self.ShowPreviewBtn = QPushButton(self.HomePageHeaderFrame)
        self.ShowPreviewBtn.setObjectName(u"ShowPreviewBtn")
        sizePolicy3 = QSizePolicy(QSizePolicy.Policy.Minimum, QSizePolicy.Policy.Expanding)
        sizePolicy3.setHorizontalStretch(0)
        sizePolicy3.setVerticalStretch(0)
        sizePolicy3.setHeightForWidth(self.ShowPreviewBtn.sizePolicy().hasHeightForWidth())
        self.ShowPreviewBtn.setSizePolicy(sizePolicy3)
        self.ShowPreviewBtn.setMaximumSize(QSize(100, 16777215))
        self.ShowPreviewBtn.setCursor(QCursor(Qt.CursorShape.PointingHandCursor))
        self.ShowPreviewBtn.setStyleSheet(u"color: rgb(231, 231, 231);")
        self.ShowPreviewBtn.setCheckable(True)
        self.ShowPreviewBtn.setFlat(True)

        self.HomePageHeaderLayout.addWidget(self.ShowPreviewBtn)


        self.HomePageLayout.addWidget(self.HomePageHeaderFrame)

        self.VideoFrame = QFrame(HomePageFrame)
        self.VideoFrame.setObjectName(u"VideoFrame")
        self.VideoLayout = QHBoxLayout(self.VideoFrame)
        self.VideoLayout.setSpacing(0)
        self.VideoLayout.setObjectName(u"VideoLayout")
        self.VideoLayout.setContentsMargins(9, 0, 9, 9)
        self.VideoLabel = QLabel(self.VideoFrame)
        self.VideoLabel.setObjectName(u"VideoLabel")
        font4 = QFont()
        font4.setFamilies([u"Segoe UI"])
        font4.setPointSize(18)
        font4.setItalic(False)
        self.VideoLabel.setFont(font4)
        self.VideoLabel.setStyleSheet(u"background-color: rgb(25, 25, 25);\n"
"color: rgb(48, 48, 48);")
        self.VideoLabel.setAlignment(Qt.AlignCenter)

        self.VideoLayout.addWidget(self.VideoLabel)


        self.HomePageLayout.addWidget(self.VideoFrame)


        self.retranslateUi(HomePageFrame)

        QMetaObject.connectSlotsByName(HomePageFrame)
    # setupUi

    def retranslateUi(self, HomePageFrame):
        HomePageFrame.setWindowTitle(QCoreApplication.translate("HomePageFrame", u"Frame", None))
        self.HomeLabel.setText(QCoreApplication.translate("HomePageFrame", u"Home", None))
        self.StartBtn.setText(QCoreApplication.translate("HomePageFrame", u"Start", None))
        self.StopBtn.setText(QCoreApplication.translate("HomePageFrame", u"Stop", None))
        self.LogLabel.setText(QCoreApplication.translate("HomePageFrame", u"Whatever running shown here...", None))
        self.ShowPreviewBtn.setText(QCoreApplication.translate("HomePageFrame", u"Show preview", None))
        self.VideoLabel.setText(QCoreApplication.translate("HomePageFrame", u"Preview", None))
    # retranslateUi

