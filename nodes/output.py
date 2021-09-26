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
        self.node.value = None
        self.setParent(parent)
        layout = QVBoxLayout()

        lbl = QLabel(self)
        lbl.setAlignment(QtCore.Qt.AlignCenter)
        lbl.setStyleSheet("border: 1px solid black;")
        btn = QPushButton('Browse', self)
        layout.addWidget(btn)
        layout.addWidget(lbl)
        self.setLayout(layout)
        def browse(blah):
            self.node.eval()
            if self.node.value != None:
                 lbl.setPixmap(self.node.value.scaled(lbl.width(), lbl.height(), QtCore.Qt.KeepAspectRatio, QtCore.Qt.SmoothTransformation))
        btn.clicked.connect(browse)

        #self.adjustSize()




class Output(Node):
    def __init__(self, scene: 'Scene'):
        super().__init__(scene, title="Image Output", inputs=[1])
    def evalImplementation(self):
        i1 = self.getInput(0)
        print("output impl ", str(i1))

        if i1 is None:
            self.markInvalid()
            self.markDescendantsDirty()
            self.grNode.setToolTip("Connect all inputs")
            return None

        else:
            print("output input connected")
            val = i1.eval()
            self.value = val
            self.markDirty(False)
            self.markInvalid(False)
            self.grNode.setToolTip("")

            self.markDescendantsDirty()
            self.evalChildren()

            return val

    def eval(self):
        print("Output eval running...")
        val = self.evalImplementation()
        if not self.isDirty() and not self.isInvalid():
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