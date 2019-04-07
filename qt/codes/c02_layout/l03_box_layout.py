import sys

from PyQt5.QtCore import *
from PyQt5.QtWidgets import *

"""
setSizePolicy与sizeHint用于布局组件。
"""


class MyButton(QPushButton):
    def sizeHint(self):
        return QSize(200, 36)  # 可以通过MaximumSize与MinimumSize设置


class MyWidget(QWidget):
    def __init__(self, parent=None):
        super().__init__(parent=parent)
        # QBoxLayout
        vlayout = QVBoxLayout()
        vlayout.setContentsMargins(100, 100, 100, 100)
        # vlayout.setSpacing(20)

        for i in range(5):
            btn = MyButton(F'按钮{i}', self)  # QPushButton(F'按钮{i}', self)
            # btn.setGeometry(0, 0, 300, 30)   # 没有效果
            # 变化策略：x方向不变化，y方向尽量占用空间
            btn.setSizePolicy(QSizePolicy.Expanding, QSizePolicy.Expanding)
            vlayout.addWidget(btn)
            # vlayout.addSpacing(i*5)  # 添加固定大小的空距
            # QSpacerItem(int w, int h, QSizePolicy::Policy hPolicy = QSizePolicy::Minimum, QSizePolicy::Policy vPolicy = QSizePolicy::Minimum)
            si = QSpacerItem(10, 5 * i, QSizePolicy.Maximum, QSizePolicy.Minimum)
            vlayout.addSpacerItem(si)  # 添加指定的空距(可以控制变化策略)
            # vlayout.addStretch(5 * i)   # 添加一个可以变化的空距，参数是最小尺寸

        self.setLayout(vlayout)

        # 布局
        self.show()

    def sizeHint(self):
        return QSize(400, 600)


app = QApplication(sys.argv)
wid = MyWidget()
sys.exit(app.exec())
