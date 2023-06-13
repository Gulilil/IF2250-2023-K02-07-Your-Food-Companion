""" Consumed Foods Tab """

from PyQt6.QtGui import QFont
from PyQt6.QtWidgets import QWidget, QVBoxLayout, QHBoxLayout

from src.M02.inventory_data.inventory_dropdown import InventoryDropdown
from src.M02.inventory_data.inventory_searchbar import InventorySearchbar
from src.components.pagination.Pagination import Pagination
from src.components.table.Table import Table
from src.M02.inventory_manager import *

im = InventoryManager()


# Global Variabel Font
font = QFont("Karla", 11)
font.setWeight(600)
addItemFont = QFont("Karla", 25)
addItemFont.setWeight(600)


class ConsumedFoodTab(QWidget):
    currentCategory = "All Categories"
    def __init__ (self):
        super(ConsumedFoodTab, self).__init__()

        self.layer = QWidget(self)
        self.layer.setStyleSheet("background-color: #2F3136")
        self.layer.setContentsMargins(0, 0, 0, 0)
        self.layerLayout = QVBoxLayout()
        self.layerLayout.setContentsMargins(0, 0, 0, 0)
        self.layerLayout.addWidget(self.layer)
        self.setLayout(self.layerLayout)

        self.contentLayout = QVBoxLayout()
        self.contentLayout.setContentsMargins(32, 32, 32, 32)
        self.layer.setLayout(self.contentLayout)

        # Set initial categories
        self.categories = "All Categories"

        self.headerLayout = QHBoxLayout()
        self.contentLayout.addLayout(self.headerLayout)

        # Adding dropdown
        self.dropdown = InventoryDropdown(self.layer)
        self.headerLayout.addWidget(self.dropdown)
        self.headerLayout.addStretch()
        self.dropdown.currentTextChanged.connect(lambda: self.changeCategory(self.dropdown.currentText()))

        # Top Right Search Bar
        self.searchbar = InventorySearchbar(self.layer)
        self.headerLayout.addWidget(self.searchbar)
        self.searchbar.getButtonSearchbar().clicked.connect(lambda: self.changeSearch())

        # # Table data
        self.header = im.Consumed_Food_Data_Header
        self.data = im.getConsumedFoodData(None)
        self.setTables(self.data)

    def setTables(self, d):
        nRows = 6
        pageAmount = ((len(d) - 1) // nRows) + 1

        table_pagination = Pagination(self.layer, pageAmount)
        self.table = Table(data=d, pagination=table_pagination, rowsPerPage=nRows, headers=self.header,
                           useCheckbox=True)

        self.contentLayout.addWidget(self.table)
        self.contentLayout.addWidget(table_pagination)

    def updateTables(self, d):
        prevTable = self.contentLayout.itemAt(1).widget()
        prevTable.deleteLater()
        prevPagination = self.contentLayout.itemAt(2).widget()
        prevPagination.deleteLater()
        self.setTables(d)

    
    def getWidget(self):
        return self.layer

    def getCategories(self):
        return self.categories

    def getButtonSearchbar(self):
        return self.searchbar.getButtonSearchbar()

    def getWidget(self):
        return self.layer

    def changeCategory(self, category):
        self.currentCategory = category
        if category == "All Categories":
          self.data = im.getConsumedFoodData(None)
        else :
          self.data = im.getConsumedFoodData(category)
        self.updateTables(self.data)

    def changeSearch(self):
        category = self.currentCategory
        content = self.searchbar.getContent()
        if (category == "All Categories"):
            temp = im.getConsumedFoodData(None)
        else:
            temp = im.getConsumedFoodData(category)
        self.data = []
        for i in temp:
            if (content in i[0]):
                self.data.append(i)
        self.updateTables(self.data)
