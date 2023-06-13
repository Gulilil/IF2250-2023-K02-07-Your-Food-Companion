""" Food Inventory Module """

from PyQt6.QtWidgets import QWidget, QVBoxLayout, QHBoxLayout, QScrollArea, QSizePolicy
from PyQt6.QtGui import QFont
from PyQt6.QtCore import Qt
from .GraphWidget import GraphWidget
from .ReportTextCard import ReportTextCard
from src.controller.controller import Controller
from .ConsumptionCard import ConsumptionTextCard

notifications = [
    ("Added Pizza on Food Inventory", "Inventory", "15 Febuary 09.15"),
    ("Added Nasi Padang on Shopping List", "Shopping List", "15 Febuary 10.15"),
    ("Bread went Stale", "Inventory", "17 Febuary 8.25"),
    ("Apple Expired", "Inventory", "20 Febuary 13.00")
]


class Report(QWidget):
    def __init__ (self):
        super(Report, self).__init__()

        controller = Controller()
        
        scrollable = QScrollArea()
        scrollable.setObjectName("scrollable-report")
        scrollable.setStyleSheet(
            """
            #scrollable-report {
                border: 1px solid #36393F;
            }
            """)
        scrollable.setContentsMargins(0,0,0,0)
        scrollable.horizontalScrollBar().setStyleSheet("QScrollBar {height:0px;}")
        scrollable.verticalScrollBar().setStyleSheet("QScrollBar {width:0px;}")
        scrollable.setVerticalScrollBarPolicy(Qt.ScrollBarPolicy.ScrollBarAlwaysOn)
        scrollable.setHorizontalScrollBarPolicy(Qt.ScrollBarPolicy.ScrollBarAlwaysOff)
        scrollable.setWidgetResizable(True)

        # Making widget item for the class
        layer = QWidget(self)
        scrollable.setWidget(layer)
        layer.setStyleSheet("background-color: #36393F")
        layerContainer = QVBoxLayout()
        layerContainer.setContentsMargins(0,0,0,0)
        layerContainer.addWidget(scrollable)
        self.setLayout(layerContainer)

        # Every components in this page, please use "self.layer" as its parent
        # Because "self.layer" is the Widget that will be inserted into Stack in Main.py

        contentLayout = QVBoxLayout()
        contentLayout.setContentsMargins(62,40,62,40)
        contentLayout.setSpacing(32)
        layer.setLayout(contentLayout)

        graphWidget = GraphWidget(controller=controller)
        contentLayout.addWidget(graphWidget)

        bottomLayout = QHBoxLayout()
        bottomLayout.setContentsMargins(0,0,0,0)
        bottomLayout.setSpacing(32)
        contentLayout.addLayout(bottomLayout)

        notificationCard = ReportTextCard(title="Recent Updates", listItems=notifications)
        notificationCard.setSizePolicy(QSizePolicy.Policy.Fixed, QSizePolicy.Policy.Expanding)
        bottomLayout.addWidget(notificationCard)

        consumptionCard = ConsumptionTextCard(title="Average Monthly Consumption", controller=controller)
        consumptionCard.setSizePolicy(QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Expanding)
        bottomLayout.addWidget(consumptionCard)