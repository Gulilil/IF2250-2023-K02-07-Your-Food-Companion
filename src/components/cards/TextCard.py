"""Text Card with Title and List Content"""

from PyQt6.QtGui import QMouseEvent
from PyQt6.QtWidgets import QWidget, QHBoxLayout, QVBoxLayout, QLabel


class CardItem(QWidget):
    def __init__(self, description, title="", parent=None, *args, **kwargs):
        super(CardItem, self).__init__(parent)

        container = QWidget()
        container.setStyleSheet(
            """
            background-color: #3D4247;
            border-radius: 16px;
            """
        )
        containerLayout = QHBoxLayout()
        self.setLayout(containerLayout)

        itemTitle = QLabel(title)
        itemTitle.setStyleSheet(
            """
            color: #F2F3F5;
            font-size: 20px;
            """
        )

        itemDescription = QLabel(description)
        itemDescription.setStyleSheet(
            """
            font-weight: 400;
            font-size: 14px;
            line-height: 16px;
            color: #D4D7DC;
            """
        )

        textLayout = QVBoxLayout()
        textLayout.addWidget(itemTitle)
        textLayout.addWidget(itemDescription)

        container.setLayout(textLayout)
        containerLayout.addWidget(container)
        self.layout().setContentsMargins(0, 0, 0, 0)


class TextCard(QWidget):
    def __init__(self, title="", listItems: list[tuple[str, str]] = [], parent=None, *args, **kwargs):
        super().__init__(parent)
        self.setAutoFillBackground(True)

        # palette = self.palette()
        # palette.setColor(QPalette.ColorRole.Window, QColor('#2F3136'))
        # self.setPalette(palette)

        cardLayout = QVBoxLayout(self)

        titleText = QLabel(title)
        titleText.setStyleSheet("""
          font-size: 24px;
          font-style: normal;
          font-weight: 700;
          color: white;
        """)

        seeAll = QLabel("See All")
        seeAll.setStyleSheet("""
          font-size: 20px;
          font-style: normal;
          font-weight: 500;
          color: white;
        """)
        seeAll.mousePressEvent = self.onClickSeeAll

        titleLayout = QHBoxLayout()
        titleLayout.addWidget(titleText)
        titleLayout.addStretch()
        titleLayout.addWidget(seeAll)
        titleLayout.setContentsMargins(5, 0, 5, 0)

        itemLayout = QVBoxLayout()
        items: list[CardItem] = []
        for listItem in listItems:
            cardItem = CardItem(title=listItem[0], description=listItem[1])
            items.append(cardItem)
            itemLayout.addWidget(cardItem)

        cardLayout.addLayout(titleLayout)
        cardLayout.addLayout(itemLayout)
        cardLayout.addStretch()

        self.setLayout(cardLayout)
        self.layout().setContentsMargins(24, 32, 24, 32)

    def onClickSeeAll(self, a0: QMouseEvent):
        print("see all is clicked")
