from nodes.baseNode import BaseNode
import os
from PyQt5 import QtCore
from PyQt5 import QtWidgets
from PyQt5.QtGui import QPixmap
from PyQt5.QtWidgets import QLabel, QPushButton, QVBoxLayout
from nodeeditor.node_node import Node
from nodeeditor.node_scene import Scene
from nodeContentBase import NNodeContentBase

class Output(BaseNode):
    def __init__(self, scene: 'Scene'):
        super().__init__(scene, title="Image Output", inputs=[1])
    def remove(self):
        pass
    NodeContent_class = NNodeContentBase