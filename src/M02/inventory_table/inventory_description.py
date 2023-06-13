""" Inventory Description """

from PyQt6.QtCore import Qt
from PyQt6.QtGui import QFont
from PyQt6.QtWidgets import QWidget, QLabel, QPushButton, QScrollArea, QVBoxLayout, QHBoxLayout, QSizePolicy as qp

from src.M02.inventory_manager import *
from src.M02.inventory_table.inventory_entry import InventoryEntry
from src.M02.inventory_table.inventory_photo import InventoryPhoto

# Global Variabel Font
font = QFont("Karla", 11)
font.setWeight(600)

im = InventoryManager()

class InventoryDescription(QWidget):
    width = 0
    height = 0
    foodCount = len(im.getStoredFoodData(None))
    expiredFoodCount = len(im.getExpiredFoodData(None))
    consumedFoodCount = len(im.getConsumedFoodData(None))
    totalValue = im.getTotalValueInventory()
    foodWasteValue = im.getTotalWasteExpired()
    categoriesCount = len(im.getCategoriesArray())
    arrCategories = im.getCategoriesArray()
    arrCategoriesCount = im.getFoodCountCategory(arrCategories)

    def __init__(self, parent: QWidget = None):
        super(InventoryDescription, self).__init__(parent)

        self.setMaximumWidth(360)

        # Layer
        self.layer = QWidget(self)
        self.layer.setStyleSheet("background-color: #4D5259;  border-radius: 10px;")
        self.layerLayout = QVBoxLayout()
        self.layerLayout.addWidget(self.layer)
        self.layerLayout.setContentsMargins(8, 8, 8, 8)
        self.setLayout(self.layerLayout)

        self.contentLayout = QVBoxLayout()
        self.layer.setLayout(self.contentLayout)
        self.contentLayout.setSpacing(48)

        # # Food profile image
        self.food_image = InventoryPhoto(self.layer)
        self.contentLayout.addWidget(self.food_image, alignment=Qt.AlignmentFlag.AlignHCenter)

        # List1
        self.container1 = QWidget(self.layer)
        self.containerOneLayout = QVBoxLayout()
        self.container1.setLayout(self.containerOneLayout)

        self.titleOneLayout = QHBoxLayout()

        self.icon1 = QPushButton(self.container1)
        self.icon1.setSizePolicy(qp.Policy.Fixed, qp.Policy.Fixed)
        self.icon1.setStyleSheet("background: transparent; image: url(./assets/icons/inv_count.png)")
        self.containerOneLayout.addWidget(self.icon1)
        self.titleOneLayout.addWidget(self.icon1)

        self.title1 = QLabel(self.container1)
        self.icon1.setSizePolicy(qp.Policy.Fixed, qp.Policy.Fixed)
        self.title1.setText("Counts")
        self.title1.setStyleSheet("color: white")
        self.title1.setFont(font)
        self.titleOneLayout.addWidget(self.title1)
        self.titleOneLayout.setSpacing(12)

        self.containerOneLayout.addLayout(self.titleOneLayout)

        self.entryOneLayout = QVBoxLayout()
        self.foodCountEntry = InventoryEntry(self.container1, "Food In Inventory", self.foodCount)
        self.entryOneLayout.addWidget(self.foodCountEntry)
        self.expiredFoodCountEntry = InventoryEntry(self.container1, "Expired Food", self.expiredFoodCount)
        self.entryOneLayout.addWidget(self.expiredFoodCountEntry)
        self.consumedFoodCounttEntry = InventoryEntry(self.container1, "Foods Consumed", self.consumedFoodCount)
        self.entryOneLayout.addWidget(self.consumedFoodCounttEntry)
        self.entryOneLayout.setSpacing(16)
        self.containerOneLayout.addLayout(self.entryOneLayout)

        self.containerOneLayout.setSpacing(24)
        self.contentLayout.addWidget(self.container1)

        # List2
        self.container2 = QWidget(self.layer)
        self.containerTwoLayout = QVBoxLayout()
        self.container2.setLayout(self.containerTwoLayout)

        self.titleTwoLayout = QHBoxLayout()

        self.icon2 = QPushButton(self.container2)
        self.icon2.setSizePolicy(qp.Policy.Fixed, qp.Policy.Fixed)
        self.icon2.setStyleSheet("background: transparent; image: url(./assets/icons/inv_monetary.png)")
        self.titleTwoLayout.addWidget(self.icon2)

        self.title2 = QLabel(self.container2)
        self.title2.setText("Monetary")
        self.title2.setStyleSheet("color: white")
        self.title2.setFont(font)
        self.titleTwoLayout.addWidget(self.title2)
        self.titleTwoLayout.setSpacing(12)

        self.containerTwoLayout.addLayout(self.titleTwoLayout)

        self.entryTwoLayout = QVBoxLayout()
        self.totalValueEntry = InventoryEntry(self.container2, "Total Value", self.totalValue)
        self.entryTwoLayout.addWidget(self.totalValueEntry)
        self.foodWasteValueEntry = InventoryEntry(self.container2, "Total Food Waste", self.foodWasteValue * -1)
        self.entryTwoLayout.addWidget(self.foodWasteValueEntry)
        self.entryTwoLayout.setSpacing(16)
        self.containerTwoLayout.addLayout(self.entryTwoLayout)

        self.containerTwoLayout.setSpacing(24)
        self.contentLayout.addWidget(self.container2)

        # # List3
        self.container3 = QWidget(self.layer)
        self.containerThreeLayout = QVBoxLayout()
        self.container3.setLayout(self.containerThreeLayout)

        self.titleThreeLayout = QHBoxLayout()

        self.icon3 = QPushButton(self.container3)
        self.icon3.setStyleSheet("background: transparent; image: url(./assets/icons/inv_categories.png)")
        self.icon3.setSizePolicy(qp.Policy.Fixed, qp.Policy.Fixed)
        self.titleThreeLayout.addWidget(self.icon3)
        self.title3 = QLabel(self.container3)
        self.title3.setText("Categories")
        self.title3.setStyleSheet("color: white")
        self.title3.setFont(font)
        self.titleThreeLayout.addWidget(self.title3)
        self.titleThreeLayout.setSpacing(12)

        self.containerThreeLayout.addLayout(self.titleThreeLayout)

        self.scrollable = QScrollArea(self.container3)
        self.scrollable.setStyleSheet("margin-right: 12px; color: white")
        self.scrollable.setFont(font)
        self.vbox = QVBoxLayout()
        self.categoriesContainer = QWidget()
        for i in range(len(self.arrCategories)):
            layout = QHBoxLayout()
            key = QLabel(self.arrCategories[i])
            val = QLabel(str(self.arrCategoriesCount[i]))
            key.setFont(font)
            val.setFont(font)
            layout.addWidget(key, alignment=Qt.AlignmentFlag.AlignLeft)
            layout.addWidget(val, alignment=Qt.AlignmentFlag.AlignRight)
            self.vbox.addLayout(layout)
        self.categoriesContainer.setLayout(self.vbox)
        self.containerThreeLayout.addWidget(self.categoriesContainer)
        self.scrollable.setVerticalScrollBarPolicy(Qt.ScrollBarPolicy.ScrollBarAsNeeded)
        self.scrollable.setHorizontalScrollBarPolicy(Qt.ScrollBarPolicy.ScrollBarAlwaysOff)
        self.scrollable.setWidgetResizable(True)
        self.scrollable.setWidget(self.categoriesContainer)
        self.containerThreeLayout.addWidget(self.scrollable)

        self.categoriesCountEntry = InventoryEntry(self.container3, "Total Categories", self.categoriesCount)
        self.containerThreeLayout.addWidget(self.categoriesCountEntry)
        self.containerThreeLayout.addStretch()
        self.containerThreeLayout.setSpacing(24)
        self.contentLayout.addWidget(self.container3)
        self.contentLayout.addStretch()

        self.setCategoriesCount(len(self.arrCategories))
        for i in range(self.categoriesCount):
          self.setFoodCountWithCategories(self.arrCategories[i], self.arrCategoriesCount[i])
        
    def updateDescription(self):
        self.setFoodCount(len(im.getStoredFoodData(None)))
        self.setExpiredFoodCount(len(im.getExpiredFoodData(None)))
        self.setConsumedFoodCount(len(im.getConsumedFoodData(None)))
        self.setTotalValue(im.getTotalValueInventory())
        self.setFoodWasteValue(im.getTotalWasteExpired())
        self.setCategoriesCount( len(im.getCategoriesArray()))
        self.arrCategories = im.getCategoriesArray()
        self.arrCategoriesCount = im.getFoodCountCategory(self.arrCategories)

        for i in range(self.categoriesCount):
          self.setFoodCountWithCategories(self.arrCategories[i], self.arrCategoriesCount[i])

    def getFoodInventoryCount(self):
        return self.foodCount

    def getExpiredFoodCount(self):
        return self.expiredFoodCount

    def getConsumedFoodCount(self):
        return self.consumedFoodCount

    def getTotalValue(self):
        return self.totalValue

    def getFoodWasteValue(self):
        return self.totalValue

    def getCategories(self):
        return self.categoriesCount

    def setFoodCount(self, n):
        self.foodCount = n
        self.foodCountEntry.setValue(n)

    def setExpiredFoodCount(self, n):
        self.expiredFoodCount = n
        self.expiredFoodCountEntry.setValue(n)

    def setConsumedFoodCount(self, n):
        self.consumedFoodCount = n
        self.consumedFoodCounttEntry.setValue(n)

    def setTotalValue(self, n):
        self.totalValue = n
        self.totalValueEntry.setValue(n)

    def setFoodWasteValue(self, n):
        self.foodWasteValue = n
        self.foodWasteValueEntry.setValue(n)

    def setFoodCountWithCategories(self, categories, n):
        if (categories in self.arrCategories):
            for i in range(len(self.arrCategories)):
                if (self.arrCategories[i] == categories):
                    self.arrCategoriesCount[i] = n
                    hboxLayout = self.vbox.itemAt(i).layout()
                    item = hboxLayout.itemAt(1).widget()
                    item.setText(str(n))
                
                    

    def setCategoriesCount(self, n):
        self.categoriesCount = n
        self.categoriesCountEntry.setValue(n)
