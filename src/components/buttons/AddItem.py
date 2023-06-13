""" Add Item Button Components """

from PyQt6.QtGui import QFont
from PyQt6.QtWidgets import QPushButton
from src.components.form.Form import Forms

addItemFont = QFont("Karla", 25)
addItemFont.setWeight(600)


class AddItemButton(QPushButton):
    def __init__(self, parent):
        super(AddItemButton, self).__init__(parent)
        self.resize(40, 40)
        self.setText("+")
        self.setFont(addItemFont)
        self.setStyleSheet("""
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
        self.clicked.connect(lambda: self.popUpAddItem())

    def popUpAddItem(self):
        self.form = Forms()
        self.form.set_title("Add Food Item")
        self.form.add_field("Food Name", "Enter food name")
        self.form.add_field("Category", "Enter food category")
        self.form.add_field("Food Cost", "Enter food cost")
        self.form.add_field("Quantity", "Enter food quantity")
        self.form.add_field("Expired Due", "Enter expiry date")
        self.form.add_field("Notes", "Enter food notes")
        self.form.getButtonSubmit().clicked.connect(lambda: self.getInputFromAddItem())
        self.form.show()

    def getInputFromAddItem(self):
        return self.form.getInput()
