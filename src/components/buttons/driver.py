import sys

from PyQt6.QtWidgets import *

from src.components.buttons.Button import Button
from src.components.buttons.Checkbox import Checkbox


class Window(QMainWindow):
    type = None
    title = "Your Food Companion"

    def __init__(self):
        super().__init__()
        # Setting up the app
        self.resize(1000, 600)

        smbtn = Button(self, "Small")
        smbtn.move(0, 0)
        smbtn.setText("Button")

        mdbtn = Button(self, "Medium")
        mdbtn.move(200, 0)
        mdbtn.setText("Button")

        lgbtn = Button(self, "Large")
        lgbtn.move(0, 100)
        lgbtn.setText("Button")
        lgbtn.setDisabled()

        cb = Checkbox(self)
        cb.move(0, 200)

        self.show()

    def test(self, insert):
        print(insert)


if __name__ == "__main__":
    app = QApplication(sys.argv)
    # Starting the app
    window = Window()
    sys.exit(app.exec())
