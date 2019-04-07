import sys

from PyQt5.QtCore import *
from PyQt5.QtWidgets import *

"""
setSizePolicy与sizeHint用于布局组件。
"""


class MyButton(QPushButton):
    def sizeHint(self):
        # 可以根据容器大小调整
        # return self.baseSize()
        return QSize(200, 200)


class MyWidget(QWidget):
    def __init__(self, parent=None):
        super().__init__(parent=parent)
        # self.resize(400, 400)
        self.btn = MyButton(self)
        self.btn.setSizeIncrement(5, 5)
        self.btn.setBaseSize(100, 40)  # 用于sizehint计算。
        self.btn.setSizePolicy(QSizePolicy.Ignored, QSizePolicy.Ignored)
        # self.btn.setMinimumSize(100, 100)

        # 布局
        layout = QGridLayout()
        layout.addWidget(self.btn)
        self.setLayout(layout)

        self.show()

    def sizeHint(self):
        return QSize(400, 300)


app = QApplication(sys.argv)
wid = MyWidget()
sys.exit(app.exec())
