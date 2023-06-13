""" Notification Page """

from PyQt6.QtCore import Qt
from PyQt6.QtGui import QFont
from PyQt6.QtWidgets import QWidget, QScrollArea, QVBoxLayout, QHBoxLayout, QLabel, QPushButton

from src.notification.notification_card import NotificationCard
from src.notification.notification_dropdown import NotificationDropdown

Notification_Dummy_Data = [
    (29, 2, 2023, "Food Inventory", "Ini merupakan sebuah makanan yang akan expired dalam dua hari kedepan"),
    (1, 2, 2023, "Food Inventory", "Ayam Geprek is Expired"),
    (8, 7, 2023, "Shopping List", "Daging Tikus has been Added"),
    (19, 12, 2023, "Shopping History", "Birthday Cake has been Bought"),
    (9, 5, 2023, "Food Inventory", "Borax has been Added"),
    (1, 10, 2023, "Food Inventory", "Pisang Goreng has been Added"),
    (17, 8, 2023, "Food Inventory", "Random Food has been Spawned"),
    (9, 3, 2023, "Shopping List", "Steak is Added to the Wishlist"),
    (6, 5, 2023, "Food Inventory", "Sate Padang has been Consumed"),
    (4, 11, 2023, "Shopping History", "Nasi Goreng has been moved to Shopping History"),

]

# Global Variabel Font
font = QFont("Karla", 13)
font.setWeight(600)


class Notification(QWidget):
    width = 1200
    height = 700

    def __init__(self):
        super(Notification, self).__init__()
        self.resize(self.width, self.height)

        # Making widget item for the class
        self.layer = QWidget(self)
        self.layer.resize(self.width, self.height)
        self.layer.setStyleSheet("background-color: #36393F")

        # Every components in this page, please use "self.layer" as its parent
        # Because "self.layer" is the Widget that will be inserted into Stack in Main.py

        self.container = QWidget(self.layer)
        self.container.setStyleSheet("background-color: #2F3136; border-radius: 20px;")
        self.containerW = self.width - 100;
        self.containerH = self.height - 200
        self.container.resize(self.containerW, self.containerH)
        self.container.move(50, 50)

        # Drop down
        self.dropdown = NotificationDropdown(self.container)
        self.dropdown.move(50, 20)

        # Mark all as read
        self.markAll = QPushButton(self.container)
        self.markAll.move(self.containerW - 220, 30)
        self.markAll.setText("Mark all as read")
        self.markAll.setStyleSheet("""
          QPushButton {
            background: transparent;
            color:white;
          }
          QPushButton:hover{
            color:#897DCf;
          }
        """)
        self.markAll.setFont(font)
        self.markAll.clicked.connect(lambda: self.markAllAsRead())

        # Scrollable Table
        self.scrollable = QScrollArea(self.container)
        self.scrollable.move(40, 80)
        self.scrollable.resize(self.containerW - 100, self.containerH - 150)
        self.cardContainer = QWidget()
        self.vbox = QVBoxLayout()
        for i in range(len(Notification_Dummy_Data)):
            layout = QHBoxLayout()
            card = NotificationCard(None, self.containerW)
            card.setTime(Notification_Dummy_Data[i][0], Notification_Dummy_Data[i][1] - 1,
                         Notification_Dummy_Data[i][2])
            card.setDescription(Notification_Dummy_Data[i][3], Notification_Dummy_Data[i][4])
            card.setMinimumHeight(80)
            layout.addWidget(card)
            self.vbox.addLayout(layout)
        self.cardContainer.setLayout(self.vbox)
        self.scrollable.setVerticalScrollBarPolicy(Qt.ScrollBarPolicy.ScrollBarAlwaysOn)
        self.scrollable.setHorizontalScrollBarPolicy(Qt.ScrollBarPolicy.ScrollBarAlwaysOff)
        self.scrollable.setWidgetResizable(True)
        self.scrollable.setWidget(self.cardContainer)

        # Description
        self.desc = QLabel(self.container)
        self.desc.move(50, self.containerH - 55)
        self.desc.setText("Notifications will be automatically deleted after a month.")
        self.desc.setFont(font)
        self.desc.setStyleSheet("color: white;")

    def getWidget(self):
        return self.layer

    def markAllAsRead(self):
        for i in range(len(Notification_Dummy_Data)):
            layout = self.vbox.itemAt(i).layout()
            item = layout.itemAt(0).widget()
            item.setCheck()
