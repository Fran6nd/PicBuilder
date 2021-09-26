import os
from PyQt5 import QtCore
from PyQt5 import QtWidgets
from PyQt5.QtGui import QPixmap
from PyQt5.QtWidgets import QLabel, QPushButton, QVBoxLayout
from nodeeditor.node_node import Node
from nodeeditor.node_scene import Scene
from nodeContentBase import NNodeContentBase

class BaseNode(Node):
    def __init__(self, scene: 'Scene', title="Base Node", inputs: list=[], outputs: list=[]):
        super().__init__(scene, title=title, inputs=inputs, outputs=outputs)
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
            #self.evalChildren()

            return val

    def eval(self):
        
        val = self.evalImplementation()
        if not self.isDirty() and not self.isInvalid():
            try:
                self.value = val
                self.content.update()
                self.evalChildren()
                return val
            except ValueError as e:
                self.markInvalid()
                self.grNode.setToolTip(str(e))
                self.markDescendantsDirty()
            except Exception as e:
                self.markInvalid()
                self.grNode.setToolTip(str(e))
    def onEdgeConnectionChanged(self, edge):
        #self.eval()
        #self.evalChildren()
        print(self.title, "edge changed")
    def onInputChanged(self, socket):
        print(self.title, "input changed")
        self.eval()
        #self.evalChildren()
    NodeContent_class = NNodeContentBase