""" All Food Hero """

""" Inventory Searchbar """

from PyQt6.QtWidgets import QWidget, QLabel, QSizePolicy, QVBoxLayout, QHBoxLayout
from PyQt6.QtGui import QFont, QColor, QPalette, QLinearGradient
from PyQt6.QtCore import Qt

# Global Variabel Font
font = QFont("Karla", 11)
font.setWeight(600)
percentFont = QFont("Karla", 16)
percentFont.setWeight(600)


class AllFoodHero(QWidget):
    goodPercent = 70.678
    stalePercent = 45.45
    expiredPercent = 23.562

    def __init__(self, parent):
        super(AllFoodHero, self).__init__(parent)

        self.setSizePolicy(QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Fixed)

        self.layer = QWidget(self)
        self.layer.setStyleSheet("background-color: #3D4247; color:white")
        self.layer.setObjectName("hero-layer")
        layerContainer = QVBoxLayout()
        layerContainer.addWidget(self.layer)
        self.setLayout(layerContainer)

        contentLayout = QHBoxLayout()
        self.layer.setLayout(contentLayout)

        # self.layer.setStyleSheet(
        #     """
        #     #hero-layer {
        #         background-color: qlineargradient(x1: 0, x2: 1, stop: 0 white, stop: 1 #3D4247);
        #         color:white;
        #     }
        #     * {
        #         background-color: transparent;
        #     }
        #     """
        #     )
        # pal = QPalette()
        # gradient = QLinearGradient(0,0,0,400)
        # gradient.setColorAt(0.0, QColor(255,255,255))
        # gradient.setColorAt(1.0, QColor(255, 160, 160))
        # self.layer.setPalette(pal)

        self.containerLayout1 = QVBoxLayout()
        self.containerLayout1.setSpacing(32)
        self.container1 = QWidget(self.layer)
        self.container1.setLayout(self.containerLayout1)
        self.goodLabel = QLabel(self.container1)
        self.goodLabel.setText(str(round(self.goodPercent, 1)) + "%")
        self.goodLabel.setFont(percentFont)
        self.goodLabel.setStyleSheet("color: #67FF5A")
        self.goodLabel.setAlignment(Qt.AlignmentFlag.AlignCenter)
        self.containerLayout1.addWidget(self.goodLabel)
        self.label1 = QLabel(self.container1)
        self.label1.setText("Good")
        self.label1.setFont(font)
        self.label1.setAlignment(Qt.AlignmentFlag.AlignCenter)
        self.containerLayout1.addWidget(self.label1)
        contentLayout.addWidget(self.container1)

        self.containerLayout2 = QVBoxLayout()
        self.containerLayout2.setSpacing(32)
        self.container2 = QWidget(self.layer)
        self.container2.setLayout(self.containerLayout2)
        self.staleLabel = QLabel(self.container2)
        self.staleLabel.setText(str(round(self.stalePercent, 1)) + "%")
        self.staleLabel.setFont(percentFont)
        self.staleLabel.setStyleSheet("color: #FFC700")
        self.staleLabel.setAlignment(Qt.AlignmentFlag.AlignCenter)
        self.containerLayout2.addWidget(self.staleLabel)
        self.label2 = QLabel(self.container2)
        self.label2.setText("Stale")
        self.label2.setFont(font)
        self.label2.setAlignment(Qt.AlignmentFlag.AlignCenter)
        self.containerLayout2.addWidget(self.label2)
        contentLayout.addWidget(self.container2)

        self.containerLayout3 = QVBoxLayout()
        self.containerLayout3.setSpacing(32)
        self.container3 = QWidget(self.layer)
        self.container3.setLayout(self.containerLayout3)
        self.expiredLabel = QLabel(self.container3)
        self.expiredLabel.setText(str(round(self.expiredPercent, 1)) + "%")
        self.expiredLabel.setFont(percentFont)
        self.expiredLabel.setStyleSheet("color: #E66D57")
        self.expiredLabel.setAlignment(Qt.AlignmentFlag.AlignCenter)
        self.containerLayout3.addWidget(self.expiredLabel)
        self.label3 = QLabel(self.container3)
        self.label3.setText("Expired")
        self.label3.setFont(font)
        self.label3.setAlignment(Qt.AlignmentFlag.AlignCenter)
        self.containerLayout3.addWidget(self.label3)
        contentLayout.addWidget(self.container3)

    def getGoodLabel(self):
        return self.goodLabel

    def getStaleLabel(self):
        return self.staleLabel

    def getExpiredLabel(self):
        return self.expiredLabel

    def setGoodPercentage(self, n):
        self.goodPercent = n
        self.goodLabel.setText(str(round(self.goodPercent, 1)) + "%")

    def setStalePercentage(self, n):
        self.stalePercent = n
        self.staleLabel.setText(str(round(self.stalePercent, 1)) + "%")

    def setExpiredPercentage(self, n):
        self.expiredPercent = n
        self.expiredLabel.setText(str(round(self.expiredPercent, 1)) + "%")
