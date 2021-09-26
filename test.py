from nodes.output import Output
import os, sys, inspect
from PyQt5 import QtCore
from PyQt5 import QtGui
from PyQt5 import QtWidgets
from PyQt5.QtGui import QImage, QPixmap
from PyQt5.QtWidgets import QPushButton, QSizePolicy, QVBoxLayout
from qtpy.QtWidgets import QApplication, QLabel

sys.path.insert(0, os.path.join( os.path.dirname(__file__), "..", ".." ))

from nodeeditor.utils import loadStylesheet
from nodeeditor.node_node import Node
from nodeeditor.node_editor_window import NodeEditorWindow
from nodes.input import Input


if __name__ == '__main__':
    app = QApplication(sys.argv)

    wnd = NodeEditorWindow()



    wnd.nodeeditor.scene.setNodeClassSelector(lambda data: Input)
    node = Input( wnd.nodeeditor.scene)
    node = Output( wnd.nodeeditor.scene)



    module_path = os.path.dirname( inspect.getfile(wnd.__class__) )

    loadStylesheet( os.path.join( module_path, 'qss/nodestyle.qss') )

    sys.exit(app.exec_())
