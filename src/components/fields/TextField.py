import os

from PyQt6.QtGui import QFont, QColor, QPalette, QFontDatabase
from PyQt6.QtWidgets import QLabel
from PyQt6.QtWidgets import QLineEdit


class TextField(QLineEdit):
    def __init__(self, placeholder_text, parent=None):
        super().__init__(parent)

        # set placeholder text and color
        pal = self.palette()
        pal.setColor(QPalette.ColorRole.PlaceholderText, QColor('#D4D7DC'))
        self.setPlaceholderText(placeholder_text)
        self.setPalette(pal)
        self.resize(100, 30)

        self.setStyleSheet(
            "background-color: #4D5259; border-radius: 8px; padding: 8px; border: 2px solid #4D5259; margin-right: 20px;")

        # Load font
        font_path = os.path.join(os.path.dirname(__file__), "../../../assets/font/Karla-Regular.ttf")
        font_id = QFontDatabase.addApplicationFont(font_path)

        if (font_id == -1):
            print("Error: font not found")

        font_family = QFontDatabase.applicationFontFamilies(font_id)[0]
        font = QFont(font_family, 20)
        self.setFont(font)
        palette = self.palette()
        palette.setColor(QPalette.ColorRole.Text, QColor('#F2F3F5'))
        self.setPalette(palette)

    def focusInEvent(self, event):
        super().focusInEvent(event)
        self.setStyleSheet(
            "background-color: #4D5259; border-radius: 8px; padding: 8px; border: 2px solid #D4D7DC;margin-right: 20px;")

    def focusOutEvent(self, event):
        super().focusOutEvent(event)
        self.setStyleSheet(
            "background-color: #4D5259; border-radius: 8px; padding: 8px; border: 2px solid #4D5259;margin-right: 20px;")

    def set_label(self, label):
        self.label = QLabel(label)
        self.label.setStyleSheet("background: transparent; color: #D4D7DC; margin-left:20px;")

        # Load font
        font_path = os.path.join(os.path.dirname(__file__), "../../../assets/font/Karla-Bold.ttf")
        font_id = QFontDatabase.addApplicationFont(font_path)

        if font_id == -1:
            print("Error: font not found")

        font_family = QFontDatabase.applicationFontFamilies(font_id)[0]
        font = QFont(font_family, 15)

        self.label.setFont(font)
