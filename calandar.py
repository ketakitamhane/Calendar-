from PyQt5.QtWidgets import *
from PyQt5 import QtCore, QtGui
from PyQt5.QtGui import *
from PyQt5.QtCore import *
import sys

class Window(QMainWindow):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("Calandar")
        self.setGeometry(100,100,425,350)
        self.setWindowIcon(QIcon("calandar.png"))
        self.UiComponents()
        self.show()

    def UiComponents(self):
        calander = QCalendarWidget(self)
        calander.setGeometry(10,10,400,250)
        push = QPushButton("Next Year",self)
        push.setGeometry(120,280,100,40)
        push.clicked.connect(lambda: do_action())

        def do_action():
            calander.showNextYear()

            
App = QApplication(sys.argv)
window = Window()
sys.exit(App.exec())
