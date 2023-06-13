""" Inventory Container """

from PyQt6.QtWidgets import QWidget, QStackedWidget, QVBoxLayout, QSizePolicy

from src.M02.inventory_data.data_tab.all_food.all_food_tab import AllFoodTab
from src.M02.inventory_data.data_tab.consumed.consumed_food_tab import ConsumedFoodTab
from src.M02.inventory_data.data_tab.expired.expired_food_tab import ExpiredFoodTab
from src.M02.inventory_data.data_tab.good.good_food_tab import GoodFoodTab
from src.M02.inventory_data.data_tab.stale.stale_food_tab import StaleFoodTab
from src.M02.inventory_data.inventory_taskbar import Taskbar
from src.M02.inventory_manager import InventoryManager

im = InventoryManager()

class InventoryContainer(QWidget):
    def __init__(self, parent):
        super(InventoryContainer, self).__init__(parent)

        # Making layer
        self.layer = QWidget(self)
        self.layer.setStyleSheet("border-bottom-left-radius: 10px; border-bottom-right-radius: 10px; margin: 0")
        self.layer.setContentsMargins(0, 0, 0, 0)
        self.layerContainer = QVBoxLayout()
        self.layerContainer.addWidget(self.layer)
        self.layerContainer.setContentsMargins(0, 0, 0, 0)
        self.layerContainer.setSpacing(0)
        self.setLayout(self.layerContainer)

        self.contentContainer = QVBoxLayout()
        self.contentContainer.setContentsMargins(0, 0, 0, 0)
        self.contentContainer.setSpacing(0)
        self.layer.setLayout(self.contentContainer)

        self.taskbar = Taskbar(self)
        self.taskbar.setContentsMargins(0, 0, 0, 0)
        self.taskbar.getButtonAllFood().clicked.connect(lambda: self.changePage(0))
        self.taskbar.getButtonGoodFood().clicked.connect(lambda: self.changePage(1))
        self.taskbar.getButtonStaleFood().clicked.connect(lambda: self.changePage(2))
        self.taskbar.getButtonExpiredFood().clicked.connect(lambda: self.changePage(3))
        self.taskbar.getButtonConsumedFood().clicked.connect(lambda: self.changePage(4))
        self.contentContainer.addWidget(self.taskbar)

        # # Making stackedWidget for page changing
        self.stack = QStackedWidget(self.layer)
        self.stack.setContentsMargins(0, 0, 0, 0)
        self.stack.setSizePolicy(QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Expanding)

        # # Setting up tabs
        self.setPage1()
        self.setPage2()
        self.setPage3()
        self.setPage4()
        self.setPage5()
        self.contentContainer.addWidget(self.stack)

        # # Set 0 as First Page
        self.lastIndex = 0
        self.currentIndex = 0
        self.stack.setCurrentIndex(0)

    def changePage(self, n):
        self.lastIndex = self.currentIndex
        self.currentIndex = n
        if (n == 0):
            data = im.getStoredFoodData(None)
            self.page1.updateTables(data)
        elif(n == 1):
            data = im.getGoodFoodData(None)
            self.page2.updateTables(data)
        elif(n == 2):
            data = im.getStaleFoodData(None)
            self.page3.updateTables(data)
        elif(n == 3):
            data = im.getExpiredFoodData(None)
            self.page4.updateTables(data)
        elif(n == 4):
            data = im.getConsumedFoodData(None)
            self.page5.updateTables(data)
        self.stack.setCurrentIndex(n)

    def setPage1(self):
        self.page1 = AllFoodTab()
        self.page1.setContentsMargins(0,0,0,0)
        self.page1.setSizePolicy(QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Expanding)
        self.stack.addWidget(self.page1)

    def setPage2(self):
        self.page2 = GoodFoodTab()
        self.page2.setContentsMargins(0,0,0,0)
        self.page2.setSizePolicy(QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Expanding)
        self.stack.addWidget(self.page2)

    def setPage3(self):
        self.page3 = StaleFoodTab()
        self.page3.setContentsMargins(0,0,0,0)
        self.page3.setSizePolicy(QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Expanding)
        self.stack.addWidget(self.page3)

    def setPage4(self):
        self.page4 = ExpiredFoodTab()
        self.page4.setContentsMargins(0,0,0,0)
        self.page4.setSizePolicy(QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Expanding)
        self.stack.addWidget(self.page4)

    def setPage5(self):
        self.page5 = ConsumedFoodTab()
        self.page5.setContentsMargins(0,0,0,0)
        self.page5.setSizePolicy(QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Expanding)
        self.stack.addWidget(self.page5)

    def getAllFoodTab(self):
        return self.page1

    def getLastIndex(self):
        return self.lastIndex

    def getCurrentIndex(self):
        return self.currentIndex
