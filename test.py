import os, sys, inspect
from PyQt5 import QtCore
from PyQt5 import QtGui
from PyQt5 import QtWidgets
from PyQt5.QtGui import QPixmap
from PyQt5.QtWidgets import QPushButton, QSizePolicy
from qtpy.QtWidgets import QApplication, QLabel

sys.path.insert(0, os.path.join( os.path.dirname(__file__), "..", ".." ))

from nodeeditor.utils import loadStylesheet
from nodeeditor.node_node import Node
from nodeeditor.node_editor_window import NodeEditorWindow


if __name__ == '__main__':
    app = QApplication(sys.argv)

    wnd = NodeEditorWindow()

    """Testing method to create a custom Node with custom content"""
    from nodeeditor.node_content_widget import QDMNodeContentWidget
    from nodeeditor.node_serializable import Serializable

    class NNodeContent(QLabel):  # , Serializable):
        def __init__(self, node, parent=None, input = None):
            super().__init__()
            self.node = node
            self.setParent(parent)
            
            lbl = QLabel(self)

            lbl.setAlignment(QtCore.Qt.AlignCenter)

            btn = QPushButton('Browse', lbl)
            def browse(blah):
                fileName, _ = QtWidgets.QFileDialog.getOpenFileName(None, 'Choose an image', "." , '*.png')
                if fileName != None:
                    pixmap = QPixmap(fileName)
                #self.setScaledContents(True)
                #self.setSizePolicy( QSizePolicy.Policy.Minimum, QSizePolicy.Policy.Maximum)
                    pixmap = pixmap.scaledToWidth(160)
                    lbl.setPixmap(pixmap)
                pass
            btn.clicked.connect(browse)
            path = ""
            pixmap = QPixmap('./wolf.png')
            if input != None:
                pixmap = QPixmap(input)
            #self.setScaledContents(True)
            #self.setSizePolicy( QSizePolicy.Policy.Minimum, QSizePolicy.Policy.Maximum)
            pixmap = pixmap.scaledToWidth(160)
            lbl.setPixmap(pixmap)
            #self.adjustSize()



    class Input(Node):
        NodeContent_class = NNodeContent

    wnd.nodeeditor.scene.setNodeClassSelector(lambda data: Input)
    node = Input( wnd.nodeeditor.scene, outputs=[0, 1, 2])

    print("node content:", node.content)



    module_path = os.path.dirname( inspect.getfile(wnd.__class__) )

    loadStylesheet( os.path.join( module_path, 'qss/nodestyle.qss') )

    sys.exit(app.exec_())
