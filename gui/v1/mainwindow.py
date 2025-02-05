# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'mainwindow.ui'
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
from PySide6.QtWidgets import (QApplication, QFrame, QHBoxLayout, QMainWindow,
    QPushButton, QSizePolicy, QSpacerItem, QVBoxLayout,
    QWidget)

class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        if not MainWindow.objectName():
            MainWindow.setObjectName(u"MainWindow")
        MainWindow.resize(720, 480)
        MainWindow.setMinimumSize(QSize(720, 480))
        MainWindow.setMaximumSize(QSize(720, 480))
        MainWindow.setStyleSheet(u"color: rgb(231, 231, 231);")
        self.CentralWidget = QWidget(MainWindow)
        self.CentralWidget.setObjectName(u"CentralWidget")
        self.CentralWidget.setStyleSheet(u"background-color: rgb(30, 30, 30);")
        self.CentralWidgetLayout = QVBoxLayout(self.CentralWidget)
        self.CentralWidgetLayout.setSpacing(0)
        self.CentralWidgetLayout.setObjectName(u"CentralWidgetLayout")
        self.CentralWidgetLayout.setContentsMargins(0, 0, 0, 0)
        self.PagesFrame = QFrame(self.CentralWidget)
        self.PagesFrame.setObjectName(u"PagesFrame")
        self.PagesFrame.setStyleSheet(u"background-color: rgb(30, 30, 30);")
        self.PagesLayout = QHBoxLayout(self.PagesFrame)
        self.PagesLayout.setSpacing(0)
        self.PagesLayout.setObjectName(u"PagesLayout")
        self.PagesLayout.setContentsMargins(0, 0, 0, 0)
        self.SidebarFrame = QFrame(self.PagesFrame)
        self.SidebarFrame.setObjectName(u"SidebarFrame")
        sizePolicy = QSizePolicy(QSizePolicy.Policy.Minimum, QSizePolicy.Policy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.SidebarFrame.sizePolicy().hasHeightForWidth())
        self.SidebarFrame.setSizePolicy(sizePolicy)
        self.SidebarFrame.setMinimumSize(QSize(50, 0))
        self.SidebarFrame.setMaximumSize(QSize(50, 16777215))
        self.SidebarFrame.setStyleSheet(u"background-color: rgb(25, 25, 25);")
        self.SidebarLayout = QVBoxLayout(self.SidebarFrame)
        self.SidebarLayout.setSpacing(3)
        self.SidebarLayout.setObjectName(u"SidebarLayout")
        self.SidebarLayout.setContentsMargins(3, 3, 3, 3)
        self.HomeBtn = QPushButton(self.SidebarFrame)
        self.HomeBtn.setObjectName(u"HomeBtn")
        self.HomeBtn.setMinimumSize(QSize(0, 44))
        font = QFont()
        font.setFamilies([u"Tektur"])
        font.setPointSize(7)
        font.setStyleStrategy(QFont.PreferAntialias)
        self.HomeBtn.setFont(font)
        self.HomeBtn.setCursor(QCursor(Qt.CursorShape.PointingHandCursor))
        self.HomeBtn.setStyleSheet(u"color: rgb(231, 231, 231);")
        icon = QIcon()
        icon.addFile(u"imgs/home.png", QSize(), QIcon.Mode.Normal, QIcon.State.Off)
        self.HomeBtn.setIcon(icon)
        self.HomeBtn.setCheckable(True)
        self.HomeBtn.setChecked(True)
        self.HomeBtn.setAutoExclusive(True)
        self.HomeBtn.setFlat(True)

        self.SidebarLayout.addWidget(self.HomeBtn)

        self.BindingBtn = QPushButton(self.SidebarFrame)
        self.BindingBtn.setObjectName(u"BindingBtn")
        self.BindingBtn.setMinimumSize(QSize(0, 44))
        self.BindingBtn.setFont(font)
        self.BindingBtn.setCursor(QCursor(Qt.CursorShape.PointingHandCursor))
        self.BindingBtn.setStyleSheet(u"color: rgb(231, 231, 231);")
        icon1 = QIcon()
        icon1.addFile(u"imgs/conversion_path.png", QSize(), QIcon.Mode.Normal, QIcon.State.Off)
        self.BindingBtn.setIcon(icon1)
        self.BindingBtn.setCheckable(True)
        self.BindingBtn.setAutoExclusive(True)
        self.BindingBtn.setFlat(True)

        self.SidebarLayout.addWidget(self.BindingBtn)

        self.ActionBtn = QPushButton(self.SidebarFrame)
        self.ActionBtn.setObjectName(u"ActionBtn")
        self.ActionBtn.setMinimumSize(QSize(0, 44))
        self.ActionBtn.setFont(font)
        self.ActionBtn.setCursor(QCursor(Qt.CursorShape.PointingHandCursor))
        self.ActionBtn.setStyleSheet(u"color: rgb(231, 231, 231);")
        icon2 = QIcon()
        icon2.addFile(u"imgs/code.png", QSize(), QIcon.Mode.Normal, QIcon.State.Off)
        self.ActionBtn.setIcon(icon2)
        self.ActionBtn.setCheckable(True)
        self.ActionBtn.setAutoExclusive(True)
        self.ActionBtn.setFlat(True)

        self.SidebarLayout.addWidget(self.ActionBtn)

        self.SidebarSpacer = QSpacerItem(0, 0, QSizePolicy.Policy.Minimum, QSizePolicy.Policy.Expanding)

        self.SidebarLayout.addItem(self.SidebarSpacer)

        self.SettingBtn = QPushButton(self.SidebarFrame)
        self.SettingBtn.setObjectName(u"SettingBtn")
        self.SettingBtn.setMinimumSize(QSize(0, 44))
        self.SettingBtn.setFont(font)
        self.SettingBtn.setCursor(QCursor(Qt.CursorShape.PointingHandCursor))
        self.SettingBtn.setStyleSheet(u"color: rgb(231, 231, 231);")
        icon3 = QIcon()
        icon3.addFile(u"imgs/settings.png", QSize(), QIcon.Mode.Normal, QIcon.State.Off)
        self.SettingBtn.setIcon(icon3)
        self.SettingBtn.setCheckable(True)
        self.SettingBtn.setChecked(False)
        self.SettingBtn.setAutoExclusive(True)
        self.SettingBtn.setFlat(True)

        self.SidebarLayout.addWidget(self.SettingBtn)


        self.PagesLayout.addWidget(self.SidebarFrame)

        self.PageFrame = QFrame(self.PagesFrame)
        self.PageFrame.setObjectName(u"PageFrame")
        self.PageLayout = QVBoxLayout(self.PageFrame)
        self.PageLayout.setSpacing(0)
        self.PageLayout.setObjectName(u"PageLayout")
        self.PageLayout.setContentsMargins(0, 0, 0, 0)
        self.PageContentFrame = QFrame(self.PageFrame)
        self.PageContentFrame.setObjectName(u"PageContentFrame")
        self.PageContentLayout = QVBoxLayout(self.PageContentFrame)
        self.PageContentLayout.setSpacing(0)
        self.PageContentLayout.setObjectName(u"PageContentLayout")
        self.PageContentLayout.setContentsMargins(0, 0, 0, 0)

        self.PageLayout.addWidget(self.PageContentFrame)


        self.PagesLayout.addWidget(self.PageFrame)


        self.CentralWidgetLayout.addWidget(self.PagesFrame)

        MainWindow.setCentralWidget(self.CentralWidget)

        self.retranslateUi(MainWindow)

        self.HomeBtn.setDefault(True)


        QMetaObject.connectSlotsByName(MainWindow)
    # setupUi

    def retranslateUi(self, MainWindow):
        MainWindow.setWindowTitle(QCoreApplication.translate("MainWindow", u"MainWindow", None))
        self.BindingBtn.setText("")
        self.ActionBtn.setText("")
        self.SettingBtn.setText("")
    # retranslateUi

