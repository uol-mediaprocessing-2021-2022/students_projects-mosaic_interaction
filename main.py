import os
import sys

from PyQt5.QtWidgets import QApplication

from ui.Window import Window


os.environ["QT_AUTO_SCREEN_SCALE_FACTOR"] = "1"
app = QApplication(sys.argv)
win = Window()
win.show()

sys.exit(app.exec())
