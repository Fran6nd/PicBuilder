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

        self.lbl = QLabel(self)
        self.lbl.setAlignment(QtCore.Qt.AlignCenter)
        self.lbl.setStyleSheet("border: 1px solid black;")
        layout.addWidget(self.lbl)
        self.setLayout(layout)
        self.lbl_size = [self.lbl.width(), self.lbl.height()]

    def update(self):
        if self.node.value != None:
                self.lbl.setPixmap(self.node.value.scaled(self.lbl_size[0], self.lbl_size[1], QtCore.Qt.KeepAspectRatio, QtCore.Qt.SmoothTransformation))
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
                self.value = val
                self.content.update()
                return val
            except ValueError as e:
                self.markInvalid()
                self.grNode.setToolTip(str(e))
                self.markDescendantsDirty()
            except Exception as e:
                self.markInvalid()
                self.grNode.setToolTip(str(e))
    def onEdgeConnectionChanged(self, edge):
        self.eval()
    NodeContent_class = NNodeContent