# 显示图像
import cv2
from PyQt5.QtGui import *
from PyQt5.QtWidgets import *


# 创建一个窗体应用
# 1.1.定义窗体
class NDArrayWidget(QWidget):

    def __init__(self):
        super().__init__()
        # 加载2个图像
        self.img1 = cv2.imread('bea.jpg')
        self.img2 = cv2.imread('flo.jpg')
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
        # 1. 转换成QImage
        img = self.img1
        # 数组的运算
        for h in range(img.shape[0]):  # 高度
            for w in range(img.shape[1]):  # 宽度
                # for d in range(img.shape[2]-1): # 图形深度
                # img[h, w, 0] = 0
                # img[h][w][0] = 0
                a = img[h, w, 0] // 3 + img[h, w, 1] // 3 + img[h, w, 2] // 3
                img[h, w, 0] = a
                img[h, w, 1] = a
                img[h, w, 2] = a

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
