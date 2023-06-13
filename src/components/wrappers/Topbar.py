""" Topbar Components """

from PyQt6.QtGui import QFont, QPixmap
from PyQt6.QtWidgets import QVBoxLayout, QHBoxLayout, QWidget, QPushButton, QLabel

# Global Variabel Font
font = QFont("Karla", 15)
font.setWeight(600)

Notification_Style = """
    QPushButton {
        image : url(./assets/icons/notification.png);
        background-color : transparent;
        color: white;
        border-radius:2px;
        padding:10px
    }
    QPushButton:hover {
        background-color : #BFBFBF;
    }
"""


class Notification(QPushButton):
    def __init__(self, parent):
        super(Notification, self).__init__(parent)
        self.setStyleSheet(Notification_Style)


class Topbar(QWidget):
    text = ""
    width = 0
    height = 0
    arr = ["Dashboard", "Food Inventory", "Shopping List", "Shopping History", "Report", "Notification"]

    def __init__(self, parent):
        super(Topbar, self).__init__(parent)

        self.layer = QWidget(self)
        self.layer.setStyleSheet("background-color: #202225")
        self.layer.setContentsMargins(58, 18, 58, 18)
        self.layerLayout = QVBoxLayout()
        self.layerLayout.addWidget(self.layer)
        self.layerLayout.setContentsMargins(0, 0, 0, 0)
        self.setLayout(self.layerLayout)

        self.wrapperLayout = QHBoxLayout()
        self.layer.setLayout(self.wrapperLayout)

        self.logo = QLabel(self.layer)
        self.img = QPixmap("./assets/icons/dashboard.png")
        self.img = self.img.scaledToHeight(30)
        self.logo.setPixmap(self.img)
        self.wrapperLayout.addWidget(self.logo)

        self.title = QLabel(self.layer)
        self.title.setStyleSheet("color:white")
        self.title.setText("Dashboard")
        self.title.setFont(font)
        self.wrapperLayout.addWidget(self.title)

        self.notif = Notification(self)
        self.wrapperLayout.addStretch()
        self.wrapperLayout.addWidget(self.notif)

    def setText(self, text):
        self.text = text
        self.title.setText(text)
        if text == "Dashboard":
            self.img = QPixmap("./assets/icons/dashboard.png")
        elif text == "Food Inventory":
            self.img = QPixmap("./assets/icons/inventory.png")
        elif text == "Shopping List":
            self.img = QPixmap("./assets/icons/list.png")
        elif text == "Shopping History":
            self.img = QPixmap("./assets/icons/history.png")
        elif text == "Report":
            self.img = QPixmap("./assets/icons/report.png")
        elif text == "Notification":
            self.img = QPixmap("./assets/icons/notification.png")
        self.img = self.img.scaledToHeight(30)
        self.logo.setPixmap(self.img)

    def getButtonNotification(self):
        return self.notif

    def getSize(self):
        return self.width, self.height
