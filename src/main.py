""" Main Program """

import sys

from PyQt6.QtWidgets import QApplication, QStackedWidget, QVBoxLayout, QHBoxLayout, QWidget, QMainWindow, QSizePolicy
from PyQt6.QtCore import Qt
from src.M01.Dashboard import Dashboard
from src.M02.FoodInventory import FoodInventory
from src.M03.ShoppingList import ShoppingList
from src.M04.ShoppingHistory import ShoppingHistory
from src.M05.Report import Report
from src.components.wrappers.Sidebar import Sidebar
from src.components.wrappers.Topbar import Topbar
from src.notification.notification import Notification


class MainWindow(QMainWindow):
    def __init__(self):
        super(MainWindow, self).__init__()
        self.setWindowTitle("Your Food Companion")
        # screenW = app.primaryScreen().size().width()
        # screenH = app.primaryScreen().size().height()
        # self.resize(screenW, screenH)
        self.setStyleSheet("background-color: black")
        self.setWindowState(Qt.WindowState.WindowMaximized)

        # Constructing Sidebar
        self.sidebar = Sidebar(self)
        self.sidebar.setSizePolicy(QSizePolicy.Policy.Fixed, QSizePolicy.Policy.Expanding)
        self.sidebar.getButtonDashboard().clicked.connect(lambda: self.changePage(0))
        self.sidebar.getButtonInventory().clicked.connect(lambda: self.changePage(1))
        self.sidebar.getButtonShoppingList().clicked.connect(lambda: self.changePage(2))
        self.sidebar.getButtonShoppingHistory().clicked.connect(lambda: self.changePage(3))
        self.sidebar.getButtonReport().clicked.connect(lambda: self.changePage(4))
        self.sidebar.getButtonQuit().clicked.connect(lambda: self.close())

        # Constructing Topbar
        self.contentLayout = QVBoxLayout()
        self.topbar = Topbar(self)
        self.topbar.getButtonNotification().clicked.connect(lambda: self.changePage(5))
        self.topbar.setSizePolicy(QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Fixed)
        self.contentLayout.addWidget(self.topbar)

        # Making stackedWidget for page changing
        self.stack = QStackedWidget()
        self.stack.setContentsMargins(0,0,0,0)
        self.contentLayout.addWidget(self.stack)

        # Setting up pages
        self.setPage1()
        self.setPage2()
        self.setPage3()
        self.setPage4()
        self.setPage5()
        self.setPageNotif()

        # HBox Layout
        self.widget = QWidget()
        self.hbox = QHBoxLayout(self)
        self.hbox.addWidget(self.sidebar.getWidget())
        self.hbox.addLayout(self.contentLayout)
        self.widget.setLayout(self.hbox)
        self.hbox.setContentsMargins(0, 0, 0, 0)
        self.hbox.setSpacing(0)
        self.setCentralWidget(self.widget)

        # Set 0 as Current Index
        self.stack.setCurrentIndex(0)

        # Setup dashboard
        self.page1.get_hero_button().clicked.connect(lambda: self.sidebar.getButtonInventory().click())
        see_all1, see_all2 = self.page1.get_see_all_button()
        see_all1.clicked.connect(lambda: self.sidebar.getButtonInventory().click())
        see_all2.clicked.connect(lambda: self.sidebar.getButtonReport().click())

        # Controller testing
        # c = Controller()
        # for i in c.get_eaten_food():
        #     print(i)

    def changePage(self, i):
        self.topbar.setText(self.topbar.arr[i])
        if (i == 1):
            self.page2.getDescTable().updateDescription()
        self.stack.setCurrentIndex(i)

    def setPage1(self):
        self.page1 = Dashboard()
        self.page1.setFoodItemCard()
        widget = self.page1.getWidget()  # Getting widget item of the pages
        self.stack.addWidget(widget)  # Adding widget item to stack (stack CANNOT contain classes)

    def setPage2(self):
        self.page2 = FoodInventory()
        widget = self.page2.getWidget()  # Getting widget item of the pages
        self.stack.addWidget(widget)  # Adding widget item to stack (stack CANNOT contain classes)

    def setPage3(self):
        self.page3 = ShoppingList()
        widget = self.page3.getWidget()  # Getting widget item of the pages
        self.stack.addWidget(widget)  # Adding widget item to stack (stack CANNOT contain classes)

    def setPage4(self):
        self.page4 = ShoppingHistory()
        widget = self.page4.getWidget()  # Getting widget item of the pages
        self.stack.addWidget(widget)  # Adding widget item to stack (stack CANNOT contain classes)

    def setPage5(self):
        self.page5 = Report()
        self.stack.addWidget(self.page5)                        # Adding widget item to stack (stack CANNOT contain classes)

    def setPageNotif(self):
        self.pageNotif = Notification()
        widget = self.pageNotif.getWidget()  # Getting widget item of the pages
        self.stack.addWidget(widget)  # Adding widget item to stack (stack CANNOT contain classes)


if __name__ == '__main__':
    app = QApplication(sys.argv)
    window = MainWindow()
    window.showMaximized()
    sys.exit(app.exec())
