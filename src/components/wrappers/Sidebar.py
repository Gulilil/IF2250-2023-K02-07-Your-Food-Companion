""" Sidebar Components """

from PyQt6 import QtGui, QtCore
from PyQt6.QtGui import QFont, QPixmap
from PyQt6.QtWidgets import QVBoxLayout, QWidget, QPushButton, QLabel, QSizePolicy
from src.components.buttons.Button import Button

# Global Variabel Font
font = QFont("Karla", 13)
font.setWeight(600)

SidebarTab_Style = """
    QPushButton {
        background : transparent;
        color : #FFFFFF;
        border-radius: 8px;
        text-align:left;
        padding: 9px 30px;
    }
    QPushButton:hover {
        color : #897DCF;
    }
"""

SidebarTab_Current = """
    QPushButton {
        background : #897DCF;
        color : #FFFFFF;
        border-radius: 8px;
        text-align:left;
        padding: 9px 30px;
    }
"""


class SidebarTab(QPushButton):
    current = False

    def __init__(self, parent, content):
        super(SidebarTab, self).__init__(parent)

        self.setContentsMargins(24, 9, 24, 9)
        self.setText("   " + content)
        self.setFont(font)
        if content == "Dashboard":
            self.setIcon(QtGui.QIcon("./assets/icons/dashboard.png"))
        elif content == "Food Inventory":
            self.setIcon(QtGui.QIcon("./assets/icons/inventory.png"))
        elif content == "Shopping List":
            self.setIcon(QtGui.QIcon("./assets/icons/list.png"))
        elif content == "Shopping History":
            self.setIcon(QtGui.QIcon("./assets/icons/history.png"))
        elif content == "Report":
            self.setIcon(QtGui.QIcon("./assets/icons/report.png"))
        style = SidebarTab_Style
        self.setStyleSheet(style)

    def setCurrent(self):
        self.current = True
        self.setStyleSheet(SidebarTab_Current)

    def setNotCurrent(self):
        self.current = False
        self.setStyleSheet(SidebarTab_Style)


class Sidebar(QWidget):
    currentIndex = 0
    width = 0
    height = 0

    def __init__(self, parent):
        super(Sidebar, self).__init__(parent)

        self.layer = QWidget(self)
        self.layer.setMaximumWidth(350)
        self.layer.setStyleSheet("background-color: #202225")
        self.layer.setSizePolicy(QSizePolicy.Policy.Fixed, QSizePolicy.Policy.Expanding)
        self.layer.setContentsMargins(24, 20, 24, 20)
        self.layerLayout = QVBoxLayout()
        self.layerLayout.addWidget(self.layer)
        self.setLayout(self.layerLayout)

        self.contentLayout = QVBoxLayout()
        self.contentLayout.setSpacing(40)
        self.layer.setLayout(self.contentLayout)

        self.title = QLabel(self.layer)
        img = QPixmap("./assets/icons/logo-sidebar-resize.png")
        img = img.scaledToHeight(75)
        self.title.setPixmap(img)
        self.title.setSizePolicy(QSizePolicy.Policy.Fixed, QSizePolicy.Policy.Fixed)
        self.contentLayout.addWidget(self.title)

        self.tabLayout = QVBoxLayout()
        self.tabLayout.setSpacing(12)
        self.contentLayout.addLayout(self.tabLayout)

        self.dashboard = SidebarTab(self.layer, "Dashboard")
        self.dashboard.setSizePolicy(QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Fixed)
        self.dashboard.setCursor(QtGui.QCursor(QtCore.Qt.CursorShape.PointingHandCursor))
        self.tabLayout.addWidget(self.dashboard)

        self.foodInventory = SidebarTab(self.layer, "Food Inventory")
        self.foodInventory.setSizePolicy(QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Fixed)
        self.foodInventory.setCursor(QtGui.QCursor(QtCore.Qt.CursorShape.PointingHandCursor))
        self.tabLayout.addWidget(self.foodInventory)

        self.shoppingList = SidebarTab(self.layer, "Shopping List")
        self.shoppingList.setSizePolicy(QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Fixed)
        self.shoppingList.setCursor(QtGui.QCursor(QtCore.Qt.CursorShape.PointingHandCursor))
        self.tabLayout.addWidget(self.shoppingList)

        self.shoppingHistory = SidebarTab(self.layer, "Shopping History")
        self.shoppingHistory.setSizePolicy(QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Fixed)
        self.shoppingHistory.setCursor(QtGui.QCursor(QtCore.Qt.CursorShape.PointingHandCursor))
        self.tabLayout.addWidget(self.shoppingHistory)

        self.report = SidebarTab(self.layer, "Report")
        self.report.setSizePolicy(QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Fixed)
        self.report.setCursor(QtGui.QCursor(QtCore.Qt.CursorShape.PointingHandCursor))
        self.tabLayout.addWidget(self.report)

        self.quitButton = Button(self.layer, "Small")
        self.quitButton.setText("Quit")
        self.quitButton.move(30, 700)

        self.tabLayout.addStretch()
        self.contentLayout.addStretch()

        self.display()

        self.dashboard.clicked.connect(lambda: self.changeIndex(0))
        self.foodInventory.clicked.connect(lambda: self.changeIndex(1))
        self.shoppingList.clicked.connect(lambda: self.changeIndex(2))
        self.shoppingHistory.clicked.connect(lambda: self.changeIndex(3))
        self.report.clicked.connect(lambda: self.changeIndex(4))

    def display(self):
        if self.currentIndex == 0:
            self.dashboard.setCurrent()
        else:
            self.dashboard.setNotCurrent()

        if self.currentIndex == 1:
            self.foodInventory.setCurrent()
        else:
            self.foodInventory.setNotCurrent()

        if self.currentIndex == 2:
            self.shoppingList.setCurrent()
        else:
            self.shoppingList.setNotCurrent()

        if self.currentIndex == 3:
            self.shoppingHistory.setCurrent()
        else:
            self.shoppingHistory.setNotCurrent()

        if self.currentIndex == 4:
            self.report.setCurrent()
        else:
            self.report.setNotCurrent()

    def changeIndex(self, n):
        if n != self.currentIndex:
            self.currentIndex = n
            self.display()

    def getSize(self):
        return self.width, self.height

    def getCurrentIndex(self):
        return self.currentIndex

    def getButtonDashboard(self):
        return self.dashboard

    def getButtonInventory(self):
        return self.foodInventory

    def getButtonShoppingList(self):
        return self.shoppingList

    def getButtonShoppingHistory(self):
        return self.shoppingHistory

    def getButtonReport(self):
        return self.report

    def getButtonQuit(self):
        return self.quitButton

    def getWidget(self):
        return self.layer
