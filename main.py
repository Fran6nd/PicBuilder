from PyQt5 import QtGui

from PyQt5.QtWidgets import QApplication, QMainWindow

import sys

from PyQt5.QtGui import QPainter, QBrush, QPen

from PyQt5.QtCore import Qt

from PyQt5.QtWidgets import QWidget, QApplication
from PyQt5.QtWidgets import QAction, qApp

class Canva(QWidget):
    #evenement QPaintEvent
    def paintEvent(self, event): # event de type QPaintEvent
        painter = QPainter(self)
        painter.setPen(QPen(Qt.green,  8, Qt.DashLine))
        painter.drawEllipse(40, 40, 400, 400)
    # Blabla de dessin ici

class Window(QMainWindow):

    def __init__(self):

        super().__init__()

        self.title = "PyQt5 Drawing Tutorial"

        self.top= 150

        self.left= 150

        self.width = 500

        self.height = 500

        self.InitWindow()

    def InitWindow(self):

        self.setGeometry(self.top, self.left, self.width, self.height)         
        
        exitAction = QAction('&Exit', self)        
        exitAction.setShortcut('Ctrl+Q')
        exitAction.setStatusTip('Exit application')
        exitAction.triggered.connect(qApp.quit)

        self.statusBar()

        menubar = self.menuBar()
        fileMenu = menubar.addMenu('&File')
        fileMenu.addAction(exitAction)
        
        
        self.setWindowTitle('PicBuilder by Fran6nd')
        self.setCentralWidget(Canva())
        self.show()

    def paintEvent(self, event):
        pass

App = QApplication(sys.argv)

window = Window()

sys.exit(App.exec())