from nodes.baseNode import BaseNode
import os
from PyQt5 import QtCore
from PyQt5 import QtWidgets
from PyQt5.QtGui import QColor, QPixmap
from PyQt5.QtWidgets import QLabel, QPushButton, QVBoxLayout
from nodeeditor.node_node import Node
from nodeeditor.node_scene import Scene
from nodeContentBase import NNodeContentBase

class FlipBlackNWhite(BaseNode):
    def __init__(self, scene: 'Scene'):
        super().__init__(scene, title="Flip Black And White", inputs=[1], outputs = [1])
    def apply(self):

        self.value = self.value.copy()
        if(self.value):
            for x in range(0, self.value.width()):
                for y in range(0, self.value.height()):
                    r, g, b, a = QColor(self.value.pixel(x ,y)).getRgb()
                    if r < 255/2:
                        r = 255
                        g = 255
                        b = 255
                    else:
                        r = 0
                        g = 0
                        b = 0
                    self.value.setPixel(x, y, QColor(r, g, b, a).rgb())