""" Notification Dropdown """

from PyQt6.QtGui import QFont
from PyQt6.QtWidgets import QWidget

from src.components.fields.Dropdown import Dropdown

# Global Variabel Font
font = QFont("Karla", 11)
font.setWeight(600)


class NotificationDropdown(QWidget):
    arr = ["Today", "This Week", "This Month"]

    def __init__(self, parent):
        super(NotificationDropdown, self).__init__(parent)

        # Top Left Drop-down
        self.dropdown = Dropdown(self)
        self.dropdown.resize(180, 50)
        self.dropdown.setPlaceholderText(self.arr[0])
        self.dropdown.setFont(font)
        for i in range(len(self.arr)):
            self.dropdown.addItem(self.arr[i])
