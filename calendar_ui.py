from PyQt5.QtWidgets import QWidget, QVBoxLayout, QCalendarWidget, QLabel

class CalendarUI(QWidget):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("My Calendar App")
        self.setGeometry(100, 100, 400, 300)

        layout = QVBoxLayout()

        # Calendar widget
        self.calendar = QCalendarWidget(self)
        self.calendar.setGridVisible(True)
    

        # Label to show selected date
        self.label = QLabel("Select a date", self)

        # Connect calendar click to label update
        self.calendar.clicked.connect(self.show_date)

        layout.addWidget(self.calendar)
        layout.addWidget(self.label)

        self.setLayout(layout)

    def show_date(self, date):
        self.label.setText(f"Selected Date: {date.toString()}")