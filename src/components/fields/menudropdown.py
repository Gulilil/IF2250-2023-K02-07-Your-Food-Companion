""" Menu Dropdown """

import os

from PyQt6 import QtGui, QtCore
from PyQt6.QtCore import QSize
from PyQt6.QtGui import QFont, QColor, QPalette, QFontDatabase
from PyQt6.QtWidgets import QComboBox, QWidget

from src.components.buttons.Checkbox import Checkbox

# Global Variabel Font
font = QFont("Karla", 11)
font.setWeight(600)


class MenuDropdown(QWidget):
    def __init__(self, parent):
        super(MenuDropdown, self).__init__(parent)

        # Top Left Drop-down
        self.dropdown = Dropdown(self)
        self.dropdown.setFont(font)
        self.dropdown.adjustSize()
        self.dropdown.currentIndexChanged.connect(lambda: self.process(self.dropdown.currentIndex()))
        self.addChoiceIcon(QtGui.QIcon("./assets/icons/menu.png"), "")
        self.dropdown.setItemData(0, QSize(0, 0), QtCore.Qt.ItemDataRole.SizeHintRole)
        self.currentIndex = 0
        view = self.dropdown.view()
        view.setFixedWidth(150)
        self.delete = Checkbox(None)
        self.edit = Checkbox(None)
        self.add = Checkbox(None)

    def addChoice(self, name):
        self.dropdown.addItem(QtGui.QIcon("./assets/icons/category.png"), name)

    def addChoiceName(self, name):
        self.dropdown.addItem(name)

    def addChoiceIcon(self, icon, name):
        self.dropdown.addItem(icon, name)

    def getObject(self):
        return self.dropdown

    def getDelete(self):
        return self.delete

    def getEdit(self):
        return self.edit

    def getAdd(self):
        return self.add

    def process(self, idx):
        temp = self.dropdown.currentText()
        if idx == 1:
            if self.delete.isChecked():
                self.delete.setChecked(False)
            else:
                self.delete.setChecked(True)
        elif idx == 2:
            if self.edit.isChecked():
                self.edit.setChecked(False)
            else:
                self.edit.setChecked(True)
        elif idx == 3:
            if self.add.isChecked():
                self.add.setChecked(False)
            else:
                self.add.setChecked(True)
        self.dropdown.setCurrentIndex(0)


class Dropdown(QComboBox):
    def __init__(self, parent=None):
        super().__init__(parent)

        # set placeholder text and color
        placeholder_text = "Select an option"

        pal = self.palette()
        pal.setColor(QPalette.ColorRole.PlaceholderText, QColor('#D4D7DC'))
        self.setPalette(pal)

        # Issue: Dropdown icon still does not show properly
        dropdown_icon = os.path.join(os.path.dirname(__file__), "../../../assets/icons/down_arrow.png")

        # Set style
        self.setStyleSheet("""
            QComboBox{
                background-color: #36393F;
                border: 2px solid #36393F;
                border-radius: 8px;
                padding: 8px;
                width: 15px;
                color: #F2F3F5;
            }
            QComboBox::down-arrow{
                image: url(./assets/icons/expand.png);
                width: 0;
                height:30px;
                margin-right:0px;
            }
            QComboBox::drop-down{
                border:0;
                width:0px;
            }
            QListView::item {
                color: #F2F3F5;
                padding:5px;
                margin-left:10px
            }
            QComboBox:hover {
                border: 2px solid #F2F3F5;
                padding: 8px;
            }
            QComboBox:on {
                border: 2px solid #F2F3F5;
                padding: 8px;
            }

        """)  # Dropdown icon does not show up

        # Load font
        font_path = os.path.join(os.path.dirname(__file__), "../../../assets/font/Karla-Regular.ttf")
        font_id = QFontDatabase.addApplicationFont(font_path)

        if font_id == -1:
            print("Error: font not found")

        font_family = QFontDatabase.applicationFontFamilies(font_id)
        font = QFont(font_family, 20)
        self.setFont(font)

        # set text color
        palette = self.palette()
        palette.setColor(QPalette.ColorRole.Text, QColor('#F2F3F5'))
        self.setPalette(palette)
