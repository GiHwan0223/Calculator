# ch 4.2.1 main.py
import sys
from ui import View
from ctri import Control
from PyQt5.QtWidgets import QApplication

if __name__ == '__main__':
    calc = QApplication(sys.argv)
    app = QApplication(sys.argv)
    view = View()
    Control(view = view)
    sys.exit(app.exec_())
