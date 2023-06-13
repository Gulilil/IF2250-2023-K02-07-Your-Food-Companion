"""Text Card with Title and List Content"""

from PyQt6.QtWidgets import QWidget, QHBoxLayout, QVBoxLayout, QLabel
from PyQt6.QtGui import QPalette, QColor, QFont
from src.controller.controller import Controller

font = (QFont("Karla", 14))

class ConsumptionCardItem(QWidget):
    def __init__(self,  title="", amount: int=0, parent=None, *args, **kwargs):
        super(ConsumptionCardItem, self).__init__(parent)

        container = QWidget()
        container.setStyleSheet(
            """
            background-color: #3D4247;
            border-radius: 16px;
            """
        )
        container.setContentsMargins(14,11,14,11)
        containerLayout = QHBoxLayout()
        self.setLayout(containerLayout)

        itemTitle = QLabel(title)
        itemTitle.setFont(font)
        itemTitle.setStyleSheet(
            """
            color: #F2F3F5;
            font-size: 20px;
            """
        )

        amountLabel = QLabel(str(amount))
        amountLabel.setFont(font)
        amountLabel.setStyleSheet(
            """
            font-weight: 400;
            font-size: 20px;
            line-height: 16px;
            color: #D4D7DC;
            """
        )

        textLayout = QHBoxLayout()
        textLayout.addWidget(itemTitle)
        textLayout.addStretch()
        textLayout.addWidget(amountLabel)

        container.setLayout(textLayout)
        containerLayout.addWidget(container)
        self.layout().setContentsMargins(0,0,0,0)

class ConsumptionTextCard(QWidget):
    def __init__(self, title="", controller: Controller= None, parent=None, *args, **kwargs):
        super().__init__(parent)

        container = QWidget()
        self.setContentsMargins(0,0,0,0)
        container.setContentsMargins(0,0,0,0)
        container.setStyleSheet("background-color: #2F3136;border-radius: 16px;margin: 0;")
        containerLayout = QVBoxLayout()
        containerLayout.setContentsMargins(0,0,0,0)
        containerLayout.addWidget(container)

        cardLayout = QVBoxLayout(self)
        cardLayout.setContentsMargins(24, 32, 24, 32)

        titleText = QLabel(title)
        titleText.setStyleSheet("""
          font-size: 24px;
          font-style: normal;
          font-weight: 700;
          color: white;
        """)

        amountText = QLabel("Amount")
        amountText.setStyleSheet("""
          font-size: 20px;
          font-style: normal;
          font-weight: 400;
          color: #D4D7DC;
        """)

        titleLayout = QHBoxLayout()
        titleLayout.addWidget(titleText)
        titleLayout.addStretch()
        titleLayout.addWidget(amountText)
        titleLayout.setContentsMargins(5, 0, 5, 0)


        itemLayout = QVBoxLayout()
        categories: list[ConsumptionCardItem] = []

        catQuery = controller.get_distinct_category()
        for cat in catQuery:
            categories.append(cat[0])

        for category in categories:
            amountQuery = controller.get_eaten_food_count_with_category_this_month(category)
            amount = 0
            for res in amountQuery:
                amount = res[0]
                if amount == None:
                    amount = 0
            cardItem = ConsumptionCardItem(title=category, amount=amount)
            itemLayout.addWidget(cardItem)

        cardLayout.addLayout(titleLayout)
        cardLayout.addLayout(itemLayout)
        cardLayout.addStretch()
        cardLayout.setSpacing(20)

        container.setLayout(cardLayout)
        self.setLayout(containerLayout)