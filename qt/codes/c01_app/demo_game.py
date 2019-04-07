# coding = utf-8
import sys

from PyQt5.QtCore import *
from PyQt5.QtGui import *
from PyQt5.QtWidgets import *


class QFish(QThread):
    update = pyqtSignal()
    x = 200  # 根据窗体大小设置，这个可以随意
    y = 200
    size = 100
    color = QColor(255, 0, 0)
    mouth = 45

    is_open = False

    def run(self):
        while True:
            if self.is_open:
                self.mouth += 1
                if self.mouth >= 45:
                    self.mouth = 45
                    self.is_open = not self.is_open
            else:
                self.mouth -= 1
                if self.mouth <= 0:
                    self.mouth = 0
                    self.is_open = not self.is_open
            # 发送窗体刷新信号
            self.update.emit()
            QThread.msleep(100)  # 单位毫秒


class SceneWidget(QWidget):
    def __init__(self):
        super().__init__()
        self.fish = QFish()
        self.setGeometry(100, 100, 500, 500)
        self.setWindowFlags(Qt.CustomizeWindowHint)

        self.fish.update.connect(self.repaint)
        self.fish.start()

    def paintEvent(self, QPaintEvent):
        # 通过绘制事件的参数，获得绘制区域
        rect = QPaintEvent.rect()  # 根据需要使用
        painter = QPainter(self)
        # 绘制大嘴鱼（一个弧形）
        # drawArc(
        #       int x, int y,
        #       int width, int height,
        #       int startAngle,
        #       int spanAngle)      # 角度采用的单位是1/16℃，不是使用的弧度
        painter.setPen(QPen(self.fish.color,
                            4.0,
                            Qt.DashDotDotLine,
                            Qt.RoundCap,
                            Qt.BevelJoin))
        path = QPainterPath()

        painter.drawPie(self.fish.x, self.fish.y,
                        self.fish.size, self.fish.size,
                        self.fish.mouth * 16,
                        (360 - self.fish.mouth * 2) * 16)


app = QApplication(sys.argv)

widget = SceneWidget()
widget.show()

sys.exit(app.exec())
