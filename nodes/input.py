import os
from PyQt5 import QtCore
from PyQt5 import QtWidgets
from PyQt5.QtGui import QPixmap
from PyQt5.QtWidgets import QLabel, QPushButton, QVBoxLayout
from nodeeditor.node_node import Node
from nodeeditor.node_scene import Scene


class NNodeContent(QLabel):  # , Serializable):
        def __init__(self, node, parent=None, input = None):
            super().__init__()
            self.node = node
            self.setParent(parent)
            layout = QVBoxLayout()

            lbl = QLabel(self)
            lbl.setAlignment(QtCore.Qt.AlignCenter)
            lbl.setStyleSheet("border: 1px solid black;")
            btn = QPushButton('Browse', self)
            layout.addWidget(btn)
            layout.addWidget(lbl)
            def load_image(path):
                if os.path.isfile(path):
                    pixmap = QPixmap(path)
                    self.node.value = pixmap
                    lbl.setScaledContents(True)
                #self.setSizePolicy( QSizePolicy.Policy.Minimum, QSizePolicy.Policy.Maximum)
                    pixmap = pixmap.scaledToWidth(lbl.width())
                    #lbl.resize(pixmap.width(), pixmap.height())
                    #lbl.maximumWidth = 120
                    #lbl.setPixmap(pixmap)
                    lbl.setPixmap(pixmap.scaled(lbl.width(), lbl.height(), QtCore.Qt.KeepAspectRatio, QtCore.Qt.SmoothTransformation))
            def browse(blah):
                fileName, _ = QtWidgets.QFileDialog.getOpenFileName(None, 'Choose an image', "." , 'Image Files(*.png *.jpg *.bmp)')
                load_image(fileName)
                pass
            btn.clicked.connect(browse)
            load_image("./empty.png")
            self.setLayout(layout)

            #self.adjustSize()



class Input(Node):
    def __init__(self, scene: 'Scene'):
        super().__init__(scene, title="Image Input", outputs=[1])
    def evalImplementation(self):
            return self.value

    def eval(self):
        print("input eval running")
        val = self.evalImplementation()
        if not self.isDirty() and not self.isInvalid():
            pass

        try:

            print("...ok")
            return val
        except ValueError as e:
            self.markInvalid()
            self.grNode.setToolTip(str(e))
            self.markDescendantsDirty()
        except Exception as e:
            self.markInvalid()
            self.grNode.setToolTip(str(e))
    NodeContent_class = NNodeContent