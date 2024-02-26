from gui.core.qt_core import *
from . flow_layout import FlowLayout

class PyImagePage(QFrame):
    def __init__(self):
        super().__init__()
        self.flow_layout = FlowLayout()
        self.btn_group = QButtonGroup()
        self.btn_group.setExclusive(True)
        self.setStyleSheet("background: transparent")
        self.setFrameShape(QFrame.NoFrame)
        self.setLayout(self.flow_layout)

