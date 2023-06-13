from PyQt6.QtGui import QFont, QColor, QPalette
from PyQt6.QtWidgets import QWidget, QLineEdit, QPushButton, QHBoxLayout


class ShoppingHistorySearchBar(QWidget):
    content = ""

    font = QFont("Karla", 11)
    font.setWeight(600)

    def __init__(self, parent):
        super().__init__(parent)

        layout = QHBoxLayout()
        self.setLayout(layout)
        self.setContentsMargins(0, 0, 0, 0)
        layout.setContentsMargins(0, 0, 0, 0)
        layout.setSpacing(0)

        self.textField = QLineEdit(self)
        layout.addWidget(self.textField)
        palette = self.textField.palette()
        palette.setColor(QPalette.ColorRole.PlaceholderText, QColor('#F2F3F5'))
        palette.setColor(QPalette.ColorRole.Text, QColor('#F2F3F5'))
        self.textField.setPalette(palette)
        self.textField.setPlaceholderText("Search...")
        self.textField.setFont(ShoppingHistorySearchBar.font)
        self.textField.setStyleSheet("""
            QLineEdit {
                background-color: #36393F;
                border-radius: 8px;
                padding: 8px;
                border: 2px solid #36393F;
            }
        """)

        self.icon = QPushButton(self)
        layout.addWidget(self.icon)
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

    def get_content(self):
        return self.content

    def get_search_button(self):
        return self.icon
