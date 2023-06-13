""" All Foods Tab """

from PyQt6.QtGui import QFont
from PyQt6.QtWidgets import QPushButton, QWidget, QVBoxLayout, QHBoxLayout, QSizePolicy as qp

from src.M02.inventory_data.data_tab.all_food.all_food_hero import AllFoodHero
from src.M02.inventory_data.inventory_dropdown import InventoryDropdown
from src.M02.inventory_data.inventory_searchbar import InventorySearchbar
from src.components.buttons.Button import Button
from src.components.form.Form import Forms
from src.components.pagination.Pagination import Pagination
from src.components.table.Table import Table
from src.M02.inventory_manager import *
from datetime import datetime

im = InventoryManager()

# Global Variabel Font
font = QFont("Karla", 11)
font.setWeight(600)
addItemFont = QFont("Karla", 25)
addItemFont.setWeight(600)

class AllFoodTab(QWidget):
    currentCategory = "All Categories"
    def __init__ (self):
        super(AllFoodTab, self).__init__()

        self.layer = QWidget(self)
        self.layer.setStyleSheet("background-color: #2F3136")
        self.layer.setContentsMargins(0,0,0,0)
        self.layerLayout = QVBoxLayout()
        self.layerLayout.addWidget(self.layer)
        self.layerLayout.setContentsMargins(0,0,0,0)
        self.setLayout(self.layerLayout)

        self.contentLayout = QVBoxLayout()
        self.contentLayout.setContentsMargins(32,32,32,32)
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

        # # Add Item
        self.additem = QPushButton(self.layer)
        self.additem.setSizePolicy(qp.Policy.Fixed, qp.Policy.Fixed)
        self.headerLayout.addWidget(self.additem)
        self.additem.setFixedSize(40,40)
        self.additem.setText("+")
        self.additem.setFont(addItemFont)
        self.additem.setStyleSheet("""
            QPushButton {
                background-color: #897DCF; 
                border-radius: 20px;
                color:black;
                text-align: center;
                padding-bottom: 5px;
            }
            QPushButton:hover {
                background-color: #998DDF;
            }
         """)
        self.additem.clicked.connect(lambda: self.popUpAddItem())

        # # Adding hero
        self.hero = AllFoodHero(self.layer)
        self.contentLayout.addWidget(self.hero)

        # Buttons
        self.buttonsContainer = QWidget()
        self.hbox = QHBoxLayout()
        self.buttonConsumed = Button(None, "Small")
        self.buttonConsumed.setText("Add to Consumed")
        self.buttonConsumed.clicked.connect(lambda: self.addFoodToConsumed())
        self.buttonEdit= Button(None, "Small")
        self.buttonEdit.setText("Edit Item")
        self.buttonEdit.clicked.connect(lambda: self.popUpEditItem())
        self.buttonDelete = Button(None, "Small")
        self.buttonDelete.setText("Delete Item")
        self.buttonDelete.clicked.connect(lambda: self.deleteItem())
        self.hbox.addWidget(self.buttonConsumed)
        self.hbox.addWidget(self.buttonEdit)
        self.hbox.addWidget(self.buttonDelete)
        self.buttonsContainer.setLayout(self.hbox)
        self.contentLayout.addWidget(self.buttonsContainer)
        
        # # Table data
        self.header = im.Stored_Food_Data_Header
        self.data = im.getStoredFoodData(None)
        self.setTables(self.data)


    def setTables(self, d):
        d = self.checkItemExpired(d)
        nRows = 3
        pageAmount = ((len(d)-1) //nRows) + 1

        table_pagination = Pagination(self.layer, pageAmount)
        self.table = Table(data=d, pagination= table_pagination, rowsPerPage=nRows, headers= self.header, useCheckbox= True)

        self.contentLayout.addWidget(self.table)
        self.contentLayout.addWidget(table_pagination)

        self.setHeroGoodPercentage(im.goodPercentage())
        self.setHeroStalePercentage(im.stalePercentage())
        self.setHeroExpiredPercentage(im.expiredPercentage())

    def updateTables(self, d):
        prevTable = self.contentLayout.itemAt(3).widget()
        prevTable.deleteLater()
        prevPagination = self.contentLayout.itemAt(4).widget()
        prevPagination.deleteLater()
        self.setTables(d)
        
        

    def getWidget(self):
        return self.layer
       
    def getCategories(self):
        return self.categories
    
    def getButtonSearchbar(self):
        return self.searchbar.getButtonSearchbar()
    
    def getButtonAddItem(self):
        return self.additem
    
    
    def popUpAddItem(self):
        self.form = Forms()
        self.form.set_title("Add Food Item")
        self.form.add_field("Food Name", "e.g. \"Ayam Geprek\" ")
        self.form.add_field("Category", "e.g. \"Vegetables\" ")
        self.form.add_field("Food Cost", "e.g. \"20000\"")
        self.form.add_field("Quantity", "e.g. \"5\"")
        self.form.add_field("Expired Due", "dd-mm-yyyy e.g. \"05-07-2020\"")
        self.form.add_field("Storing Location", "e.g. \"Di kolong meja\"")
        self.form.add_field("Notes", "e.g. \"Digoreng dadakan\"")
        self.form.getButtonSubmit().clicked.connect(lambda: self.addFoodItem())
        self.form.show()

    def addFoodItem(self):
        c = Controller()
        self.arrInput = self.form.getInput()
        print(self.arrInput)
        validTuple = im.isItemInputValid(self.arrInput)
        if (validTuple[0]):
            # Setup date
            oldDate = self.arrInput[4][1].split("-")
            newDate = oldDate[2]+"-"+oldDate[1]+"-"+oldDate[0]
            # setup category
            newCategory = im.getCategoryFromKey(self.arrInput[1][1])
            newID = im.getLastFoodID()+1
            c.insert_food(newID, self.arrInput[0][1], newCategory)
            c.insert_stored_food(newID, self.arrInput[3][1], "pieces", self.arrInput[2][1], newDate, self.arrInput[5][1], self.arrInput[6][1])
            self.data = im.getStoredFoodData(None)
            self.updateTables(self.data)
        else :
          print("Invalid Input")
            

    def setHeroGoodPercentage(self, n):
        self.hero.setGoodPercentage(n)
    
    def setHeroStalePercentage(self, n):
        self.hero.setStalePercentage(n)

    def setHeroExpiredPercentage(self, n):
        self.hero.setExpiredPercentage(n)

    def changeCategory(self, category):
        self.currentCategory = category
        if category == "All Categories":
          self.data = im.getStoredFoodData(None)
        else :
          self.data = im.getStoredFoodData(category)
        self.updateTables(self.data)

    def changeSearch(self):
        category = self.currentCategory
        content = self.searchbar.getContent()
        print(category, content)
        if (category == "All Categories"):
            temp = im.getStoredFoodData(None)
        else:
            temp = im.getStoredFoodData(category)
        self.data = []
        for i in temp:
            if (content in i[0]):
                self.data.append(i)
        self.updateTables(self.data)

    def getAddItemForm(self):
        return self.form
        
    def popUpEditItem(self):
        selectedIdx = self.table.getCheckedIndexes()
        if (len(selectedIdx) != 1):
            print("Exactly one selected item is needed")
        else :
            item = (self.getItemAtIndex(selectedIdx[0]))
            dbItem = self.getItemFromDatabase(item)

            self.editForm = Forms()
            self.editForm.set_title("Edit Food Item")
            self.editForm.add_field("Food Name", "before: \""+str(dbItem[7])+"\" ")
            self.editForm.add_field("Category", "before: \""+str(dbItem[8])+"\" ")
            self.editForm.add_field("Food Cost", "before: \""+str(dbItem[3])+"\" ")
            self.editForm.add_field("Quantity", "before: \""+str(dbItem[1])+"\"")
            self.editForm.add_field("Expired Due", "dd-mm-yyyy ")
            self.editForm.add_field("Storing Location", "before: \""+str(dbItem[5])+"\"")
            self.editForm.add_field("Notes", "before: \""+str(dbItem[6])+"\"")
            self.editForm.getButtonSubmit().clicked.connect(lambda: self.editFoodItem(dbItem[0]))
            self.editForm.show()

    def getItemFromDatabase(self, item):
        c = Controller()
        allStoredFood = c.get_stored_food()
        for i in allStoredFood:
          # Check name, cost, date, quantity
          if (item[0] == i[len(i)-2] and item[1] == i[3] and item[2] == i[4] and item[3]== i[1]):
              return i

    def editFoodItem(self, id):
        c = Controller()
        self.arrInput = self.editForm.getInput()
        print(self.arrInput)
        validTuple = im.isItemInputValid(self.arrInput)
        if (validTuple[0]):
            # Setup date
            oldDate = self.arrInput[4][1].split("-")
            newDate = oldDate[2]+"-"+oldDate[1]+"-"+oldDate[0]
            # setup category
            newCategory = im.getCategoryFromKey(self.arrInput[1][1])
            c.update_food(id, self.arrInput[0][1], newCategory)
            c.update_stored_food(id, self.arrInput[3][1], "pieces", self.arrInput[2][1], newDate, self.arrInput[5][1], self.arrInput[6][1])
            self.data = im.getStoredFoodData(None)
            self.updateTables(self.data)
        else :
          print("Invalid Input")
        
        
    def deleteItem(self):
        c = Controller()
        selectedIdx = self.table.getCheckedIndexes()
        arr = []
        dbItems = []
        for i in selectedIdx:
            arr.append(self.data[i])
        for i in range(len(arr)):
            dbItems.append(self.getItemFromDatabase(arr[i]))
        
        for i in range(len(dbItems)):
            c.delete_food(dbItems[i][0])
            c.delete_stored_food(dbItems[i][0])

        self.data = im.getStoredFoodData(None)
        self.updateTables(self.data)


    def addFoodToConsumed(self):
        c = Controller()
        selectedIdx = self.table.getCheckedIndexes()
        arr = []
        dbItems = []
        for i in selectedIdx:
            arr.append(self.data[i])
        for i in range(len(arr)):
            dbItems.append(self.getItemFromDatabase(arr[i]))
          
        for i in range(len(dbItems)):
            # setup eaten date
            year = str(datetime.now().year)
            month = str(datetime.now().month)
            day = str(datetime.now().day)
            if len(month) == 1:
                month = "0"+month
            if len(day) == 1:
                day = "0"+day
            date = year+"-"+month+"-"+day

            # insert
            print(dbItems[i])
            c.insert_eaten_food(dbItems[i][0], dbItems[i][1], "pieces", date)
            c.delete_stored_food(dbItems[i][0])
        self.data = im.getStoredFoodData(None)
        self.updateTables(self.data)

    def getItemAtIndex(self, n):
        return self.data[n]
    
    def checkItemExpired(self, items):
        c = Controller()
        arr = []
        for i in range(len(items)):
            if (self.isExpired(items[i][2])):
                arr.append(items[i])

        dbItems = []
        for i in range(len(arr)):
            dbItems.append(self.getItemFromDatabase(arr[i]))
        
        for i in range(len(dbItems)):
            c.insert_expired_food(dbItems[i][0], dbItems[i][1], dbItems[i][2], dbItems[i][3],  dbItems[i][4])
            c.delete_stored_food(dbItems[i][0])
        return im.getStoredFoodData(None)


    def isExpired(self, date):
        arr = date.split("-")
        y = int(arr[0])
        m = int(arr[1])
        d = int(arr[2])

        if y < int(datetime.now().year):
            return True
        elif y > int(datetime.now().year):
            return False
        else :
            if m < int(datetime.now().month):
                return True
            elif m > int(datetime.now().month):
                return False
            else:
                if d <= int(datetime.now().day):
                    return True
                else :
                    return False