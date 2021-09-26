from nodes.baseNode import BaseNode
import os
from PyQt5 import QtCore
from PyQt5 import QtWidgets
from PyQt5.QtGui import QPixmap
from PyQt5.QtWidgets import QLabel, QPushButton, QVBoxLayout
from nodeeditor.node_node import Node
from nodeeditor.node_scene import Scene
from nodeContentBase import NNodeContentBase

class FlipBlackNWhite(BaseNode):
    def __init__(self, scene: 'Scene'):
        super().__init__(scene, title="Flip Black And White", inputs=[1], outputs = [1])
    pass