# 显示图像
import cv2
import numpy as np
from PyQt5.QtCore import *
from PyQt5.QtGui import *
from PyQt5.QtWidgets import *


# 创建一个窗体应用
# 1.1.定义窗体
class NDArrayWidget(QWidget):
    weight = 0.0

    def __init__(self):
        super().__init__()
        # 加载2个图像
        self.img1 = cv2.imread('bea.jpg')
        self.img2 = cv2.imread('flo.jpg')
        self.img1 = cv2.cvtColor(self.img1, cv2.COLOR_BGR2RGB)
        self.img2 = cv2.cvtColor(self.img2, cv2.COLOR_BGR2RGB)

        win_w = 800
        win_h = 600
        self.resize(win_w, win_h)
        # 创建标签框架显示

        lbl_h = 360
        lbl_w = 360 * self.img1.shape[1] / self.img1.shape[0]
        self.lbl_img = QLabel(self)
        self.lbl_img.setGeometry(
            (win_w - lbl_w) / 2,
            (win_h - lbl_h) / 2,
            lbl_w, lbl_h)

        # 定时器
        self.timer = QTimer()
        self.timer.timeout.connect(self.handle_image_show)
        self.timer.start(100)

    def handle_image_show(self):
        # 1. 转换成QImage
        # img = np.zeros_like(self.img1, dtype=np.uint8)
        # 两幅图像的元素使用加权和，动画改变权重系统
        img = (self.weight * self.img1 + (1 - self.weight) * self.img2).astype(np.uint8)
        # print(self.weight)
        if self.weight < 1.0:
            self.weight += 0.01

        q_img = QImage(
            img,
            img.shape[1],
            img.shape[0],
            img.shape[1] * img.shape[2],
            QImage.Format_RGB888
        )
        # 2. 转换像素图QPixamp
        pix_img = QPixmap(q_img)
        # 3. 标签显示
        self.lbl_img.setPixmap(pix_img)
        self.lbl_img.setScaledContents(True)


# 1.2. 利用窗体创建应用
app = QApplication([])

nd = NDArrayWidget()
nd.show()

app.exec()
