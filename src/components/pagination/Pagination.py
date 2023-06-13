from collections.abc import Callable

from PyQt6.QtGui import QFont
from PyQt6.QtWidgets import QPushButton, QWidget, QHBoxLayout, QVBoxLayout, QSizePolicy

from src.components.buttons.Checkbox import Checkbox

# Global Variabel Font
font = QFont("Karla", 11)
font.setWeight(700)

Arrow_Style = """
    QPushButton {
        background : transparent;
        color : #F2F3F5;
        border : 0;
    }
    QPushButton:hover {
        color : #897DCF;
    }
"""

Arrow_Disabled = """
    QPushButton {
        background : transparent;
        color : #D4D7DC;
        border : 0;
    }
"""


class Arrow(QPushButton):
    valid = True
    val = None
    w = 112
    h = 47

    def __init__(self, parent, props):
        super(Arrow, self).__init__(parent)
        self.setStyleSheet(Arrow_Style)
        self.resize(self.w, self.h)
        self.setFont(font)
        if props == "Next":
            self.val = props
            self.setText("Next >")
        elif props == "Back":
            self.val = props
            self.setText("< Back")

    def setEnabled(self):
        self.valid = True
        self.setStyleSheet(Arrow_Style)

    def setDisabled(self):
        self.valid = False
        self.setStyleSheet(Arrow_Disabled)


PageNumber_Style = """
    QPushButton {
        background : transparent;
        color : #F2F3F5;
        border : 0;
    }
    QPushButton:hover {
        color : #897DCF;
    }
"""

PageNumber_Current_Style = """
    QPushButton {
        background : #897DCF;
        color : #F2F3F5;
        border-radius : 15px;
    }
"""


class PageNumber(QPushButton):
    isCurrent = False
    num = None

    def __init__(self, parent, number):
        super(PageNumber, self).__init__(parent)
        self.num = number
        self.setStyleSheet(PageNumber_Style)
        self.setFixedSize(30, 30)
        self.setText(str(number))
        self.setFont(font)

    def setCurrent(self):
        self.isCurrent = True
        self.setStyleSheet(PageNumber_Current_Style)

    def setNotCurrent(self):
        self.isCurrent = False
        self.setStyleSheet(PageNumber_Style)

    def changeNum(self, n):
        self.num = n
        self.setText(str(n))

    def getNum(self):
        return self.num


Pagination_Layer_Style = '''
    background-color: #2F3136;
    border-radius:20px;
'''


