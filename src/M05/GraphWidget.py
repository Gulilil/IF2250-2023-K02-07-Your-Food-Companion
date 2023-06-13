from PyQt6.QtWidgets import QWidget, QVBoxLayout, QHBoxLayout
import pyqtgraph as pg
from .ReportTable import ReportTable
from .ReportDropdown import Dropdown
from src.controller.controller import Controller
from src.controller.controller import Controller

# headers = ["Category", "January", "February", "March", "April", "May"]
# indexes = ["Category", "Whole Foods", "Dairy", "Fast Foods"]
# data = [
#     [400000, 100000, 300000, 200000, 500000],
#     [100000, 250000, 200000, 300000, 150000],
#     [130000, 150000, 140000, 100000, 120000]
# ]

class GraphWidget(QWidget):
    availableStats = ["Food Waste", "Eaten Food", "Bought Food"]
    foodWasteCols = ["Quantity", "Cost"]
    eatenFoodCols = ["Quantity"]
    boughtFoodCols = ["Quantity"]

    statToTable = {
        "Food Waste": "expired_food", 
        "Eaten Food": "eaten_food",
        "Bought Food": "purchased_food",
    }

    statToDate = {
        "Food Waste": "expiration_date", 
        "Eaten Food": "eaten_date",
        "Bought Food": "purchase_date",
    }

    colToTableCol = {
        "Quantity": "quantity",
        "Cost": "price"
    }

    monthsMapping = ["January", "February", "March", "April", "May", "June", "July", "August", "September", "October", "November", "December"]

    def __init__(self, controller: Controller=None, parent=None) -> None:
        super().__init__(parent)

        self.controller = controller

        self.selectedStat = "Food Waste"
        self.currentColumn = "Quantity"

        self.data = []
        self.indexes = []
        self.headers = []

        container = QWidget()
        container.setStyleSheet(
            """
            background-color: #2F3136;
            border-radius: 16px;
            padding: 32px;
            """
        )
        containerLayout = QVBoxLayout()
        containerLayout.addWidget(container)
        containerLayout.setContentsMargins(0,0,0,0)
        self.setLayout(containerLayout)

        contentLayout = QVBoxLayout()
        contentLayout.setSpacing(0)
        container.setLayout(contentLayout)

        dropdownLayout = QHBoxLayout()
        contentLayout.addLayout(dropdownLayout)

        statisticDropdown = Dropdown()
        statisticDropdown.addItems(self.availableStats)
        statisticDropdown.currentTextChanged.connect(self.onChangeStatistic)
        dropdownLayout.addWidget(statisticDropdown)

        self.dataColumnDropdown = Dropdown()
        self.dataColumnDropdown.addItems(self.foodWasteCols)
        self.dataColumnDropdown.currentTextChanged.connect(self.onChangeColumn)
        dropdownLayout.addWidget(self.dataColumnDropdown)
        dropdownLayout.addStretch()
        dropdownLayout.setSpacing(32)

        self.graph: None | QWidget = None
        self.table: None | QWidget = None
        
        self.dataLayout = QVBoxLayout()
        self.dataLayout.setSpacing(0)
        contentLayout.addLayout(self.dataLayout)

        self.displayStats()

    def normalizeData(self):
        catQuery = self.controller.get_distinct_category()
        self.indexes = ["Categories"]
        categories = []
        for cat in catQuery:
            self.indexes.append(cat[0])
            categories.append(cat[0])
        
        summary = {}
        for category in categories:
            summaryQuery = self.controller.get_category_summary(self.statToTable[self.selectedStat], category, self.colToTableCol[self.currentColumn], self.statToDate[self.selectedStat])
            categorySummary = []
            for res in summaryQuery:
                categorySummary.append((res[0], res[1], res[2]))
            summary[category] = categorySummary
        
        months = set()
        for category in summary:
            for monthSummary in summary[category]:
                months.add((monthSummary[0], monthSummary[1]))
        
        months = list(months)
        months = sorted(months)
        self.headers = ["Categories"]
        for month in months:
            self.headers.append(self.monthsMapping[int(month[1])-1] + " " + month[0])

        self.data = []
        for category in summary:
            rowData = [0 for _ in months]
            for idx, month in enumerate(months):
                for summaryData in summary[category]:
                    if month[0] == summaryData[0] and month[1] == summaryData[1]:
                        rowData[idx] = summaryData[2]
            self.data.append(rowData)

    def displayStats(self):
        if self.graph != None:
            self.dataLayout.removeWidget(self.graph)
            self.graph.setParent(None)

        if self.table != None:
            self.dataLayout.removeWidget(self.table)
            self.table.setParent(None)

        self.normalizeData()

        pg.setConfigOption('background', (47, 49, 54, 100))
        pg.setConfigOptions(antialias=True)
        self.graph = pg.PlotWidget()
        self.graph.setMinimumHeight(400)
        self.graph.showGrid(x=False, y=True)
        
        self.graph.getAxis("left").setPen('w')
        self.graph.getAxis("left").setTextPen('w')

        colorTuples = [
            (24, 160, 251),
            (242, 119, 5),
            (192, 24, 251),
            (255, 234, 238),
            (0, 242, 242),
            (77, 170, 87),
            (237, 28, 36),
            (159, 107, 160)
        ]

        for idx, row in enumerate(self.data):
            self.graph.plot(row, pen=pg.mkPen(colorTuples[idx % len(colorTuples)], width=3), symbol="o", symbolPen=pg.mkPen(colorTuples[idx % len(colorTuples)]), symbolBrush=colorTuples[idx % len(colorTuples)])

        # Set x-axis range with padding
        x_range = [0, len(self.data[0])-1]
        padding_x = 0.05 * (x_range[1] - x_range[0])  # 5% padding on each side

        # Set y-axis range with padding
        y_range = [min([min(row) for row in self.data]), max([max(row) for row in self.data])]
        padding_y = 0.3 * (y_range[1] - y_range[0])  # 5% padding on each side

        self.graph.plotItem.getViewBox().setRange(xRange=[x_range[0] - padding_x, x_range[1] + padding_x], yRange=[y_range[0] - padding_y, y_range[1]])

        # Enable zooming with the mouse wheel
        self.graph.setMouseEnabled(x=False, y=False)
        self.graph.setContentsMargins(0,0,0,0)
        self.dataLayout.addWidget(self.graph)

        self.table = ReportTable(colorTuples=colorTuples, header=self.headers, indexes=self.indexes, data=self.data)
        self.table.setContentsMargins(0,0,0,0)
        self.dataLayout.addWidget(self.table)

    def onChangeStatistic(self, statistic):
        if statistic == "Food Waste":
            self.dataColumnDropdown.clear()
            self.dataColumnDropdown.addItems(self.foodWasteCols)
        elif statistic == "Eaten Food":
            self.dataColumnDropdown.clear()
            self.dataColumnDropdown.addItems(self.eatenFoodCols)
        elif statistic == "Bought Food":
            self.dataColumnDropdown.clear()
            self.dataColumnDropdown.addItems(self.boughtFoodCols)
        self.selectedStat = statistic
        self.currentColumn = "Quantity"
        self.displayStats()

    def onChangeColumn(self, column):
        self.currentColumn = column
        self.displayStats()