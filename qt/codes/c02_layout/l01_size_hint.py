import sys

from PyQt5.QtCore import *
from PyQt5.QtWidgets import *

"""
重载sizehint用来设置组件的优先尺寸，默认是(0,0)
baseSize与sizeIncrement一般不会直接对组件大小产生应用，主要用于在布局种计算组件大小。

setBaseSize(QSize)               # 默认大小，一般是（0，0），一般与sizeIncrement()一起工作，确定组件大小。
baseSize() → QSize

sizeIncrement() → QSize       # 组件大小变化单位
setSizeIncrement(QSize)

下面例子尽管没有布局，但用来说明baseSize与sizeIncrement的使用。
"""


class MyButton(QPushButton):
    def sizeHint(self):
        # 可以根据容器大小调整
        return self.baseSize()


class MyWidget(QWidget):
    def __init__(self, parent=None):
        super().__init__(parent=parent)
        # self.resize(400, 400)
        self.btn = MyButton(self)
        self.btn.setSizeIncrement(15, 15)
        self.btn.setBaseSize(100, 40)  # 用于sizehint计算。
        self.show()

    def sizeHint(self):
        return QSize(400, 300)


app = QApplication(sys.argv)
wid = MyWidget()
sys.exit(app.exec())
