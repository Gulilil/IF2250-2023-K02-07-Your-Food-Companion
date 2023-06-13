import sys

from PyQt6.QtWidgets import *

from src.components.wrappers.Sidebar import Sidebar
from src.components.wrappers.Topbar import Notification, Topbar


class Window(QMainWindow):
    type = None
    title = "Your Food Companion"

    def __init__(self):
        super().__init__()
        # Setting up the app
        screenW = app.primaryScreen().size().width()
        screenH = app.primaryScreen().size().height()
        self.resize(screenW, screenH)
        self.setStyleSheet("background-color: black")

        # tab2 = SidebarTab(self, "Hehe")
        # tab1 = SidebarTab(self, "Dashboard")
        # tab1.move(0,100)
        # tab1.setCurrent()

        sb = Sidebar(self, screenW, screenH)
        sb.move(0, 0)

        tb = Topbar(self, screenW, 300)

        n = Notification(self)
        n.move(500, 100)

    def test(self, insert):
        print(insert)


if __name__ == "__main__":
    app = QApplication(sys.argv)
    # Starting the app
    window = Window()
    window.showMaximized()
    sys.exit(app.exec())
