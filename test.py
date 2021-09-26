import os, sys, inspect
from PyQt5 import QtCore
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
        def __init__(self, node, parent=None):
            super().__init__()
            self.node = node
            self.setParent(parent)
            lbl = QLabel(self)

            lbl.setScaledContents(True)
            lbl.setAlignment(QtCore.Qt.AlignCenter)
            btn = QPushButton('PyQt5 button', self)
            path = ""
            def on_click(bla):
                path = "gogo"
                
                self.setPixmap(pixmap)
            pixmap = QPixmap('./wolf.png')
            self.setScaledContents(True)
            self.setSizePolicy( QSizePolicy.Policy.Ignored, QSizePolicy.Policy.Ignored)
            btn.clicked.connect(on_click)
            self.setPixmap(pixmap)



    class Input(Node):
        NodeContent_class = NNodeContent

    wnd.nodeeditor.scene.setNodeClassSelector(lambda data: Input)
    node = Input( wnd.nodeeditor.scene, outputs=[0, 1, 2])

    print("node content:", node.content)



    module_path = os.path.dirname( inspect.getfile(wnd.__class__) )

    loadStylesheet( os.path.join( module_path, 'qss/nodestyle.qss') )

    sys.exit(app.exec_())
