from PyQt5 import QtCore
from PyQt5.QtWidgets import QLabel, QVBoxLayout


class NNodeContentBase(QLabel):  # , Serializable):
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
        self.lbl_size = None

    def update(self):
        if not self.lbl_size:
            self.lbl_size = [self.lbl.width(), self.lbl.height()]
        if self.node.value != None:
                self.lbl.setPixmap(self.node.value.scaled(self.lbl_size[0],self.lbl_size[1], QtCore.Qt.KeepAspectRatio, QtCore.Qt.SmoothTransformation))