from PyQt6.QtGui import QFont
from PyQt6.QtWidgets import QWidget, QHBoxLayout, QVBoxLayout, QLabel, QPushButton

from src.controller.controller import Controller

font = (QFont("Karla", 14))


class SummaryItem(QWidget):
    def __init__(self, title="", desc="", parent=None):
        super(SummaryItem, self).__init__(parent)

        container = QWidget()
        container.setStyleSheet(
            '''
                background: #3D4247;
                border-radius: 16px;
                padding: 4px;
            '''
        )

        containerLayout = QHBoxLayout()
        self.setLayout(containerLayout)

        itemTitle = QLabel(title)
        itemTitle.setFont(font)
        itemTitle.setStyleSheet("color: #F2F3F5; font-size: 16px;")
        itemTitle.setContentsMargins(0, 0, 0, 0)

        itemDesc = QLabel(desc)
        itemDesc.setFont(font)
        itemDesc.setStyleSheet("color: #F2F3F5; font-size: 16px;")
        itemDesc.setContentsMargins(0, 0, 0, 0)

        textLayout = QHBoxLayout()
        textLayout.addWidget(itemTitle)
        textLayout.addStretch()
        textLayout.addWidget(itemDesc)
        textLayout.setSpacing(16)

        container.setLayout(textLayout)
        containerLayout.addWidget(container)
        self.layout().setContentsMargins(0, 0, 0, 0)


class SummaryCard(QWidget):
    def __init__(self, title="Summary", parent=None):
        super(SummaryCard, self).__init__(parent)

        container = QWidget()
        self.setContentsMargins(0, 0, 0, 0)
        container.setStyleSheet("background-color: #2F3136; border-radius: 16px;")

        containerLayout = QVBoxLayout()
        containerLayout.addWidget(container)

        titleContainer = QWidget()
        titleLabel = QLabel(title)
        titleLabel.setFont(font)
        titleLabel.setStyleSheet("color: #F2F3F5; font-size: 20px; font-weight: 600;")
        self.seeAll = QPushButton("See all")
        self.seeAll.setFont(font)
        self.seeAll.setStyleSheet(
            '''
            QPushButton {
                color: #F2F3F5;
                font-size: 14px;
                font-weight: 600;
                border: none;
                
                }
                QPushButton:hover {
                    color: #7289DA;
                    font-size: 14px;
                    font-weight: 600;
                    border: none;
                }
                '''
        )

        titleLayout = QHBoxLayout()
        titleLayout.addWidget(titleLabel)
        titleLayout.addStretch()
        titleLayout.addWidget(self.seeAll)
        titleLayout.setSpacing(16)
        titleContainer.setLayout(titleLayout)

        ctrl = Controller()
        foods = ctrl.get_stored_food().fetchall()
        expired = ctrl.get_expired_food().fetchall()
        shoplist = ctrl.get_grocery_food().fetchall()
        stale = ctrl.get_stale_food().fetchall()

        cardLayout = QVBoxLayout()
        totalFood = SummaryItem("Total Food", str(len(foods)))
        totalStale = SummaryItem("Total Stale", str(len(stale)))
        totalExpired = SummaryItem("Total Expired", str(len(expired)))
        totalShopList = SummaryItem("Total Food in Shopping List", str(len(shoplist)))
        cardLayout.addWidget(titleContainer)
        cardLayout.addWidget(totalFood)
        cardLayout.addWidget(totalStale)
        cardLayout.addWidget(totalExpired)
        cardLayout.addWidget(totalShopList)
        cardLayout.setSpacing(16)
        container.setLayout(cardLayout)

        self.setLayout(containerLayout)

    def see_all_summary(self):
        return self.seeAll
