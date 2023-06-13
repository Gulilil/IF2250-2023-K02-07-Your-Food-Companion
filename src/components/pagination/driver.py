import sys

from PyQt6.QtWidgets import *

from src.components.pagination.Pagination import Arrow, PageNumber, Pagination


class Window(QMainWindow):
    type = None
    title = "Your Food Companion"

    def __init__(self):
        super().__init__()
        # Setting up the app
        self.resize(1000, 600)
        self.setStyleSheet("background-color: white")

        next = Arrow(self, "Next")
        next.move(100, 0)

        back = Arrow(self, "Back")
        back.move(0, 0)
        back.setDisabled()

        p1 = PageNumber(self, 1)
        p1.move(0, 75)

        p2 = PageNumber(self, 2)
        p2.move(50, 75)
        p2.setCurrent()
        p2.setText("3")

        p = Pagination(self, 8)
        p.move(0, 150)

        self.show()

    def test(self, insert):
        print(insert)


if __name__ == "__main__":
    app = QApplication(sys.argv)
    # Starting the app
    window = Window()
    sys.exit(app.exec())
