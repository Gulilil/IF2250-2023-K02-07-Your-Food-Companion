"""Shopping List Item Components """

from PyQt6.QtGui import QFont
from PyQt6.QtWidgets import QWidget, QLabel

from src.components.buttons.Checkbox import Checkbox
from src.components.fields.menudropdown import MenuDropdown

font = QFont("Karla", 15)
font.setWeight(600)

font2 = QFont("Karla", 9)
font2.setWeight(600)


class ShoppingListItem(QWidget):
    def __init__(self, parent, height, width, name, priority, category):
        super(ShoppingListItem, self).__init__(parent)
        self.resize(int(width), int(height))

        self.layer = QWidget(self)
        self.layer.setStyleSheet("background-color:#36393F;border-radius:10px")
        self.layer.resize(int(width), int(height))

        self.food_Name = QLabel(self.layer)
        self.food_Name.setText(str(name))
        self.food_Name.setFont(font)
        self.food_Name.move(20, 15)
        self.food_Name.setStyleSheet("color:#F2F3F5")

        self.priority = QLabel(self.layer)
        self.priority.setText(priority)
        self.priority.setFont(font2)
        self.priority.move(20, self.layer.height() - 50)
        self.priority.setStyleSheet("color:#F2F3F5")

        self.category = QLabel(self.layer)
        self.category.setText(category)
        self.category.setFont(font2)
        self.category.move(20, self.layer.height() - 30)
        self.category.setStyleSheet("color:#F2F3F5")

        self.menu = MenuDropdown(self.layer)
        self.menu.addChoiceName("Delete")
        self.menu.addChoiceName("Edit")
        self.menu.addChoiceName("Add To Inventory")
        self.menu.move(self.layer.width() - int(self.menu.width() / 2), 15)
        self.menu.getDelete().stateChanged.connect(lambda: self.processDelete())
        self.menu.getEdit().stateChanged.connect(lambda: self.processEdit())
        self.menu.getAdd().stateChanged.connect(lambda: self.processAdd())

        self.change = Checkbox(None)
        self.status = ""

    def resetText(self, name, priority, category):
        self.food_Name.setText(name)
        self.food_Name.adjustSize()
        self.priority.setText(priority)
        self.priority.adjustSize()
        self.category.setText(category)
        self.category.adjustSize()

    def getName(self):
        return self.food_Name.text()

    def getPrio(self):
        return self.priority.text()

    def getCategory(self):
        return self.category.text()

    def getChange(self):
        return self.change

    def getStatus(self):
        return self.status

    def processDelete(self):
        self.status = "delete"
        if self.change.isChecked():
            self.change.setChecked(False)
        else:
            self.change.setChecked(True)

    def processEdit(self):
        self.status = "edit"
        if self.change.isChecked():
            self.change.setChecked(False)
        else:
            self.change.setChecked(True)

    def processAdd(self):
        self.status = "add"
        if self.change.isChecked():
            self.change.setChecked(False)
        else:
            self.change.setChecked(True)
