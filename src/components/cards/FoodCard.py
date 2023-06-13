from PyQt6.QtCore import Qt
from PyQt6.QtGui import QFont
from PyQt6.QtWidgets import QLabel, QWidget, QVBoxLayout, QHBoxLayout
from PyQt6.QtWidgets import QSizePolicy

font = QFont("Karla")


class FoodCard(QWidget):
    def __init__(self, name, category, quantity, cost, expired, storing, parent=None):
        super(FoodCard, self).__init__(parent)

        # Initialize the main container
        container = QWidget()
        container.setObjectName("food-container")

        # Set the main layout
        container_layout = QVBoxLayout()
        self.setLayout(container_layout)

        # Set the card layout
        card_layout = QVBoxLayout()
        card_layout.setSpacing(0)

        # Set the top container
        top_container = QWidget()
        top_container.setFixedHeight(164)
        top_container.setStyleSheet("background-image: url(./assets/img/hero_bg.jpg); \
                             background-color: rgba(0, 0, 0, 150); \
                             border-top-left-radius: 16px; \
                             border-top-right-radius: 16px; \
                             background-position: center center; \
                             background-repeat: no-repeat;")

        # Set the top layout
        top_layout = QVBoxLayout()
        top_container.setLayout(top_layout)

        # Set the top labels
        # Container
        label_container = QWidget()
        label_container.setSizePolicy(QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Fixed)

        # Layout
        label_layout = QVBoxLayout()
        label_layout.setSpacing(8)
        label_container.setLayout(label_layout)

        # Title
        title = QLabel(name)
        title.setStyleSheet("font-weight: bold; font-size: 20px; color: #F2F3F5;")
        title.setFont(font)

        # Category
        category = QLabel(category)
        category.setStyleSheet("font-size: 14px; color: #F2F3F5;")
        category.setFont(font)

        # Add the title and category to the layout
        label_layout.addWidget(title)
        label_layout.addWidget(category)

        # Set the label container to the bottom of the top layout
        top_layout.addStretch(1)

        # Add the label container to the top layout
        top_layout.addWidget(label_container)

        # Set the bottom container
        bottom_container = QWidget()
        bottom_container.setStyleSheet(
            "background-color: #4D5259; border-bottom-left-radius: 16px; border-bottom-right-radius: 16px; padding: 4px;")

        # Set the bottom layout
        bottom_layout = QHBoxLayout()
        bottom_container.setLayout(bottom_layout)

        # Set the description labels
        # Quantity
        quantity_container = QWidget()
        quantity_container.setSizePolicy(QSizePolicy.Policy.Fixed, QSizePolicy.Policy.Fixed)
        quantity_layout = QVBoxLayout()
        quantity_layout.setAlignment(Qt.AlignmentFlag.AlignCenter)
        quantity_title = QLabel("Quantity")
        quantity_title.setStyleSheet("font-weight: bold; font-size: 16px; color: #F2F3F5;")
        quantity_name = QLabel(str(quantity))
        quantity_name.setStyleSheet("font-size: 16px; color: #F2F3F5;")
        quantity_layout.addWidget(quantity_title)
        quantity_layout.addWidget(quantity_name)
        quantity_container.setSizePolicy(QSizePolicy.Policy.Fixed, QSizePolicy.Policy.Fixed)
        quantity_container.setLayout(quantity_layout)

        # Cost
        cost_container = QWidget()
        cost_container.setSizePolicy(QSizePolicy.Policy.Fixed, QSizePolicy.Policy.Fixed)
        cost_layout = QVBoxLayout()
        cost_layout.setAlignment(Qt.AlignmentFlag.AlignCenter)
        cost_title = QLabel("Cost")
        cost_title.setStyleSheet("font-weight: bold; font-size: 16px; color: #F2F3F5;")
        cost_name = QLabel(str(cost))
        cost_name.setStyleSheet("font-size: 16px; color: #F2F3F5;")
        cost_layout.addWidget(cost_title)
        cost_layout.addWidget(cost_name)
        cost_container.setSizePolicy(QSizePolicy.Policy.Fixed, QSizePolicy.Policy.Fixed)
        cost_container.setLayout(cost_layout)

        # Expired due
        expired_container = QWidget()
        expired_container.setSizePolicy(QSizePolicy.Policy.Fixed, QSizePolicy.Policy.Fixed)
        expired_layout = QVBoxLayout()
        expired_layout.setAlignment(Qt.AlignmentFlag.AlignCenter)
        expired_title = QLabel("Expired due")
        expired_title.setStyleSheet("font-weight: bold; font-size: 16px; color: #F2F3F5;")
        expired_name = QLabel(str(expired))
        expired_name.setStyleSheet("font-size: 16px; color: #F2F3F5;")
        expired_layout.addWidget(expired_title)
        expired_layout.addWidget(expired_name)
        expired_container.setSizePolicy(QSizePolicy.Policy.Fixed, QSizePolicy.Policy.Fixed)
        expired_container.setLayout(expired_layout)

        # Storing
        storing_container = QWidget()
        storing_container.setSizePolicy(QSizePolicy.Policy.Fixed, QSizePolicy.Policy.Fixed)
        storing_layout = QVBoxLayout()
        storing_layout.setAlignment(Qt.AlignmentFlag.AlignCenter)
        storing_title = QLabel("Storing Place")
        storing_title.setStyleSheet("font-weight: bold; font-size: 16px; color: #F2F3F5;")
        storing_name = QLabel(str(storing))
        storing_name.setStyleSheet("font-size: 16px; color: #F2F3F5;")
        storing_layout.addWidget(storing_title)
        storing_layout.addWidget(storing_name)
        storing_container.setSizePolicy(QSizePolicy.Policy.Fixed, QSizePolicy.Policy.Fixed)
        storing_container.setLayout(storing_layout)

        # Add the item description to the bottom layout
        bottom_layout.addWidget(quantity_container)
        bottom_layout.addWidget(cost_container)
        bottom_layout.addWidget(expired_container)
        bottom_layout.addWidget(storing_container)

        # Add the containers to the card layout
        card_layout.addWidget(top_container)
        card_layout.addWidget(bottom_container)

        # Add the card layout to the container layout
        container.setLayout(card_layout)
        container_layout.addWidget(container)
