""" Searchbar """

from PyQt6.QtGui import QFont, QColor, QPalette
from PyQt6.QtWidgets import QWidget, QLineEdit, QPushButton

# Global Variabel Font
font = QFont("Karla", 11)
font.setWeight(600)


class Searchbar(QWidget):
    content = ""

    def __init__(self, parent):
        super(Searchbar, self).__init__(parent)
        self.resize(320, 50)

        self.textField = QLineEdit(self)
        pal = self.textField.palette()
        pal.setColor(QPalette.ColorRole.PlaceholderText, QColor('#F2F3F5'))
        pal.setColor(QPalette.ColorRole.Text, QColor('#F2F3F5'))
        self.textField.setPalette(pal)
        self.textField.move(0, 0)
        self.textField.resize(250, 50)
        self.textField.setPlaceholderText("Search...")
        self.textField.setFont(font)
        self.textField.setStyleSheet("""
            QLineEdit {
                background-color: #36393F;
                border-radius: 8px;
                padding: 8px;
                border: 2px solid #36393F;
            }
        """)

        self.icon = QPushButton(self)
        self.icon.move(250, 0)
        self.icon.resize(50, 50)
        self.icon.setStyleSheet("""
            QPushButton {
                background: transparent; 
                image: url(./assets/icons/searchbar.png); 
                padding: 10px; 
                margin-left:10px;
                border-radius: 5px;
                border: 2px solid #36393F;
            } 
            QPushButton:hover{
                background-color: #36393F;
            }
        """)
        self.icon.clicked.connect(lambda: self.submit())

    def submit(self):
        content = self.textField.text()
        self.content = content

    def getContent(self):
        return self.content

    def getButtonSearchbar(self):
        return self.icon

    def clear(self):
        self.textField.clear()
