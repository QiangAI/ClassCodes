# 显示图像
import cv2
import numpy as np
from PyQt5.QtGui import *
from PyQt5.QtWidgets import *


# 创建一个窗体应用
# 1.1.定义窗体
class NDArrayWidget(QWidget):
    weight = 0.0

    def __init__(self):
        super().__init__()
        # 加载2个图像
        self.img1 = cv2.imread('digit.jpg')
        self.img1 = cv2.cvtColor(self.img1, cv2.COLOR_BGR2RGB)

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
        self.handle_image_show()

    def handle_image_show(self):
        img = self.img1
        # img = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)  # 可以不做灰度处理
        # img = np.gradient(img, axis=1)
        img = img.astype(np.float32)
        img = np.gradient(img, axis=0)
        # img = (img[0] + img[1])
        img = img.astype(np.uint8)
        img += 120
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
nd.setWindowTitle('Numpy在图像中应用')
nd.show()

app.exec()
