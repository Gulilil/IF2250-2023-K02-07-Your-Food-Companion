""" Notification Card"""

from PyQt6.QtWidgets import QWidget, QLabel, QScrollArea, QHBoxLayout, QPushButton
from PyQt6.QtGui import QFont
from PyQt6.QtCore import Qt

# Global Variabel Font
font = QFont("Karla", 13)
font.setWeight(600)

Notification_Read = """
    QWidget {
        background-color: #46494F;
        padding: 8px;
        color: white;
    }
    QWidget:hover {
        color: #897DCF;
    }
"""

Notification_Unread = """
    QWidget {
        background-color: #66696F;
        padding: 8px;
        color:white;
    }
"""

Title_Style = """
  QLabel {
    background-color: white;
    color: #2F3136; 
    padding : 3px;
    border-radius: 5px;
  }
"""


class NotificationCard(QWidget):
    arrMonths = ["January", "February", "March", "April", "May", "June", "July", "August", "September", "October", "November", "December"]
    isRead = False
    def __init__(self, parent=None, parentW=800):
        super(NotificationCard, self).__init__(parent)
        self.w = parentW-150; self.h = 80;
        self.resize(self.w, self.h)

        self.layer = QPushButton(self)
        self.layer.setStyleSheet(Notification_Unread)
        self.layer.resize(self.w, self.h)
        self.layer.clicked.connect(lambda: self.setCheck())


        # Time Stamp
        self.timeStamp = QWidget(self.layer)
        self.datetitle = QLabel(self.timeStamp)
        self.datetitle.setText("Date")
        self.datetitle.setFont(font)
        self.datetitle.setStyleSheet(Title_Style)
        self.date = QLabel(self.timeStamp)
        self.date.setText("31")
        self.date.setFont(font)
        self.date.move(0,25)
        self.month = QLabel(self.timeStamp)
        self.month.setText(self.arrMonths[11] + ",")
        self.month.move(35,25)
        self.month.setFont(font)
        self.year = QLabel(self.timeStamp)
        self.year.setText("0000")
        self.year.move(145,25)
        self.year.setFont(font)
        self.timeStamp.move(20,12)
        self.timeStamp.resize(200, 70)

        # Module
        self.moduletitle = QLabel(self.layer)
        self.moduletitle.move(260, 11)
        self.moduletitle.setText("Module")
        self.moduletitle.setFont(font)
        self.moduletitle.setStyleSheet(Title_Style)
        self.module = QLabel(self.layer)
        self.module.move(260, 38)
        self.module.setText("Food Inventory")
        self.module.setStyleSheet("color: white")
        self.module.setFont(font)

        # Notes
        self.scrollableNotes = QScrollArea(self.layer)
        self.scrollableNotes.move(500, 28)
        self.scrollableNotes.resize(300, 60)

        # self.hbox = QHBoxLayout()

        self.notes = QLabel(self.layer)
        self.notes.setText("Temporary Notes")
        self.notes.setStyleSheet("color:white")
        # self.notes.setWordWrap(True)
        self.notes.setFont(font)

        self.scrollableNotes.setWidget(self.notes)
        self.scrollableNotes.setVerticalScrollBarPolicy(Qt.ScrollBarPolicy.ScrollBarAlwaysOff)
        self.scrollableNotes.setHorizontalScrollBarPolicy(Qt.ScrollBarPolicy.ScrollBarAlwaysOff)
        self.scrollableNotes.setWidgetResizable(True)
        


    def setTime(self, date, month, year):
        self.date.setText(str(date))
        self.month.setText(self.arrMonths[month]+ ", ")
        self.year.setText(str(year))

    def setDescription(self, module, notes):
        self.module.setText(module)
        self.notes.setText(notes)

    def setCheck(self):
        self.isRead = True
        # self.checkbox.setChecked(True)
        self.layer.setStyleSheet(Notification_Read)

    def setUncheck(self):
        self.isRead = False
        # self.checkbox.setChecked(False)
        self.layer.setStyleSheet(Notification_Unread)

    def changeState(self):
        if (self.isRead):
            self.setUncheck() 
        else :
            self.setCheck()
    
    def getWidget(self):
        return self.layer
    
