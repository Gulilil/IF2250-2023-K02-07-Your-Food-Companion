import os

from PyQt6.QtCore import Qt
from PyQt6.QtGui import QFont, QFontDatabase
from PyQt6.QtWidgets import QDialog, QFormLayout, QPushButton, QWidget
from PyQt6.QtWidgets import QLabel
from src.components.fields.TextField import TextField

titleFont = QFont("Karla", 25)
titleFont.setWeight(600)


class Forms(QDialog):
    arrInput = []

    def __init__(self, parent=None):
        super().__init__(parent)

        self.setWindowTitle("Form")
        self.setModal(True)
        self.w = 900
        self.h = 700
        self.topPadding = 100
        self.setFixedHeight(self.h)
        self.setFixedWidth(self.w)

        self.layer = QWidget(self)
        self.layer.move(15, self.topPadding)
        self.layer.resize(self.w - 30, self.h - self.topPadding - 100)
        self.layer.setStyleSheet("background-color: #36393F; border-radius:10px;")

        # Set the title of the main layout
        self.layout_title = QLabel(self)
        self.layout_title.setText("Form")
        self.layout_title.setStyleSheet("color: white")
        self.layout_title.setFont(titleFont)
        self.layout_title.resize(200, 60)
        self.layout_title.move(30, 30)

        # Set main layout
        # self.main_layout = QVBoxLayout(self)

        # create form layout
        self.form_layout = QFormLayout(self.layer)

        # # add form layout to main layout
        # self.main_layout.addLayout(self.layout_title)
        # self.main_layout.addLayout(self.form_layout)

        # add form layout title
        self.subtitle = QLabel("Item Details")
        self.subtitle.setStyleSheet("background: transparent; margin-left:20px")
        self.form_layout.addRow(self.subtitle)

        # Load font
        font_path = os.path.join(os.path.dirname(__file__), "../../../assets/font/Karla-Regular.ttf")
        font_id = QFontDatabase.addApplicationFont(font_path)

        if (font_id == -1):
            print("Error: font not found")

        font_family = QFontDatabase.applicationFontFamilies(font_id)
        font = QFont(font_family, 15)
        self.setFont(font)
        self.subtitle.setFont(font)

        # Set form alignment and spacing
        self.form_layout.setFormAlignment(Qt.AlignmentFlag.AlignLeft | Qt.AlignmentFlag.AlignVCenter)
        self.form_layout.setHorizontalSpacing(64)

        # Set style
        self.setStyleSheet("background-color: #4D5259; color: #F2F3F5;")
        # self.main_layout.setSpacing(32)
        # self.main_layout.setContentsMargins(32, 32, 32, 32)
        # self.form_layout.setSpacing(5)

        self.bottomLayer = QWidget(self)
        self.bottomLayer.resize(self.w, 75)
        self.bottomLayer.move(0, self.h - 75)
        self.bottomLayer.setStyleSheet("background-color: #202225")

        # create submit button
        self.submit_button = QPushButton(self.bottomLayer)
        self.submit_button.setText("Save")
        self.submit_button.clicked.connect(self.submit)
        self.submit_button.move(self.w - 100, 0)
        self.submit_button.resize(80, 60)
        self.submit_button.setStyleSheet("""
            QPushButton{
                margin-top:20px;
                background-color: #897DCF; 
                border-radius: 8px; 
                padding: 8px; 
                color: #F2F3F5; 
                font-size: 20px;
            }
            QPushButton:hover{
                background-color: #998DEF;
            }
        """)
        self.submit_button.setFont(font)

        # Set the layout
        self.setLayout(self.form_layout)

    def add_field(self, label, placeholder_text):
        field = TextField(placeholder_text)
        field.set_label(label)
        self.form_layout.addRow(field.label, field)

    def add_disabled_field(self, label, placeholder_text):
        field = TextField(placeholder_text)
        field.set_label(label)
        field.setReadOnly(True)
        self.form_layout.addRow(field.label, field)

    def set_title(self, title):
        # Find the QLabel widget that contains the form title
        self.layout_title.setText(title)
        self.layout_title.adjustSize()

        # Set the style of the widget
        self.layout_title.setStyleSheet("font-size: 30px;")

    def submit(self):
        self.arrInput = []
        for i in range(1, self.form_layout.rowCount()):
            label_widget = self.form_layout.itemAt(i, QFormLayout.ItemRole.LabelRole).widget()
            field_widget = self.form_layout.itemAt(i, QFormLayout.ItemRole.FieldRole).widget()

            label = label_widget.text()
            value = field_widget.text()
            # print(f"{label}: {value}")
            self.arrInput.append((label, value))

        self.accept()

    def getInput(self):
        return self.arrInput

    def getButtonSubmit(self):
        return self.submit_button
