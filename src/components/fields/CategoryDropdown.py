""" Inventory Dropdown """

from PyQt6 import QtGui
from PyQt6.QtGui import QFont
from PyQt6.QtWidgets import QWidget

from src.components.fields.Dropdown import Dropdown

# Global Variabel Font
font = QFont("Karla", 11)
font.setWeight(600)


class CategoryDropdown(QWidget):
    def __init__(self, parent):
        super(CategoryDropdown, self).__init__(parent)

        # Top Left Drop-down
        self.dropdown = Dropdown(self)
        self.dropdown.resize(180, 50)
        self.dropdown.setFont(font)

    def addChoice(self, name):
        self.dropdown.addItem(QtGui.QIcon("./assets/icons/category.png"), name)

    def getObject(self):
        return self.dropdown
