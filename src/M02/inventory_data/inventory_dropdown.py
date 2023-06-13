""" Inventory Dropdown """

from PyQt6.QtGui import QFont
from src.components.fields.Dropdown import Dropdown
from src.M02.inventory_manager import *

im = InventoryManager()

# Global Variabel Font
font = QFont("Karla", 11)
font.setWeight(600)


class InventoryDropdown(Dropdown):
    arr = ["All Categories"]
    for i in im.getCategoriesArray():
        arr.append(i)

    def __init__(self, parent):
        super(InventoryDropdown, self).__init__(parent)

        # Top Left Drop-down
        self.setPlaceholderText(self.arr[0])
        self.setFont(font)
        for i in range(len(self.arr)):
            self.addItem(self.arr[i])
