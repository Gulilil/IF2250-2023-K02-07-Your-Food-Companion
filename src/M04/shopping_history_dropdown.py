from PyQt6.QtGui import QFont

from src.components.fields.Dropdown import Dropdown
from src.controller.controller import Controller


class ShoppingHistoryDropdown(Dropdown):
    font = QFont("Karla", 11)
    font.setWeight(600)

    def __init__(self, parent):
        super().__init__(parent)

        self.categories = []

        self.setFont(ShoppingHistoryDropdown.font)

        # self.setPlaceholderText('All Categories')
        # self.activated.connect(self.reset_categories)

        self.reset_categories()

    def reset_categories(self) -> None:
        self.remove_categories()
        self.get_categories()

        for i in range(len(self.categories)):
            self.addItem(self.categories[i])

    def remove_categories(self) -> None:
        # Remove all categories in the dropdown except "All Categories"
        self.clear()
        self.categories = []

    def get_categories(self) -> None:
        # Get all distinct categories from the database
        controller = Controller()
        temp = controller.get_distinct_category()
        self.categories = ['All Categories']  # "All Categories" will always be present

        for i in temp:
            self.categories.append(i[0])
