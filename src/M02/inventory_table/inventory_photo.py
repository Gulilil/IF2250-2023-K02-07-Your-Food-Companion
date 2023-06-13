""" Inventory Photo"""

from PyQt6.QtWidgets import QWidget, QPushButton

# image : url(./assets/img/profile_food.png)
Photo_Style = """
    border-radius: 60px;
    border: 5px solid #4D5259;
    padding: 5px;
"""


# class Photo(QLabel):
#     def __init__ (self, parent):
#         super(Photo, self).__init__(parent)
#         img = QPixmap("./assets/img/profile_food.png")
#         img = img.scaledToHeight(75)
#         self.setPixmap(img)
#         self.setStyleSheet(Photo_Style)

class InventoryPhoto(QPushButton):
    def __init__(self, parent):
        super(InventoryPhoto, self).__init__(parent)
        self.setStyleSheet(Photo_Style)
        self.setFixedSize(120, 120)
        self.white = QWidget(self)
        self.white.setStyleSheet("background-color: white; border-radius: 55px")
        self.white.resize(110, 110)
        self.white.move(5, 5)
