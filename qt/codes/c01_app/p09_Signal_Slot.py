# coding = utf-8
import sys

from PyQt5.QtCore import pyqtSlot, pyqtSignal, Qt
from PyQt5.QtWidgets import QApplication, QWidget, QDialog


class MyWidget(QWidget):

    def __init__(self):
        super().__init__()
        self.setWindowTitle('窗体')
        self.setGeometry(100, 100, 400, 400)
        self.setMouseTracking(True)

    @pyqtSlot(int, int)
    def show_pos_in_title(self, x, y):
        self.setWindowTitle('鼠标位置：(%d,%d)' % (x, y))

    def mouseMoveEvent(self, QMouseEvent):
        # 只有对话框关闭，这个时间才能触发
        x = QMouseEvent.x()
        y = QMouseEvent.y()
        print(x, y)


class LoginDialog(QDialog):
    # showPos
    showPos = pyqtSignal(int, int)  # 参数用来传递鼠标位置

    # 初始化窗体
    def __init__(self, parent=None):
        super(QDialog, self).__init__(parent=parent)
        self.setGeometry(200, 200, 200, 200)
        self.setMouseTracking(True)
        self.setWindowModality(Qt.ApplicationModal)

    def mouseMoveEvent(self, QMouseEvent):
        x = QMouseEvent.x()
        y = QMouseEvent.y()
        self.showPos.emit(x, y)


app = QApplication(sys.argv)

widget = MyWidget()
dialog = LoginDialog()
dialog.showPos.connect(widget.show_pos_in_title)
widget.show()
dialog.show()

sys.exit(app.exec())
