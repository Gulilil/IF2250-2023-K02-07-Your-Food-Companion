"""Text Card with Title and List Content"""

from PyQt6.QtWidgets import QWidget, QHBoxLayout, QVBoxLayout, QLabel
from PyQt6.QtGui import QPalette, QColor, QFont

font = (QFont("Karla", 14))

class ReportCardItem(QWidget):
    def __init__(self,  title="", category="", time="", parent=None, *args, **kwargs):
        super(ReportCardItem, self).__init__(parent)

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
        itemTitle.setFont(font)
        itemTitle.setStyleSheet(
            """
            color: #F2F3F5;
            font-size: 20px;
            """
        )

        categoryLabel = QLabel(category + " • " + time)
        categoryLabel.setFont(font)
        categoryLabel.setStyleSheet(
            """
            font-weight: 400;
            font-size: 14px;
            line-height: 16px;
            color: #D4D7DC;
            """
        )

        textLayout = QVBoxLayout()
        textLayout.addWidget(itemTitle)
        textLayout.addWidget(categoryLabel)
        textLayout.setSpacing(16)

        container.setLayout(textLayout)
        containerLayout.addWidget(container)
        self.layout().setContentsMargins(0,0,0,0)

class ReportTextCard(QWidget):
    def __init__(self, title="", listItems: list[tuple[str, str, str]] = [], parent=None, *args, **kwargs):
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

        titleLayout = QHBoxLayout()
        titleLayout.addWidget(titleText)
        titleLayout.addStretch()
        titleLayout.setContentsMargins(5, 0, 5, 0)

        itemLayout = QVBoxLayout()
        items: list[ReportCardItem] = []
        for i in range(min(4, len(listItems))):
          listItem = listItems[i]
          cardItem = ReportCardItem(title=listItem[0], category=listItem[1], time=listItem[2])
          items.append(cardItem)
          itemLayout.addWidget(cardItem)

        cardLayout.addLayout(titleLayout)
        cardLayout.addLayout(itemLayout)
        cardLayout.addStretch()
        cardLayout.setSpacing(20)

        container.setLayout(cardLayout)
        self.setLayout(containerLayout)