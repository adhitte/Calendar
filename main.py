import sys
from PyQt5.QtWidgets import QApplication
from calendar_ui import CalendarUI

def main():
    app = QApplication(sys.argv)
    window = CalendarUI()
    window.show()
    sys.exit(app.exec_())

if __name__ == "__main__":
    main()