# coding = utf-8
import sys

from PyQt5.QtWidgets import QApplication, QWidget


class MyWidget(QWidget):
    def __init__(self):
        super().__init__()
        self.setWindowTitle('窗体')
        self.setGeometry(100, 100, 400, 300)
        self.setMouseTracking(True)

    def mouseMoveEvent(self, QMouseEvent):
        x = QMouseEvent.x()
        y = QMouseEvent.y()
        # self.setWindowTitle('鼠标位置：(%d,%d)' % (QMouseEvent.pos().x(),QMouseEvent.pos().y()))
        self.setWindowTitle('鼠标位置：(%d,%d)' % (x, y))

    def enterEvent(self, QEvent):
        print('Enter')

    def leaveEvent(self, QEvent):
        print('leave')


app = QApplication(sys.argv)

widget = MyWidget()
widget.show()

sys.exit(app.exec())