class Pagination(QWidget):
    def __init__(self, parent, amount):
        super(Pagination, self).__init__(parent)

        self.arr = []
        self.amountPage = 1
        self.currentPage = 1
        self.template = None
        self.w = 586
        self.h = 50
        self.xPad = 30
        self.avgh = 40
        self.onChangePage: Callable[[int], None] = lambda pageNum: None

        self.amountPage = amount
        self.resize(self.w, self.h)

        self.layer = QWidget(self)
        self.layer.setSizePolicy(QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Fixed)
        self.layer.setStyleSheet(Pagination_Layer_Style)
        self.layerLayout = QVBoxLayout()
        self.layerLayout.addWidget(self.layer)
        self.setLayout(self.layerLayout)

        for i in range(self.amountPage + 1):
            if i == 0:
                self.arr.append("...")
            else:
                self.arr.append(i)

        self.container = QWidget(self.layer)
        self.container.setStyleSheet("background: transparent")
        self.containerLayout = QVBoxLayout()
        self.containerLayout.addWidget(self.container)
        self.containerLayout.setContentsMargins(32, 8, 32, 8)
        self.layer.setLayout(self.containerLayout)

        self.paginationComponentsLayout = QHBoxLayout()

        self.back = Arrow(self.layer, "Back")
        self.back.clicked.connect(lambda: self.changePage(self.currentPage - 1))
        self.paginationComponentsLayout.addWidget(self.back)
        self.paginationComponentsLayout.addStretch()

        self.pageNumberLayout = QHBoxLayout()
        self.pn1 = PageNumber(self.container, 0)
        self.pageNumberLayout.addWidget(self.pn1)
        self.pn2 = PageNumber(self.container, 0)
        self.pageNumberLayout.addWidget(self.pn2)
        self.pn3 = PageNumber(self.container, 0)
        self.pageNumberLayout.addWidget(self.pn3)
        self.pn4 = PageNumber(self.container, 0)
        self.pageNumberLayout.addWidget(self.pn4)
        self.pn5 = PageNumber(self.container, 0)
        self.pageNumberLayout.addWidget(self.pn5)
        self.pageNumberLayout.setSpacing(20)
        self.paginationComponentsLayout.addLayout(self.pageNumberLayout)
        self.paginationComponentsLayout.addStretch()

        self.next = Arrow(self.layer, "Next")
        self.next.clicked.connect(lambda: self.changePage(self.currentPage + 1))
        self.paginationComponentsLayout.addWidget(self.next)

        self.paginationComponentsLayout.setSpacing(20)
        self.container.setLayout(self.paginationComponentsLayout)

        self.signal = Checkbox(None)

        if self.amountPage <= 5:
            self.display(0)
        else:
            self.display(1)

    def display(self, template):

        self.checkArrow(self.next)
        self.checkArrow(self.back)

        if template == 0:
            self.pageArr = ["" for i in range(5 + 1)]
            for i in range(len(self.arr)):
                self.pageArr[i] = self.arr[i]
        elif template == 1:
            self.pageArr = ["...", 1, 2, 3, "...", self.amountPage]
        elif template == 2:
            self.pageArr = ["...", 1, "...", self.currentPage, "...", self.amountPage]
        elif template == 3:
            self.pageArr = ["...", 1, "...", self.amountPage - 2, self.amountPage - 1, self.amountPage]

        self.pn1.changeNum(str(self.pageArr[1]))
        if self.currentPage == self.pageArr[1] and self.pageArr[1] != "":
            self.pn1.setCurrent()
        else:
            self.pn1.setNotCurrent()

        try:
            self.pn1.clicked.disconnect()
        except Exception:
            pass
        self.pn1.clicked.connect(lambda: self.changePage(self.pageArr[1]))

        self.pn2.changeNum(str(self.pageArr[2]))
        if self.currentPage == self.pageArr[2] and self.pageArr[2] != "":
            self.pn2.setCurrent()
        else:
            self.pn2.setNotCurrent()

        try:
            self.pn2.clicked.disconnect()
        except Exception:
            pass
        self.pn2.clicked.connect(lambda: self.changePage(self.pageArr[2]))

        self.pn3.changeNum(str(self.pageArr[3]))
        if self.currentPage == self.pageArr[3] and self.pageArr[3] != "":
            self.pn3.setCurrent()
        else:
            self.pn3.setNotCurrent()

        try:
            self.pn3.clicked.disconnect()
        except Exception:
            pass
        self.pn3.clicked.connect(lambda: self.changePage(self.pageArr[3]))

        self.pn4.changeNum(str(self.pageArr[4]))
        if self.currentPage == self.pageArr[4] and self.pageArr[4] != "":
            self.pn4.setCurrent()
        else:
            self.pn4.setNotCurrent()

        try:
            self.pn4.clicked.disconnect()
        except Exception:
            pass
        self.pn4.clicked.connect(lambda: self.changePage(self.pageArr[4]))

        self.pn5.changeNum(str(self.pageArr[5]))
        if self.currentPage == self.pageArr[5] and self.pageArr[5] != "":
            self.pn5.setCurrent()
        else:
            self.pn5.setNotCurrent()

        try:
            self.pn5.clicked.disconnect()
        except Exception:
            pass
        self.pn5.clicked.connect(lambda: self.changePage(self.pageArr[5]))

    def checkArrow(self, arrow):
        if arrow.val == "Back":
            if self.currentPage == 1:
                arrow.setDisabled()
            else:
                arrow.setEnabled()
        else:
            if self.currentPage == self.amountPage:
                arrow.setDisabled()
            else:
                arrow.setEnabled()

    def changePage(self, num):
        if str(num) != "" and str(num) != "..." and num != self.currentPage and 1 <= num <= self.amountPage:
            self.currentPage = num
            if self.signal.isChecked():
                self.signal.setChecked(False)
            else:
                self.signal.setChecked(True)
            if self.amountPage <= 5:
                self.display(0)
            else:
                if self.currentPage <= 3:
                    self.display(1)
                elif self.currentPage >= self.amountPage - 2:
                    self.display(3)
                else:
                    self.display(2)

        if self.onChangePage is not None:
            self.onChangePage(num)

    def displayArr(self):
        for i in range(self.amountPage + 1):
            print(self.arr[i].getNum(), end=" | ")

    def getCurrentPage(self):
        return self.currentPage

    def getSignal(self):
        return self.signal
