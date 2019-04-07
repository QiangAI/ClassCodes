import sys

from PyQt5.QtCore import *
from PyQt5.QtWidgets import *


class MyWidget(QWidget):
    def __init__(self, parent=None):
        super().__init__(parent=parent)
        # QBoxLayout
        flayout = QFormLayout()
        flayout.setContentsMargins(100, 50, 100, 50)
        flayout.setFormAlignment(Qt.AlignCenter)
        flayout.setFieldGrowthPolicy(QFormLayout.ExpandingFieldsGrow)

        edt_username = QLineEdit(self)
        flayout.addRow('用户:', edt_username)
        edt_password = QLineEdit(self)
        flayout.addRow('暗号:', edt_password)

        # 嵌套布局
        glayout = QGridLayout()
        glayout.setContentsMargins(30, 30, 30, 30)
        btn_submit = QPushButton('登录', self)
        btn_cancel = QPushButton('取消', self)

        glayout.addWidget(btn_submit, 0, 0)
        glayout.addWidget(btn_cancel, 0, 1)
        flayout.addRow(glayout)

        self.setLayout(flayout)

        # 布局
        self.show()

    def sizeHint(self):
        return QSize(400, 200)


app = QApplication(sys.argv)
wid = MyWidget()
sys.exit(app.exec())
