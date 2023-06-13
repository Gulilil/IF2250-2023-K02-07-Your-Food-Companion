""" Data Taskbar """

from PyQt6.QtWidgets import QWidget
from src.components.buttons.TaskbarTab import TaskbarTab


class ShoppingListTaskbar(QWidget):
    currentIndex = 0

    def __init__(self, parent, parentW):
        super(ShoppingListTaskbar, self).__init__(parent)
        self.width = parentW
        self.height = 40
        self.resize(self.width, self.height)
        self.move(0, 5)

        self.layer = QWidget(self)
        self.layer.resize(self.width, self.height)
        self.layer.setStyleSheet("background-color: transparent")

        self.allFood = TaskbarTab(self.layer, "All Foods")
        self.allFood.move(0, 0)

        self.high = TaskbarTab(self.layer, "High Priority")
        self.high.move(self.allFood.getWidth(), 0)

        self.medium = TaskbarTab(self.layer, "Medium Priority")
        self.medium.move(self.allFood.getWidth() + self.high.getWidth(), 0)

        self.low = TaskbarTab(self.layer, "Low Priority")
        self.low.move(self.allFood.getWidth() + self.high.getWidth() + self.medium.getWidth(), 0)

        self.display()

    def display(self):
        if (self.currentIndex == 0):
            self.allFood.setCurrent()
        else:
            self.allFood.setNotCurrent()
        self.allFood.clicked.connect(lambda: self.changeIndex(0))

        if (self.currentIndex == 1):
            self.high.setCurrent()
        else:
            self.high.setNotCurrent()
        self.high.clicked.connect(lambda: self.changeIndex(1))

        if (self.currentIndex == 2):
            self.medium.setCurrent()
        else:
            self.medium.setNotCurrent()
        self.medium.clicked.connect(lambda: self.changeIndex(2))

        if (self.currentIndex == 3):
            self.low.setCurrent()
        else:
            self.low.setNotCurrent()
        self.low.clicked.connect(lambda: self.changeIndex(3))

    def changeIndex(self, n):
        if (n != self.currentIndex):
            self.currentIndex = n
            self.display()

    def getButtonAllFood(self):
        return self.allFood

    def getButtonHighPriority(self):
        return self.high

    def getButtonMediumPriority(self):
        return self.medium

    def getButtonLowPriority(self):
        return self.low

    def getSize(self):
        return (self.width, self.height)
