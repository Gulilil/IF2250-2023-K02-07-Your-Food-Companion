from PyQt6 import QtCore
from PyQt6.QtWidgets import QVBoxLayout, QHBoxLayout, QWidget, QLabel, QSizePolicy, QStackedLayout

from src.components.pagination.Pagination import Pagination
from src.components.buttons.Checkbox import Checkbox


class TableRow(QWidget):
    def __init__(self, data: list[str] = [], useCheckbox=False, parent=None) -> None:
        super(TableRow, self).__init__(parent)

        self.checkbox = None
        self.dataLabels: list[QLabel] = []

        container = QWidget()

        containerLayout = QVBoxLayout()
        containerLayout.addWidget(container)
        self.setLayout(containerLayout)

        rowContainerLayout = QHBoxLayout()
        rowContainerLayout.setContentsMargins(0, 0, 0, 0)

        if useCheckbox:
            self.checkbox = Checkbox(container)
            rowContainerLayout.addWidget(self.checkbox, alignment=QtCore.Qt.AlignmentFlag.AlignLeft)

        self.rowContainer = QWidget()
        self.rowContainer.setStyleSheet(
            """
            background-color: #3D4247;
            border-radius: 8px;
            """
        )
        rowLayout = QHBoxLayout()
        self.rowContainer.setLayout(rowLayout)
        self.rowContainer.setSizePolicy(QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Expanding)
        rowLayout.setContentsMargins(20, 12, 20, 12)
        for dataText in data:
            label = QLabel(str(dataText))  # Ini selalu dicasting ke string
            label.setStyleSheet(
                """
                font-weight: 600;
                font-size: 14px;
                line-height: 20px;
                color: #F2F3F5;
                """
            )
            self.dataLabels.append(label)
            label.setMinimumWidth(self.rowContainer.width() // len(data))
            rowLayout.addWidget(label)

        rowContainerLayout.addWidget(self.rowContainer)

        container.setLayout(rowContainerLayout)
        containerLayout.setContentsMargins(0, 0, 0, 0)

    def isChecked(self):
        if self.checkbox != None:
            return self.checkbox.isChecked()
        return False

    def setChecked(self, checked: bool):
        if self.checkbox != None:
            return self.checkbox.setChecked(checked)


class TableHeader(QWidget):
    def __init__(self, headers: list[str] = [], useCheckbox=False, parent=None) -> None:
        super(TableHeader, self).__init__(parent)

        container = QWidget()

        containerLayout = QVBoxLayout()
        containerLayout.addWidget(container)
        self.setLayout(containerLayout)

        headerContainerLayout = QHBoxLayout()
        headerContainerLayout.setContentsMargins(0, 0, 0, 0)

        if useCheckbox:
            self.checkbox = Checkbox(container)
            self.checkbox.hide()
            sp = self.checkbox.sizePolicy()
            sp.setRetainSizeWhenHidden(True)
            self.checkbox.setSizePolicy(sp)
            headerContainerLayout.addWidget(self.checkbox, alignment=QtCore.Qt.AlignmentFlag.AlignLeft)

        headerContainer = QWidget()
        headerLayout = QHBoxLayout()
        headerContainer.setLayout(headerLayout)
        headerContainer.setSizePolicy(QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Expanding)
        headerLayout.setContentsMargins(20, 0, 20, 0)
        dataLabels = []
        for dataText in headers:
            label = QLabel(dataText)
            label.setStyleSheet(
                """
                font-weight: 600;
                font-size: 14px;
                line-height: 20px;
                color: #F2F3F5;
                """
            )
            dataLabels.append(label)
            label.setMinimumWidth(headerContainer.width() // len(headers))
            headerLayout.addWidget(label)

        headerContainerLayout.addWidget(headerContainer)
        container.setLayout(headerContainerLayout)
        containerLayout.setContentsMargins(0, 0, 0, 0)


class Table(QWidget):
    def __init__(self, pagination: Pagination | None = None, rowsPerPage: int = 0, headers: list[str] = [],
                 data: list[list[str]] = [], useCheckbox=False, parent=None) -> None:
        super(Table, self).__init__(parent)

        self.rows: list[TableRow] = []
        self.data: list[list[str]] = []
        self.pagination: Pagination | None = None

        self.data = data

        container = QWidget()

        containerLayout = QVBoxLayout()
        containerLayout.addWidget(container)
        self.setLayout(containerLayout)

        tableLayout = QVBoxLayout()

        header = TableHeader(headers=headers, parent=self, useCheckbox=useCheckbox)
        header.setSizePolicy(QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Fixed)
        tableLayout.addWidget(header)

        dataLayout = QVBoxLayout()
        self.stackedLayout: QStackedLayout = QStackedLayout()
        self.rowLayouts: list[QVBoxLayout] = []

        if rowsPerPage == 0 or pagination == None:
            page_container = QWidget()
            t_layout = QVBoxLayout()
            t_layout.setContentsMargins(0, 0, 0, 0)
            for row in data:
                tableRow = TableRow(data=row, parent=self, useCheckbox=useCheckbox)
                tableRow.setSizePolicy(QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Fixed)
                self.rows.append(tableRow)
                t_layout.addWidget(tableRow)
            self.rowLayouts.append(t_layout)
            t_layout.setSpacing(16)
            t_layout.addStretch()
            page_container.setLayout(t_layout)
            self.stackedLayout.addWidget(page_container)
        else:
            for i in range(0, (len(data) + rowsPerPage - 1) // rowsPerPage):
                page_container = QWidget()
                t_layout = QVBoxLayout()
                t_layout.setContentsMargins(0, 0, 0, 0)
                page_container.setSizePolicy(QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Fixed)
                for j in range(i * rowsPerPage, min(len(data), (i + 1) * rowsPerPage)):
                    row = data[j]
                    tableRow = TableRow(data=row, parent=self, useCheckbox=useCheckbox)
                    tableRow.setSizePolicy(QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Fixed)
                    self.rows.append(tableRow)
                    t_layout.addWidget(tableRow)
                self.rowLayouts.append(t_layout)
                t_layout.setSpacing(16)
                t_layout.addStretch()
                page_container.setLayout(t_layout)
                self.stackedLayout.addWidget(page_container)

        dataLayout.addLayout(self.stackedLayout)

        selectAllLayout = QHBoxLayout()
        selectAllCheckbox = Checkbox()
        selectAllCheckbox.setSizePolicy(QSizePolicy.Policy.Fixed, QSizePolicy.Policy.Fixed)
        selectAllCheckbox.clicked.connect(self.onSelectAllClick)
        selectAllLabel = QLabel("Select / Deselect All")
        selectAllLabel.setSizePolicy(QSizePolicy.Policy.Fixed, QSizePolicy.Policy.Fixed)
        selectAllLabel.setStyleSheet(
            """
            font-weight: 600;
            font-size: 14px;
            line-height: 20px;
            color: #F2F3F5;
            """
        )

        selectAllLayout.addWidget(selectAllCheckbox)
        selectAllLayout.addWidget(selectAllLabel)
        selectAllLayout.addStretch()
        dataLayout.setSpacing(10)
        dataLayout.addLayout(selectAllLayout)

        tableLayout.addLayout(dataLayout)
        tableLayout.addStretch()

        container.setLayout(tableLayout)
        tableLayout.setSpacing(6)
        containerLayout.setSpacing(0)

        if pagination != None:
            self.pagination = pagination
            self.pagination.onChangePage = self.changePage
            self.rowsPerPage = rowsPerPage

    def changePage(self, pageNum: int):
        self.stackedLayout.setCurrentIndex(pageNum - 1)

    def onSelectAllClick(self) -> None:
        if len(self.data) == len(self.getCheckedIndexes()):
            for row in self.rows:
                row.setChecked(False)
        else:
            for row in self.rows:
                row.setChecked(True)

    def getCheckedIndexes(self) -> list[int]:
        checkedIndexes: list[int] = []
        for idx, row in enumerate(self.rows):
            if row.isChecked():
                checkedIndexes.append(idx)
        return checkedIndexes
