import sys

from PyQt5.QtCore import *
from PyQt5.QtWidgets import *


class MyWidget(QWidget):
    def __init__(self, parent=None):
        super().__init__(parent=parent)
        # QBoxLayout
        glayout = QGridLayout()
        glayout.setContentsMargins(100, 100, 100, 100)

        for y in range(5):
            for x in range(5):
                if x == y or y == -x + 4:
                    btn = QPushButton(F'按钮{y},{x}', self)  # QPushButton(F'按钮{i}', self)
                    glayout.addWidget(btn, y, x)

        self.setLayout(glayout)

        # 布局
        self.show()

    def sizeHint(self):
        return QSize(400, 600)


app = QApplication(sys.argv)
wid = MyWidget()
sys.exit(app.exec())
