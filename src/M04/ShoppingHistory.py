""" Shopping History Module """

from PyQt6.QtWidgets import QVBoxLayout
from PyQt6.QtWidgets import QWidget

from src.M04.shopping_history_container import ShoppingHistoryContainer

SHOPPING_HISTORY_LAYER_STYLE = """
    background-color: #36393F;
    margin: 0;
"""


class ShoppingHistory(QWidget):
    def __init__(self):
        super(ShoppingHistory, self).__init__()

        # Making widget item for the class
        self.layer = QWidget(self)
        self.layer.setStyleSheet(SHOPPING_HISTORY_LAYER_STYLE)

        # Every component in this page, please use "self.layer" as its parent
        # Because "self.layer" is the Widget that will be inserted into Stack in Main.py

        self.shopping_history_container = ShoppingHistoryContainer(self.layer)

        # Layer layout
        self.layer_layout = QVBoxLayout()
        self.layer_layout.addWidget(self.layer)
        self.setLayout(self.layer_layout)

        # Content layout
        self.content_layout = QVBoxLayout()
        self.content_layout.addWidget(self.shopping_history_container)
        self.layer.setLayout(self.content_layout)

    def getWidget(self):
        return self.layer
