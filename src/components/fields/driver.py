import sys

from PyQt6.QtWidgets import QApplication
from PyQt6.QtWidgets import QVBoxLayout
from PyQt6.QtWidgets import QWidget

from src.components.fields.Dropdown import Dropdown
from src.components.fields.TextField import TextField


class MainWindow(QWidget):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("Your Food Companion")
        self.setGeometry(100, 100, 400, 400)

        # create a text field
        text_field = TextField("Input here")

        # add the text field to a layout
        layout = QVBoxLayout()
        layout.addWidget(text_field)

        # Create a dropdown
        dropdown = Dropdown()
        dropdown.addItem("Item 1")
        dropdown.addItem("Item 2")
        dropdown.addItem("Item 3")
        layout.addWidget(dropdown)
        self.setLayout(layout)


if __name__ == '__main__':
    app = QApplication(sys.argv)
    window = MainWindow()
    window.show()
    sys.exit(app.exec())
