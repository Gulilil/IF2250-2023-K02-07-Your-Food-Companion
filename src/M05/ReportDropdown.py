from PyQt6.QtWidgets import QComboBox
from PyQt6.QtGui import QFont, QColor, QPalette, QFontDatabase
from PyQt6 import QtGui, QtCore
import os

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
                color: #F2F3F5;
            }
            QComboBox::down-arrow{
                image: url(./assets/icons/expand.png);
                width: 30px;
                height:30px;
                margin-right:10px;
            }
            QComboBox::drop-down{
                border:0;
                width:30px;
            }
            QListView::item {
                color: #F2F3F5;
                margin-left:10px
            }
            QComboBox:hover {
                border: 2px solid #F2F3F5;
            }
            QComboBox:on {
                border: 2px solid #F2F3F5;
            }
            QComboBox QAbstractItemView {
                padding: 2px;
                border-radius: 0;
            }
        """)    # Dropdown icon does not show up
        
        # Load font
        font_path = os.path.join(os.path.dirname(__file__), "../../assets/font/Karla-Regular.ttf")
        font_id = QFontDatabase.addApplicationFont(font_path)
        
        if (font_id == -1):
            print("Error: font not found")
        
        font_family = QFontDatabase.applicationFontFamilies(font_id)
        font = QFont(font_family, 14)
        self.setFont(font)
        
        # set text color
        palette = self.palette()
        palette.setColor(QPalette.ColorRole.Text, QColor('#F2F3F5'))
        self.setPalette(palette)

        # self.setStyleSheet("""
        #     QComboBox {
        #         background-color: #36393F;
        #         color: #F2F3F5;
        #         border-radius: 8px;
        #         padding: 8px;
        #     }
        #     QComboBox::down-arrow {
        #         image: url(""" + dropdown_icon + """);
        #         color: #F2F3F5;
        #         width: 10px;
        #         height: 10px;
        #         border-radius: 8px;
        #     }
        # """)    # Dropdown icon does not show up
