""" Button Components """

from PyQt6.QtCore import Qt
from PyQt6.QtGui import QFont
from PyQt6.QtWidgets import QPushButton

Button_Style = """
    QPushButton {
        background-color: #9987FF; 
        color : #F2F3F5;
        border-radius : 7px;
        padding: 12px;
    }
    QPushButton:hover {
        background-color: #897DCF;
    }
"""

Button_Disabled_Style = """
    QPushButton {
        background-color: #4D5259; 
        color : #D4D7DC;
        border-radius : 7px;
    }
"""


class Button(QPushButton):
    valid = True

    def __init__(self, parent, size):
        super(Button, self).__init__(parent)
        self.setStyleSheet(Button_Style)
        if size == "Small":
            self.resize(112, 45)
            font = (QFont("Karla", 13))
        elif size == "Medium":
            self.resize(143, 64)
            font = (QFont("Karla", 16))
        elif size == "Large":
            self.resize(181, 72)
            font = (QFont("Karla", 20))
        else:
            font = (QFont("Karla", 16))
            self.resize(143, 64)
        font.setWeight(700)
        self.setFont(font)
        self.setCursor(Qt.CursorShape.PointingHandCursor)

    def setEnabled(self):
        self.valid = True
        self.setStyleSheet(Button_Style)

    def setDisabled(self):
        self.Valid = False
        self.setStyleSheet(Button_Disabled_Style)
