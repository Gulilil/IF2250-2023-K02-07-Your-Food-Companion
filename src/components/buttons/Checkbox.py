""" Checkbox Components """

from PyQt6.QtCore import Qt
from PyQt6.QtWidgets import QCheckBox

Checkbox_Style_Disabled = """QCheckBox::indicator{border-image:url(./assets/icons/cboxdisabled.png);border-radius:5px}
                             QCheckBox::indicator{width:25px;height:25px}"""

Checkbox_Style = """QCheckBox::indicator:checked{border-image:url(./assets/icons/cboxchecked.png);border-radius:5px}
                    QCheckBox::indicator:unchecked{border-image:url(./assets/icons/cboxunchecked.png);border-radius:5px}
                    QCheckBox::indicator{width:25px;height:25px}"""


class Checkbox(QCheckBox):
    def __init__(self, parent=None):
        self.enabled = True
        self.checked = False
        super(Checkbox, self).__init__(parent)
        self.stateChanged.connect(self.changeCheckState)
        self.setStyleSheet(Checkbox_Style)
        self.setEnabled(True)

    def enableCheckbox(self):
        self.setStyleSheet(Checkbox_Style)
        self.setEnabled(True)
        self.enabled = True

    def disableCheckbox(self):
        self.setStyleSheet(Checkbox_Style_Disabled)
        self.setEnabled(False)
        self.enabled = False

    def isChecked(self):
        return self.checked

    def changeCheckState(self):
        state = self.checkState()
        if state == Qt.CheckState.Checked:
            self.checked = True
        else:
            self.checked = False
