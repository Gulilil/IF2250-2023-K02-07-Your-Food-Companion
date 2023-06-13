"""Image Card with Image Title Desc Content"""

from PyQt6.QtGui import QPalette, QColor, QMouseEvent
from PyQt6.QtWidgets import QWidget, QVBoxLayout, QLabel


class ImageCard(QWidget):
    def __init__(self, title="", description="", parent=None, *args, **kwargs):
        super(ImageCard, self).__init__(parent)

        self.isSelected = False

        self.container = QWidget()
        self.container.setObjectName("imageCardContainer")
        self.container.setStyleSheet(
            """
            #imageCardContainer {
              background-color: #3D4247;
              border-radius: 16px;
            }
            """
        )

        palette = self.palette()
        palette.setColor(QPalette.ColorRole.Window, QColor('#2F3136'))
        self.setPalette(palette)

        titleText = QLabel(title)
        titleText.setStyleSheet(
            """
            font-size: 32px;
            font-style: normal;
            font-weight: 700;
            color: white;
            line-height: 20px;
            """
        )

        descText = QLabel(description)
        descText.setStyleSheet(
            """
            font-size: 24px;
            font-style: normal;
            font-weight: 400;
            color: white;
            """
        )

        cardLayout = QVBoxLayout()
        cardLayout.setContentsMargins(24, 24, 24, 24)
        cardLayout.addWidget(titleText)
        cardLayout.addStretch()
        cardLayout.addWidget(descText)

        self.container.setLayout(cardLayout)

        layout = QVBoxLayout()
        layout.addWidget(self.container)
        self.setLayout(layout)

        self.mousePressEvent = self.onClick

    def onClick(self, a0: QMouseEvent):
        if self.isSelected:
            self.container.setStyleSheet(
                """
                #imageCardContainer {
                  background-color: #3D4247;
                  border-radius: 16px;
                }
                """
            )
            self.isSelected = False
        else:
            self.container.setStyleSheet(
                """
                #imageCardContainer {
                  background-color: #3D4247;
                  border-radius: 16px;
                  border: 2.5px solid #F3B8FF;
                }
                """
            )
            self.isSelected = True
