""" Data Taskbar """

from PyQt6.QtGui import QFont
from PyQt6.QtWidgets import QWidget, QPushButton, QHBoxLayout, QSizePolicy

# Global Variabel Font
font = QFont("Karla", 11)
font.setWeight(600)

TaskbarTab_Style = """
    QPushButton {
        background-color: transparent;
        color: white;
        border-top-left-radius :10px;
        border-top-right-radius:10px;
        border-bottom-left-radius :0;
        border-bottom-right-radius:0;
        text-align:center;
        padding: 10px 28px;
    }
    QPushButton:hover {
        background-color: #4D5259;
    }

"""

TaskbarTab_Current = """
    QPushButton {
        background-color: #2F3136;
        color:white;
        border-top-left-radius: 10px;
        border-top-right-radius:10px;
        border-bottom-left-radius :0;
        border-bottom-right-radius:0;
        text-align:center;
        padding: 10px 28px;
    }

"""


class TaskbarTab(QPushButton):
    current = False

    def __init__(self, parent, content):
        super(TaskbarTab, self).__init__(parent)
        self.setText(content)
        self.setFont(font)
        self.setStyleSheet(TaskbarTab_Style)
        self.setSizePolicy(QSizePolicy.Policy.Fixed, QSizePolicy.Policy.Fixed)

    def setCurrent(self):
        self.current = True
        self.setStyleSheet(TaskbarTab_Current)

    def setNotCurrent(self):
        self.current = False
        self.setStyleSheet(TaskbarTab_Style)

    def getWidth(self):
        return self.width


class Taskbar(QWidget):
    def __init__(self, parent):
        super(Taskbar, self).__init__(parent)

        self.currentIndex = 0

        self.layer = QWidget(self)
        self.layer.setStyleSheet("background-color: transparent")
        self.layerContainer = QHBoxLayout()
        self.layerContainer.setContentsMargins(0, 0, 0, 0)
        self.layerContainer.addWidget(self.layer)

        self.contentLayout = QHBoxLayout()
        self.contentLayout.setSpacing(0)
        self.contentLayout.setContentsMargins(0, 0, 0, 0)
        self.layer.setLayout(self.contentLayout)

        self.allFood = TaskbarTab(self.layer, "All Foods")
        self.contentLayout.addWidget(self.allFood)

        self.goodFood = TaskbarTab(self.layer, "Good")
        self.contentLayout.addWidget(self.goodFood)

        self.staleFood = TaskbarTab(self.layer, "Stale")
        self.contentLayout.addWidget(self.staleFood)

        self.expiredFood = TaskbarTab(self.layer, "Expired")
        self.contentLayout.addWidget(self.expiredFood)

        self.consumedFood = TaskbarTab(self.layer, "Consumed")
        self.contentLayout.addWidget(self.consumedFood)
        self.contentLayout.addStretch()

        self.setLayout(self.layerContainer)

        self.display()

        self.allFood.clicked.connect(lambda: self.changeIndex(0))
        self.goodFood.clicked.connect(lambda: self.changeIndex(1))
        self.staleFood.clicked.connect(lambda: self.changeIndex(2))
        self.expiredFood.clicked.connect(lambda: self.changeIndex(3))
        self.consumedFood.clicked.connect(lambda: self.changeIndex(4))

    def display(self):
        if (self.currentIndex == 0):
            self.allFood.setCurrent()
        else:
            self.allFood.setNotCurrent()

        if (self.currentIndex == 1):
            self.goodFood.setCurrent()
        else:
            self.goodFood.setNotCurrent()

        if (self.currentIndex == 2):
            self.staleFood.setCurrent()
        else:
            self.staleFood.setNotCurrent()

        if (self.currentIndex == 3):
            self.expiredFood.setCurrent()
        else:
            self.expiredFood.setNotCurrent()

        if (self.currentIndex == 4):
            self.consumedFood.setCurrent()
        else:
            self.consumedFood.setNotCurrent()

    def changeIndex(self, n):
        if (n != self.currentIndex):
            self.currentIndex = n
            self.display()

    def getButtonAllFood(self):
        return self.allFood

    def getButtonGoodFood(self):
        return self.goodFood

    def getButtonStaleFood(self):
        return self.staleFood

    def getButtonExpiredFood(self):
        return self.expiredFood

    def getButtonConsumedFood(self):
        return self.consumedFood

    def getSize(self):
        return (self.width, self.height)
