import cv2
import numpy as np
from PyQt5.QtGui import *
from PyQt5.QtWidgets import *


class GradientWidget(QWidget):
    def __init__(self):
        super().__init__()
        # 加载图像
        self.img = cv2.imread('flo.jpg')
        self.img = cv2.cvtColor(self.img, cv2.COLOR_BGR2RGB)

        self.lbl_img = QLabel(self)
        w = 800
        h = 600
        l_h = 360
        l_w = 360 * self.img.shape[1] / self.img.shape[0]

        # 窗体大小
        self.resize(w, h)
        # 图像框的大小
        self.lbl_img.setGeometry(
            (w - l_w) / 2,
            (h - l_h) / 2,
            l_w,
            l_h
        )
        self.handle_img()

    def handle_img(self):
        img = self.img
        # 先对图像做一个梯度运算
        # 1. 数组类型转换
        img = img.astype(np.float32)
        img = np.gradient(img, axis=0)
        img = img.astype(np.uint8)
        img += 100
        # 显示图像
        q_img = QImage(
            img,
            img.shape[1],
            img.shape[0],
            img.shape[1] * img.shape[2],
            QImage.Format_RGB888
        )
        q_pix = QPixmap(q_img)

        self.lbl_img.setPixmap(q_pix)
        self.lbl_img.setScaledContents(True)


app = QApplication([])
widget = GradientWidget()
widget.setWindowTitle('Numpy的图像处理')
widget.show()
app.exec()
