""" Food Inventory Module """

import re

from PyQt6.QtWidgets import QWidget

from src.M03.slistitem import ShoppingListItem
from src.M03.slisttaskbar import ShoppingListTaskbar
from src.components.buttons.ShoppingAddItem import ShoppingAddItemButton
from src.components.fields.CategoryDropdown import CategoryDropdown
from src.components.fields.Searchbar import Searchbar
from src.components.form.Form import Forms
from src.components.pagination.Pagination import Pagination
from src.controller.controller import Controller
from datetime import date

FirstTaskbarButton = "background-color: #2F3136;border-radius:10px;border-top-left-radius:0"
TaskbarButton = "background-color: #2F3136;border-radius:10px"


class ShoppingList(QWidget):
    width = 1200
    height = 800

    def __init__(self):
        super(ShoppingList, self).__init__()
        self.resize(self.width, self.height)

        # Making widget item for the class
        self.layer = QWidget(self)
        self.layer.resize(self.width, self.height)
        self.layer.setStyleSheet("background-color: #36393F")

        # Every components in this page, please use "self.layer" as its parent
        # Because "self.layer" is the Widget that will be inserted into Stack in Main.py
        self.controller = Controller()

        self.taskbar = ShoppingListTaskbar(self.layer, self.width)
        self.taskbar.getButtonAllFood().clicked.connect(lambda: self.changePage(0))
        self.taskbar.getButtonHighPriority().clicked.connect(lambda: self.changePage(1))
        self.taskbar.getButtonMediumPriority().clicked.connect(lambda: self.changePage(2))
        self.taskbar.getButtonLowPriority().clicked.connect(lambda: self.changePage(3))
        self.taskbar.move(50, 50)
        tempy = self.taskbar.getSize()[1]

        self.container = QWidget(self.layer)
        self.container.resize(self.layer.width() - 100, self.layer.height() - 100 - tempy)
        self.container.setStyleSheet(FirstTaskbarButton)
        self.container.move(50, 50 + tempy)

        self.searchbar = Searchbar(self.container)
        self.searchbar.move(self.container.width() - 70 - self.searchbar.width(), 30)
        self.searchbar.getButtonSearchbar().clicked.connect(lambda: self.search())

        self.additembutton = ShoppingAddItemButton(self.container)
        self.additembutton.move(self.container.width() - 70, 30)
        self.additembutton.getValid().stateChanged.connect(self.processNewItem)

        self.data = self.controller.get_grocery_food()

        self.indexButton = 0

        self.item = []

        itemheight = (self.container.height() - 250) / 3
        itemwidth = (self.container.width() - 150) / 5

        i = 0
        for i in range(15):
            self.item.append(ShoppingListItem(self.container, itemheight, itemwidth, "", "", ""))
            self.item[i].move(int(15 + 20 * ((i % 5) + 1) + itemwidth * (i % 5)),
                              int(120 + (20 + itemheight) * (i // 5)))
            i = i + 1
            if (i == 15):
                break

        self.item[0].getChange().stateChanged.connect(lambda: self.processChange(0))
        self.item[1].getChange().stateChanged.connect(lambda: self.processChange(1))
        self.item[2].getChange().stateChanged.connect(lambda: self.processChange(2))
        self.item[3].getChange().stateChanged.connect(lambda: self.processChange(3))
        self.item[4].getChange().stateChanged.connect(lambda: self.processChange(4))
        self.item[5].getChange().stateChanged.connect(lambda: self.processChange(5))
        self.item[6].getChange().stateChanged.connect(lambda: self.processChange(6))
        self.item[7].getChange().stateChanged.connect(lambda: self.processChange(7))
        self.item[8].getChange().stateChanged.connect(lambda: self.processChange(8))
        self.item[9].getChange().stateChanged.connect(lambda: self.processChange(9))
        self.item[10].getChange().stateChanged.connect(lambda: self.processChange(10))
        self.item[11].getChange().stateChanged.connect(lambda: self.processChange(11))
        self.item[12].getChange().stateChanged.connect(lambda: self.processChange(12))
        self.item[13].getChange().stateChanged.connect(lambda: self.processChange(13))
        self.item[14].getChange().stateChanged.connect(lambda: self.processChange(14))

        self.page = Pagination(self.container, 1)
        self.page.move(self.container.width() - self.page.width() + 50,
                       self.container.height() - self.page.height() - 30)
        self.page.adjustSize()
        self.page.getSignal().stateChanged.connect(lambda: self.nextItems())

        self.category = CategoryDropdown(self.container)
        self.category.move(30, 30)
        self.category.addChoice("All Category")
        temp = self.controller.get_category()
        for row in temp:
            self.category.addChoice(row[0])
        self.category.getObject().currentTextChanged.connect(
            lambda: self.changeCategory(self.category.getObject().currentText()))

        self.changePage(0)
        self.currentPrio = "All"
        self.currentCategory = "All Category"
        self.form = Forms()
        self.pickfoodid = -1
        self.icount = 0
        self.pcount = 0

    def getWidget(self):
        return self.layer

    def toint(self, i):
        temp = i
        return temp

    def changePage(self, index):
        self.searchbar.clear()
        self.indexButton = index
        self.currentCategory = "All Category"
        self.category.getObject().setCurrentIndex(0)
        if (index == 0):
            self.currentPrio = "All"
            self.container.setStyleSheet(FirstTaskbarButton)
            self.data = self.controller.get_grocery_food()
        else:
            self.container.setStyleSheet(TaskbarButton)
            if (index == 1):
                self.data = self.controller.get_grocery_food_prio("High")
                self.currentPrio = "High"
            elif (index == 2):
                self.data = self.controller.get_grocery_food_prio("Medium")
                self.currentPrio = "Medium"
            elif (index == 3):
                self.data = self.controller.get_grocery_food_prio("Low")
                self.currentPrio = "Low"
        self.updatePage()

    def changeCategory(self, cat):
        self.searchbar.clear()
        self.currentCategory = cat
        if (cat == "All Category" and self.currentPrio == "All"):
            self.data = self.controller.get_grocery_food()
        elif (cat != "All Category" and self.currentPrio == "All"):
            self.data = self.controller.get_grocery_food_cat(cat)
        elif (cat == "All Category" and self.currentPrio != "All"):
            self.data = self.controller.get_grocery_food_prio(self.currentPrio)
        else:
            self.data = self.controller.get_grocery_food_prio_cat(self.currentPrio, cat)
        self.updatePage()

    def updatePage(self):
        i = 0
        tempdata = []
        for row in self.data:
            items = []
            for item in row:
                items.append(item)
            tempdata.append(items)

        self.data = tempdata

        for row in self.data:
            self.item[i].show()
            self.item[i].resetText(row[2], row[1], row[3])
            i = i + 1
            if (i == 15):
                break
        while (i < 15):
            self.item[i].hide()
            i = i + 1

        self.icount = len(self.data)
        self.pcount = ((len(self.data)-1) // 15) + 1
        self.page.hide()
        self.page = Pagination(self.container, self.pcount)
        self.page.show()
        self.page.move(self.container.width() - self.page.width() + 50,
                       self.container.height() - self.page.height() - 30)
        self.page.getSignal().stateChanged.connect(lambda: self.nextItems())
        self.page.adjustSize()

    def nextItems(self):
        page = self.page.getCurrentPage()
        i = 0
        lendata = len(self.data)
        while i < 15:
            self.item[i].show()
            self.item[i].resetText(self.data[(page - 1) * 15 + i][2], self.data[(page - 1) * 15 + i][1],
                                   self.data[(page - 1) * 15 + i][3])
            i = i + 1
            if ((page - 1) * 15 + i == lendata):
                break
        while (i < 15):
            self.item[i].hide()
            i = i + 1

    def search(self):
        if (self.currentCategory == "All Category" and self.currentPrio == "All"):
            self.data = self.controller.get_grocery_food_name(self.searchbar.getContent())
        elif (self.currentCategory != "All Category" and self.currentPrio == "All"):
            self.data = self.controller.get_grocery_food_cat_name(cat, self.searchbar.getContent())
        elif (self.currentCategory == "All Category" and self.currentPrio != "All"):
            self.data = self.controller.get_grocery_food_prio_name(self.currentPrio, self.searchbar.getContent())
        else:
            self.data = self.controller.get_grocery_food_prio_cat_name(self.currentPrio, cat,
                                                                       self.searchbar.getContent())
        self.updatePage()

    def processNewItem(self):
        tempdata = self.additembutton.getData()
        currentfood = self.controller.get_food()

        valid = False
        foodid = -1
        for row in currentfood:
            if row[1] == tempdata[0][1] and row[2] == tempdata[1][1]:
                valid = True
                foodid = row[0]
                break

        if valid:
            currentfood = self.controller.get_grocery_food()
            currentfood = self.controller.get_food()
            for row in currentfood:
                if row[0] == foodid:
                    self.controller.delete_grocery_food(foodid)
                    break
            self.controller.insert_grocery_food(foodid, tempdata[2][1])
        else:
            max = 0
            currentfood = self.controller.get_food()
            for row in currentfood:
                if row[0] > max:
                    max = row[0]
            self.controller.insert_food(max + 1, tempdata[0][1], tempdata[1][1])
            self.controller.insert_grocery_food(max + 1, tempdata[2][1])
        self.currentCategory == "All Category"
        self.currentPrio == "All"
        self.taskbar.changeIndex(0)
        self.changePage(0)

    def processChange(self, idx):
        status = self.item[idx].getStatus()
        allfood = self.controller.get_food()
        self.pickfoodid = -1
        for row in allfood:
            if row[1] == self.item[idx].getName() and row[2] == self.item[idx].getCategory():
                self.pickfoodid = row[0]
                break
        if status == "delete":
            self.controller.delete_grocery_food(self.pickfoodid)
            self.currentCategory == "All Category"
            self.currentPrio == "All"
            self.taskbar.changeIndex(0)
            self.changePage(0)
        elif status == "edit":
            self.form = Forms()
            self.form.set_title("Edit Food Item")
            self.form.add_disabled_field("Food Name", self.item[idx].getName())
            self.form.add_disabled_field("Category", self.item[idx].getCategory())
            self.form.add_field("Priority", "High / Medium / Low")
            self.form.getButtonSubmit().clicked.connect(lambda: self.checkEditValid(self.pickfoodid))
            self.form.show()
        elif status == "add":
            self.form = Forms()
            self.form.set_title("Add Info For Inventory Item")
            self.form.add_disabled_field("Food Name", self.item[idx].getName())
            self.form.add_field("Food Cost", "Enter food cost (number)")
            self.form.add_field("Quantity", "Enter food quantity (number)")
            self.form.add_field("Unit", "Enter unit of quantity")
            self.form.add_field("Expired Due", "YYYY-MM-DD")
            self.form.add_field("Notes", "Enter food notes")
            self.form.add_field("Storing Location", "Refrigerator/Freezer/Pantry/Shelves/Rack")
            self.form.getButtonSubmit().clicked.connect(lambda: self.getInputFromAddItem(self.pickfoodid))
            self.form.show()

    def checkEditValid(self, i):
        if (self.form.getInput()[2][1] in ["High", "Medium", "Low"]):
            self.controller.delete_grocery_food(i)
            self.controller.insert_grocery_food(i, self.form.getInput()[2][1])
            self.currentCategory == "All Category"
            self.currentPrio == "All"
            self.taskbar.changeIndex(0)
            self.changePage(0)

    def getInputFromAddItem(self, i):
        if (self.form.getInput()[2][1].isdigit() and self.form.getInput()[1][1].isdigit() and re.search(
                "[0-9][0-9][0-9][0-9]-[0-9][0-9]-[0-9][0-9]", self.form.getInput()[4][1]) and self.form.getInput()[6][
            1] in ["Refrigerator", "Freezer", "Pantry", "Shelves", "Rack"]):
            self.controller.delete_grocery_food(i)
            self.controller.insert_stored_food(i, self.form.getInput()[2][1], self.form.getInput()[3][1],
                                               self.form.getInput()[1][1], self.form.getInput()[4][1],
                                               self.form.getInput()[6][1], self.form.getInput()[5][1])
            self.controller.insert_purchased_food(i, self.form.getInput()[2][1], self.form.getInput()[3][1], str(date.today()))
            self.currentCategory == "All Category"
            self.currentPrio == "All"
            self.taskbar.changeIndex(0)
            self.changePage(0)
