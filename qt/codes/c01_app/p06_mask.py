# coding = utf-8
import sys

from PyQt5.QtGui import QPixmap, QPainter, QBitmap
from PyQt5.QtWidgets import QWidget, QApplication


class MaskWidget(QWidget):  # 不规则窗体
    def __init__(self, parent=None):
        super(MaskWidget, self).__init__(parent)
        self.setWindowTitle('遮罩的使用')
        bp = QBitmap('pic.png')  # 遮罩图（黑白二色）
        bp = bp.scaled(423, 300)  # 图像太大，缩放一下，缩放后图像类型成为QPixmap类型
        self.bp = QBitmap(bp)  # 遮罩智能使用QBitmap类型
        self.setMask(self.bp)

    def paintEvent(self, QPaintEvent):  # 绘制窗口
        paint = QPainter(self)
        tu = QPixmap('scenery.jpg')  # 被绘制的图像，绘制结果被遮罩影响
        # tu = tu.scaled(423, 300)   # 图样根据窗体大小缩放下
        # 绘制图像，该图像的绘制会被遮罩影响
        paint.drawPixmap(0, 0, self.bp.width(), self.bp.height(), tu)


app = QApplication(sys.argv)
widget = MaskWidget()
widget.setGeometry(300, 300, 423, 300)
widget.show()
sys.exit(app.exec())
