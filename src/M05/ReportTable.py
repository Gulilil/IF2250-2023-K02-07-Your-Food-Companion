from PyQt6.QtWidgets import QWidget, QVBoxLayout, QHBoxLayout, QLabel
from PyQt6.QtGui import QFont

font = (QFont("Karla", 14))

class TableCell(QWidget):
    def __init__(self, legendColor: None | tuple=None, isTopLeft=False, isTopRight=False, isBottomLeft=False, isBottomRight=False,  textAlign: str= "right", label: str = "",  parent: QWidget = None) -> None:
        super().__init__(parent)

        container = QWidget()
        container.setFont(font)
        container.setObjectName("table-cell-container")
        container.setStyleSheet(
            f"""
            #table-cell-container {{
                border: 1px solid #4D5259;
                text-align {textAlign};
            }}
            * {{
                color: white;
                padding: 3px 4px;
                border-radius: 0;
                {"border-top-left-radius :16px;" if isTopLeft else ""}
                {"border-top-right-radius : 16px;" if isTopRight else ""}
                {"border-bottom-left-radius : 16px;" if isBottomLeft else ""}
                {"border-bottom-right-radius : 16px;" if isBottomRight else ""}
            }}
            """
        )
        containerLayout = QHBoxLayout()
        containerLayout.setContentsMargins(0,0,0,0)
        containerLayout.addWidget(container)
        self.setLayout(containerLayout)

        contentLayout = QHBoxLayout()
        container.setLayout(contentLayout)

        if legendColor != None:
            circle = QLabel()
            circle.setFixedSize(20,20)
            legendColorStr = [str(x) for x in legendColor]
            rgbBorder = "rgb(" + ','.join(legendColorStr) + ")"
            circle.setStyleSheet(f"border: 3px solid {rgbBorder};border-radius: 10px;")
            contentLayout.addWidget(circle)

        label = QLabel(label)
        label.setFont(font)
        contentLayout.addWidget(label)

class ReportTable(QWidget):
    def __init__(self, colorTuples: list[tuple] = [], indexes: list[str] =[], data: list[list[int]] = [], header: list[str] =[], parent: QWidget = None) -> None:
        super().__init__(parent)

        container = QWidget()
        container.setObjectName("report-table-container")
        container.setStyleSheet(
            """
            #report-table-container {
                background-color: #36393F;
                border: 1px solid #4D5259;
                border-radius: 16px;
                color: white;
                margin: 5px;
            }
            """
        )
        containerLayout = QVBoxLayout()
        containerLayout.addWidget(container)
        self.setLayout(containerLayout)

        contentLayout = QVBoxLayout()
        contentLayout.setSpacing(0)
        container.setLayout(contentLayout)

        headerLayout = QHBoxLayout()
        headerLayout.setSpacing(0)
        headerLayout.setContentsMargins(0,0,0,0)
        contentLayout.addLayout(headerLayout)
        indexCell = TableCell(legendColor=(0,0,0,0), label=indexes[0], textAlign="left", isTopLeft=True)
        headerLayout.addWidget(indexCell)
        for i in range(1, len(header)):
            cell = TableCell(label=header[i], isTopRight=(i == len(header) - 1))
            headerLayout.addWidget(cell)

        for i in range(len(data)):
            rowLayout = QHBoxLayout()
            rowLayout.setSpacing(0)
            rowLayout.setContentsMargins(0,0,0,0)
            contentLayout.addLayout(rowLayout)
            isLastRow = i == len(data) - 1
            rowIndexCell = TableCell(legendColor=colorTuples[i % len(colorTuples)], label=indexes[i + 1], textAlign="left", isBottomLeft=isLastRow)
            rowLayout.addWidget(rowIndexCell)
            for j in range(0, len(data[i])):
                isLastCol = j == len(data[i]) - 1
                cell = TableCell(label=str(data[i][j]), isBottomRight=(isLastRow and isLastCol))
                rowLayout.addWidget(cell)
            

