from PyQt6.QtGui import QFont
from PyQt6.QtWidgets import QWidget, QVBoxLayout, QHBoxLayout

from src.M04.shopping_history_dropdown import ShoppingHistoryDropdown
from src.M04.shopping_history_search_bar import ShoppingHistorySearchBar
from src.components.buttons.Button import Button
from src.components.pagination.Pagination import Pagination
from src.components.table.Table import Table
from src.controller.controller import Controller

SHOPPING_HISTORY_CONTAINER_LAYER_STYLE = """
    background-color: #2F3136;
    border-radius: 10px;
"""

TABLE_HEADER = ['Food Name', 'Quantity', 'Purchase Date']


class ShoppingHistoryContainer(QWidget):
    font = QFont("Karla", 11)
    font.setWeight(600)

    def __init__(self, parent):
        super().__init__(parent)

        # Making layer
        self.layer = QWidget(self)
        self.layer.setStyleSheet(SHOPPING_HISTORY_CONTAINER_LAYER_STYLE)
        self.layer.setContentsMargins(0, 0, 0, 0)

        # Setup layout for ShoppingHistoryContainer
        self.layer_layout = QVBoxLayout()
        self.layer_layout.addWidget(self.layer)
        self.layer_layout.setContentsMargins(0, 0, 0, 0)
        self.layer_layout.setSpacing(0)
        self.setLayout(self.layer_layout)

        # Setup layout for contents of ShoppingHistoryContainer
        self.content_layout = QVBoxLayout()
        self.content_layout.setContentsMargins(10, 10, 10, 10)
        self.content_layout.setSpacing(0)
        self.layer.setLayout(self.content_layout)

        # Header layout contains dropdown and search_bar
        self.header_layout = QHBoxLayout()
        self.dropdown = ShoppingHistoryDropdown(self.layer)
        self.dropdown.currentTextChanged.connect(lambda: self.change_dropdown_category(self.dropdown.currentText()))
        self.search_bar = ShoppingHistorySearchBar(self.layer)
        self.search_bar.get_search_button().clicked.connect(lambda: self.search_food())
        self.header_layout.addSpacing(41)
        self.header_layout.addWidget(self.dropdown)
        self.header_layout.addStretch()
        self.header_layout.addWidget(self.search_bar)
        self.header_layout.addSpacing(17)
        self.content_layout.addLayout(self.header_layout)

        self.data = get_purchased_food_data()
        self.set_up_table_and_pagination()

    def set_up_table_and_pagination(self) -> None:
        # Set up the shopping history table
        number_of_rows = 8
        number_of_pages = ((len(self.data) - 1) // number_of_rows) + 1

        data_in_table = []
        for row in self.data:
            data_in_table.append(row[1:])

        table_pagination = Pagination(self.layer, number_of_pages)
        table = Table(data=data_in_table,
                      pagination=table_pagination,
                      rowsPerPage=number_of_rows,
                      headers=TABLE_HEADER,
                      useCheckbox=True)

        button_layout = QHBoxLayout()
        button_layout.setContentsMargins(10, 10, 10, 10)
        button_layout.setSpacing(0)

        delete_from_history_button = Button(self.layer, "Small")
        delete_from_history_button.resize(200, 45)
        delete_from_history_button.setText("Delete from History")
        delete_from_history_button.clicked.connect(lambda: self.delete_purchased_food())
        button_layout.addStretch()
        button_layout.addWidget(delete_from_history_button)
        button_layout.addSpacing(10)

        self.content_layout.addWidget(table)
        self.content_layout.addWidget(table_pagination)
        self.content_layout.addLayout(button_layout)

    def change_dropdown_category(self, category: str) -> None:
        if category == "All Categories":
            self.data = get_purchased_food_data()
        else:
            self.data = get_purchased_food_data(category=category)

        self.reset_table_and_pagination()

    def reset_table_and_pagination(self) -> None:
        # remove the previous table and pagination
        prev_table = self.content_layout.itemAt(1).widget()
        prev_table.deleteLater()
        prev_pagination = self.content_layout.itemAt(2).widget()
        prev_pagination.deleteLater()
        button_layout = self.content_layout.itemAt(3).layout()
        button_layout.deleteLater()

        self.set_up_table_and_pagination()

    def search_food(self) -> None:
        category = self.dropdown.currentText()
        keyword = self.search_bar.get_content()

        if category == "All Categories":
            temp_data = get_purchased_food_data()
        else:
            temp_data = get_purchased_food_data(category)

        self.data = []

        for temp_row_data in temp_data:
            if keyword in temp_row_data[1]:
                self.data.append(temp_row_data)

        self.reset_table_and_pagination()

    def delete_purchased_food(self) -> None:
        checked_indices = self.content_layout.itemAt(1).widget().getCheckedIndexes()
        data_want_to_be_removed = []  # only contains IDs

        for index in checked_indices:
            data_want_to_be_removed.append(self.data[index][0])

        self.data = [x for i, x in enumerate(self.data) if i not in checked_indices]

        controller = Controller()
        for id in data_want_to_be_removed:
            controller.delete_purchased_food(id)

        self.reset_table_and_pagination()


def get_purchased_food_data(category: str = None) -> list:
    controller = Controller()
    data = []

    if category is None:
        rows = controller.get_purchased_food()

        for row in rows:
            row_data = [row[0], row[4], row[1], row[3]]
            data.append(row_data)
    else:
        rows = controller.get_purchased_food_with_category(category)

        for row in rows:
            row_data = [row[0], row[5], row[1], row[3]]
            data.append(row_data)

    return data
