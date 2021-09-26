from nodeeditor.node_editor_widget import NodeEditorWidget
from nodes.flipBlackNWhite import FlipBlackNWhite
from nodes.output import Output
import os, sys, inspect
from PyQt5 import QtCore
from PyQt5 import QtGui
from PyQt5 import QtWidgets
from PyQt5.QtGui import QImage, QPixmap
from PyQt5.QtWidgets import QAction, QMenu, QPushButton, QSizePolicy, QVBoxLayout
from qtpy.QtWidgets import QApplication, QLabel

sys.path.insert(0, os.path.join( os.path.dirname(__file__), "..", ".." ))

from nodeeditor.utils import loadStylesheet
from nodeeditor.node_node import Node
from nodeeditor.node_editor_window import NodeEditorWindow
from nodes.input import Input
from nodes.flipBlackNWhite import FlipBlackNWhite
from functools import partial

class nodeditorwidget(NodeEditorWidget):
    def __init__(self, *args, **kwargs):
        super().__init__( *args, **kwargs)
    def mousePressEvent(self, QMouseEvent):
        if QMouseEvent.button() == QtCore.Qt.LeftButton:
            print("Left Button Clicked")
        elif QMouseEvent.button() == QtCore.Qt.RightButton:
            #do what you want here
            print("Right Button Clicked")
    def showMenu(self,pos):
        menu = QMenu()
        clear_action = menu.addAction("Clear Selection")
        action = menu.exec_(self.mapToGlobal(pos))
        if action == clear_action:
            self.combo.setCurrentIndex(0)
            
class window(NodeEditorWindow):
    NodeEditorWidget_class = nodeditorwidget
    def createActions(self):
        super().createActions()



    def createMenus(self):
        """Create Menus for `File` and `Edit`"""
        self.createFileMenu()
        self.createEditMenu()
        self.createAddMenu()

    def createFileMenu(self):
        menubar = self.menuBar()
        self.fileMenu = menubar.addMenu('&File')
        self.fileMenu.addAction(self.actNew)
        self.fileMenu.addSeparator()
        self.fileMenu.addAction(self.actOpen)
        self.fileMenu.addAction(self.actSave)
        self.fileMenu.addAction(self.actSaveAs)
        self.fileMenu.addSeparator()
        self.fileMenu.addAction(self.actExit)

    def createAddMenu(self):
        menubar = self.menuBar()
        self.fileMenu = menubar.addMenu('&Add')
        """Create basic `File` and `Edit` actions"""
        def tt(node):
            node(self.nodeeditor.scene)
        nodeList = [Input, FlipBlackNWhite]
        for node in nodeList:
            self.fileMenu.addAction(QAction('&Add ' + node.__name__, self, statusTip="Add a new image input", triggered=partial(tt, node)))
        #self.fileMenu.addAction(self.addInput)

if __name__ == '__main__':
    app = QApplication(sys.argv)

    wnd = window()



    node = Input( wnd.nodeeditor.scene)
    node = Output( wnd.nodeeditor.scene)
    node = FlipBlackNWhite( wnd.nodeeditor.scene)



    module_path = os.path.dirname( inspect.getfile(wnd.__class__) )

    loadStylesheet( os.path.join( module_path, 'qss/nodestyle.qss') )

    sys.exit(app.exec_())
