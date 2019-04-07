import sys

from PyQt5.QtCore import *
from PyQt5.QtWidgets import *


class MyWidget(QWidget):
    def __init__(self, parent=None):
        super().__init__(parent=parent)
        # QBoxLayout
        flayout = QFormLayout()
        flayout.setContentsMargins(100, 50, 100, 50)

        edt_username = QLineEdit(self)
        flayout.addRow('用户:', edt_username)
        edt_password = QLineEdit(self)
        flayout.addRow('暗号:', edt_password)

        self.setLayout(flayout)

        # 布局
        self.show()

    def sizeHint(self):
        return QSize(400, 200)


app = QApplication(sys.argv)
wid = MyWidget()
sys.exit(app.exec())
