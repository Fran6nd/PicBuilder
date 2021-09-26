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
            layout = QVBoxLayout()
            lbl = QLabel(self)
            lbl.setAlignment(QtCore.Qt.AlignCenter)
            btn = QPushButton('Browse', self)
            layout.addWidget(btn)
            layout.addWidget(lbl)
            def load_image(path):
                if os.path.isfile(path):
                    pixmap = QPixmap(path)
                #self.setScaledContents(True)
                #self.setSizePolicy( QSizePolicy.Policy.Minimum, QSizePolicy.Policy.Maximum)
                    pixmap = pixmap.scaledToWidth(100)
                    lbl.resize(pixmap.width(), pixmap.height())
                    lbl.setPixmap(pixmap)
            def browse(blah):
                fileName, _ = QtWidgets.QFileDialog.getOpenFileName(None, 'Choose an image', "." , '*.png')
                load_image(fileName)
                pass
            btn.clicked.connect(browse)
            load_image("./empty.png")
            self.setLayout(layout)

            #self.adjustSize()



    class Input(Node):
        NodeContent_class = NNodeContent

    wnd.nodeeditor.scene.setNodeClassSelector(lambda data: Input)
    node = Input( wnd.nodeeditor.scene,title = "Input", outputs=[0])

    print("node content:", node.content)



    module_path = os.path.dirname( inspect.getfile(wnd.__class__) )

    loadStylesheet( os.path.join( module_path, 'qss/nodestyle.qss') )

    sys.exit(app.exec_())
