""" Inventory Entry """

from PyQt6.QtCore import Qt
from PyQt6.QtGui import QFont
from PyQt6.QtWidgets import QWidget, QLabel, QSizePolicy, QHBoxLayout

# Global Variabel Font
font = QFont("Karla", 11)
font.setWeight(600)


class InventoryEntry(QWidget):
    k = ""
    v = ""

    def __init__(self, parent, key, value):
        super(InventoryEntry, self).__init__(parent)
        self.k = key;
        self.v = str(value)
        self.setSizePolicy(QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Fixed)

        layout = QHBoxLayout()
        layout.setContentsMargins(12, 0, 12, 0)

        self.key = QLabel()
        self.key.setStyleSheet("color: white")
        self.key.setText(key)
        self.key.setFont(font)
        layout.addWidget(self.key)

        self.value = QLabel()
        self.value.setAlignment(Qt.AlignmentFlag.AlignRight)
        self.value.setStyleSheet("color: white;")
        self.value.setText(str(value))
        self.value.setFont(font)
        layout.addWidget(self.value)

        self.setLayout(layout)

    def getKey(self):
        return self.k

    def getValue(self):
        return self.v

    def setValue(self, val):
        self.v = val
        self.value.setText(str(val))
