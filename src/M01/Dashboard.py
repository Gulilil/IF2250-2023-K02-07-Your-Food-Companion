""" Dashboard Module """

from PyQt6.QtCore import Qt
from PyQt6.QtGui import QFont
from PyQt6.QtWidgets import QLabel, QScrollArea
from PyQt6.QtWidgets import QPushButton
from PyQt6.QtWidgets import QVBoxLayout, QHBoxLayout, QSizePolicy
from PyQt6.QtWidgets import QWidget

from src.components.cards.FoodCard import FoodCard
from src.components.cards.HeroCard import HeroCard
from src.components.cards.SummaryCard import SummaryCard
from src.controller.controller import Controller

font = QFont("Karla")


class Dashboard(QWidget):
    width = 0
    height = 0

    def __init__(self):
        super(Dashboard, self).__init__()

        # Making widget item for the class
        self.layer = QWidget(self)
        self.layer.setStyleSheet("background-color: #36393F")

        # Every components in this page, please use "self.layer" as its parent
        # Because "self.layer" is the Widget that will be inserted into Stack in Main.py

        # Initialize the main layout
        self.main_layout = QVBoxLayout()
        self.main_layout.setContentsMargins(16, 16, 16, 16)
        self.main_layout.setAlignment(Qt.AlignmentFlag.AlignTop | Qt.AlignmentFlag.AlignLeft)

        # Set the top horizontal container and layout
        self.top_container = QWidget()
        self.top_layout = QHBoxLayout()
        self.top_layout.setContentsMargins(0, 0, 0, 0)
        self.top_container.setLayout(self.top_layout)
        self.top_container.setSizePolicy(QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Fixed)

        # Making hero (Left-top)
        hero = HeroCard("Welcome Back to Your Food Companion", "See how well you manage your food storing",
                        parent=self.layer)
        hero.setSizePolicy(QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Fixed)
        self.top_layout.addWidget(hero)
        hero.setFixedHeight(300)

        # Making table (Right-top)
        self.card = SummaryCard(parent=self.layer)
        self.card.setSizePolicy(QSizePolicy.Policy.Fixed, QSizePolicy.Policy.Expanding)
        self.top_layout.addWidget(self.card)

        # Set the bottom horizontal container and layout
        self.bottom_container = QWidget()
        self.bottom_layout = QVBoxLayout()
        self.bottom_layout.setContentsMargins(0, 0, 0, 0)
        self.bottom_container.setLayout(self.bottom_layout)

        # Set the bottom label layout
        bottom_label = QWidget(parent=self.layer)
        bottom_label.setSizePolicy(QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Fixed)
        bottom_label.setStyleSheet("padding-left: 12px; padding-right: 12px;")
        bottom_label_layout = QHBoxLayout()
        bottom_label_layout.setContentsMargins(0, 0, 0, 0)

        bottom_label_title = QLabel("Foods about to expire")
        bottom_label_title.setFont(font)
        bottom_label_title.setStyleSheet("color: #F2F3F5; font-size: 24px; font-weight: 600;")

        self.bottom_label_see_all = QPushButton("See all")
        self.bottom_label_see_all.setFont(font)
        self.bottom_label_see_all.setStyleSheet(
            '''
            QPushButton {
                color: #F2F3F5;
                font-size: 16px;
                font-weight: 600;
                border: none;
                
                }
                QPushButton:hover {
                    color: #7289DA;
                    font-size: 16px;
                    font-weight: 600;
                    border: none;
                }
                '''
        )
        self.bottom_label_see_all.setCursor(Qt.CursorShape.PointingHandCursor)

        bottom_label_layout.addWidget(bottom_label_title)
        bottom_label_layout.addStretch(1)
        bottom_label_layout.addWidget(self.bottom_label_see_all)

        bottom_label.setLayout(bottom_label_layout)
        self.bottom_layout.addWidget(bottom_label)

        # Set the bottom cards widget and layout
        bottom_cards_scroll = QScrollArea()
        bottom_cards_scroll.setVerticalScrollBarPolicy(Qt.ScrollBarPolicy.ScrollBarAlwaysOff)
        bottom_cards_scroll.setHorizontalScrollBarPolicy(Qt.ScrollBarPolicy.ScrollBarAlwaysOff)
        bottom_cards_scroll.setWidgetResizable(True)
        bottom_cards_scroll.setStyleSheet("background-color: #36393F; border: none;")

        bottom_cards = QWidget()

        self.bottom_cards_layout = QHBoxLayout()
        self.bottom_cards_layout.setSpacing(8)
        self.bottom_cards_layout.setAlignment(Qt.AlignmentFlag.AlignLeft | Qt.AlignmentFlag.AlignTop)
        bottom_cards.setLayout(self.bottom_cards_layout)
        self.bottom_cards_layout.setContentsMargins(0, 0, 0, 0)

        bottom_cards_scroll.setWidget(bottom_cards)
        self.bottom_layout.addWidget(bottom_cards_scroll)

        # Set the main layout
        self.main_layout.addWidget(self.top_container)
        self.main_layout.addSpacing(16)
        self.main_layout.addWidget(self.bottom_container)

        self.layer.setLayout(self.main_layout)

    def addFoodItemCard(self, name, category, quantity, cost, expired, storing):
        bottom_card_item = FoodCard(name, category, quantity, cost, expired, storing, parent=self.layer)
        bottom_card_item.setSizePolicy(QSizePolicy.Policy.Fixed, QSizePolicy.Policy.Fixed)
        self.bottom_cards_layout.addWidget(bottom_card_item)

    def setFoodItemCard(self):
        ctrl = Controller()
        stale = ctrl.get_good_food()

        for idx, food in enumerate(stale):
            if idx == 5:
                break

            name = food[len(food) - 2]
            category = food[len(food) - 1]
            quantity = food[1]
            cost = food[3]
            expired = food[4]
            storing = food[5]

            self.addFoodItemCard(name, category, quantity, cost, expired, storing)

    def getWidget(self):
        return self.layer

    def get_hero_button(self):
        return self.top_layout.itemAt(0).widget().get_button()

    def get_see_all_button(self):
        return self.bottom_label_see_all, self.card.see_all_summary()
