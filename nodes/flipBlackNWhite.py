import os
from PyQt5 import QtCore
from PyQt5 import QtWidgets
from PyQt5.QtGui import QPixmap
from PyQt5.QtWidgets import QLabel, QPushButton, QVBoxLayout
from nodeeditor.node_node import Node
from nodeeditor.node_scene import Scene
from nodeContentBase import NNodeContentBase

class FlipBlackNWhite(Node):
    def __init__(self, scene: 'Scene'):
        super().__init__(scene, title="Flip Black And White", inputs=[1], outputs=[1])
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
    NodeContent_class = NNodeContentBase