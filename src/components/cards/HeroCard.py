from PyQt6.QtGui import QFont
from PyQt6.QtWidgets import QLabel, QWidget, QVBoxLayout, QHBoxLayout
from PyQt6.QtWidgets import QSizePolicy

from src.components.buttons.Button import Button


class HeroCard(QWidget):
    def __init__(self, title="", description="", parent=None):
        super(HeroCard, self).__init__(parent)

        # Set the container for the card
        container = QWidget()
        container.setObjectName("hero-container")
        container.setStyleSheet(
            '''
            #hero-container {
                background-image: url(./assets/img/hero_bg.jpg);
                border-radius: 16px;
            }
            * {
                background-color: transparent;
            }
            '''
        )

        # Set the main layout
        container_layout = QHBoxLayout()
        self.setLayout(container_layout)

        # Set the card title
        card_title = QLabel(title)
        card_title.setFont(QFont("Karla"))
        card_title.setStyleSheet(
            "color: #F2F3F5; font-size: 24px; font-weight: 600;"
        )

        # Set the card subtitle
        card_subtitle = QLabel("Explore and keep track on your food waste")
        card_subtitle.setFont(QFont("Karla"))
        card_subtitle.setStyleSheet(
            "color: #F2F3F5; font-size: 16px;"
        )

        # Set the card description
        card_description = QLabel(description)
        card_description.setFont(QFont("Karla"))
        card_description.setStyleSheet(
            "color: #F2F3F5; font-size: 16px; font-weight: 600;"
        )

        # Set the card subdescription
        card_subdescription = QLabel("Track your foods in the inventory")
        card_subdescription.setFont(QFont("Karla"))
        card_subdescription.setStyleSheet(
            "color: #F2F3F5; font-size: 16px;"
        )

        # Set the title container
        title_container = QWidget()
        title_container.setStyleSheet("margin-left: 4px;")
        title_container.setSizePolicy(QSizePolicy.Policy.Fixed, QSizePolicy.Policy.Fixed)

        # Set the title layout
        title_layout = QVBoxLayout()
        title_layout.addWidget(card_title)
        title_layout.addWidget(card_subtitle)
        title_layout.setSpacing(8)
        title_container.setLayout(title_layout)

        # Set the description container
        description_container = QWidget()
        description_container.setSizePolicy(QSizePolicy.Policy.Fixed, QSizePolicy.Policy.Fixed)

        # Set the description layout
        description_layout = QVBoxLayout()
        description_layout.addWidget(card_description)
        description_layout.addWidget(card_subdescription)
        description_layout.setSpacing(8)
        description_container.setLayout(description_layout)

        # Set the bottom container and layout
        bottom_container = QWidget()
        bottom_container.setSizePolicy(QSizePolicy.Policy.Fixed, QSizePolicy.Policy.Fixed)

        bottom_layout = QVBoxLayout()
        bottom_layout.addWidget(description_container)
        self.inventory_button = Button("See Inventory", "Small")
        self.inventory_button.setSizePolicy(QSizePolicy.Policy.Fixed, QSizePolicy.Policy.Fixed)
        bottom_layout.addWidget(self.inventory_button)
        bottom_layout.setSpacing(16)
        bottom_container.setLayout(bottom_layout)

        # Set the text layout
        text_layout = QVBoxLayout()
        text_layout.addWidget(title_container)
        text_layout.addWidget(bottom_container)

        # Set the spacing between title and description
        self.setSizePolicy(QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Fixed)
        text_layout.setSpacing(32)

        # Set container layout
        container.setLayout(text_layout)
        container_layout.addWidget(container)
        self.layout().setContentsMargins(0, 0, 0, 0)

    def set_hero(self, title_text, description_text):
        # Set the title for the card
        self.title.setText(title_text)

        # Set the description for the card
        self.description.setText(description_text)

    def get_button(self):
        return self.inventory_button
