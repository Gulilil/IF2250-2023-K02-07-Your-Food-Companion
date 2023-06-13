""" Shopping Add Item Button Components """

from PyQt6.QtGui import QFont
from PyQt6.QtWidgets import QPushButton

from src.components.buttons.Checkbox import Checkbox
from src.components.form.Form import Forms

addItemFont = QFont("Karla", 25)
addItemFont.setWeight(600)

default_style = """
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
         """

invalid_style = """
            QPushButton {
                background-color: red; 
                border-radius: 20px;
                color:black;
                text-align: center;
                padding-bottom: 5px;
            }
            QPushButton:hover {
                background-color: red;
            }
         """


class ShoppingAddItemButton(QPushButton):
    def __init__(self, parent):
        super(ShoppingAddItemButton, self).__init__(parent)
        self.resize(40, 40)
        self.setText("+")
        self.setFont(addItemFont)
        self.setStyleSheet(default_style)
        self.clicked.connect(lambda: self.popUpAddItem())
        self.form = Forms()
        self.data = None
        self.valid = Checkbox(None)

    def popUpAddItem(self):
        self.data = None
        self.form = Forms()
        self.form.set_title("Add Food Item")
        self.form.add_field("Food Name", "Enter food name")
        self.form.add_field("Category", "Enter food category")
        self.form.add_field("Priority", "Enter food priority")
        self.form.getButtonSubmit().clicked.connect(lambda: self.checkValid())
        self.form.show()

    def checkValid(self):
        if (self.form.getInput()[2][1] not in ["High", "Medium", "Low"]):
            self.setStyleSheet(invalid_style)
            self.data = None
        else:
            self.setStyleSheet(default_style)
            self.data = self.form.getInput()
            if self.valid.isChecked():
                self.valid.setChecked(False)
            else:
                self.valid.setChecked(True)

    def getData(self):
        return self.data

    def getForm(self):
        return self.form

    def getValid(self):
        return self.valid
