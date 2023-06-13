""" Food Inventory Module """

from PyQt6.QtWidgets import QWidget, QVBoxLayout, QHBoxLayout, QSizePolicy
from PyQt6.QtCore import Qt

from src.M02.inventory_data.inventory_container import InventoryContainer
from src.M02.inventory_table.inventory_description import InventoryDescription


class FoodInventory(QWidget):
    def __init__(self):
        super(FoodInventory, self).__init__()

        # Making widget item for the class
        self.layer = QWidget(self)
        # self.layer.resize(screenW, screenH)
        self.layer.setStyleSheet("background-color: #36393F;")
        # self.layer.move(10, 10)

        # Every components in this page, please use "self.layer" as its parent
        # Because "self.layer" is the Widget that will be inserted into Stack in Main.py

        self.desc_table = InventoryDescription(self.layer)
        self.data_table = InventoryContainer(self.layer)


        contentLayout = QHBoxLayout()
        self.desc_table = InventoryDescription(self.layer)
        contentLayout.addWidget(self.desc_table, alignment=Qt.AlignmentFlag.AlignTop)
        self.data_table = InventoryContainer(self.layer)
        contentLayout.addWidget(self.data_table, alignment=Qt.AlignmentFlag.AlignTop)

        self.layer.setLayout(contentLayout)

        layerContainer = QVBoxLayout()
        layerContainer.addWidget(self.layer)
        self.setLayout(layerContainer)

    def getWidget(self):
        return self.layer
    
    def getDescTable(self):
        return self.desc_table
