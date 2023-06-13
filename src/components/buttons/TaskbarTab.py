""" Data Taskbar """

from PyQt6.QtGui import QFont
from PyQt6.QtWidgets import QPushButton

# Global Variabel Font
font = QFont("Karla", 11)
font.setWeight(600)

TaskbarTab_Style = """
    QPushButton {
        background-color: transparent;
        color: white;
        border-top-left-radius :10px;
        border-top-right-radius:10px;
        text-align:center;
    }
    QPushButton:hover {
        background-color: #4D5259;
    }

"""

TaskbarTab_Current = """
    QPushButton {
        background-color: #2F3136;
        color:white;
        border-top-left-radius :10px;
        border-top-right-radius:10px;
        text-align:center;
    }

"""


class TaskbarTab(QPushButton):
    current = False

    def __init__(self, parent, content):
        super(TaskbarTab, self).__init__(parent)
        self.height = 40
        self.width = self.size().width() + 40
        self.resize(self.width, self.height)
        self.setText(content)
        self.setFont(font)
        self.setStyleSheet(TaskbarTab_Style)

    def setCurrent(self):
        self.current = True
        self.setStyleSheet(TaskbarTab_Current)

    def setNotCurrent(self):
        self.current = False
        self.setStyleSheet(TaskbarTab_Style)

    def getWidth(self):
        return self.width
