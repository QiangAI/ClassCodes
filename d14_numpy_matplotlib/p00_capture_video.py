import cv2
from PyQt5.QtCore import *
from PyQt5.QtGui import *
from PyQt5.QtWidgets import *


# 1.1. QWidget
class VideoWidget(QWidget):
    line = 0

    # 2.1 实现构造器，创建标签框，用来显示视频
    def __init__(self):
        super().__init__()
        # 读取兔子昂
        self.img = cv2.imread('bea.jpg')
        self.img2 = cv2.imread('flo.jpg')
        self.img = cv2.cvtColor(self.img, cv2.COLOR_BGR2RGB)
        self.img_w = self.img.shape[1]
        self.img_h = self.img.shape[0]
        # 窗体800*600
        # 标签框
        self.resize(800, 600)
        # 2.2. 标签
        self.lbl_img = QLabel(self, text='<font size=20>数据采集中...</font>')
        # 文本与图像居中
        self.lbl_img.setAlignment(Qt.AlignCenter)

        # 大小设置
        h = 500
        w = h * self.img_w / self.img_h
        # print(w,h)
        self.lbl_img.setGeometry((800 - w) / 2, (600 - h) / 2, w, h)
        # -----------------------------
        # 3. 创建定时器
        self.timer = QTimer()
        # 3.1. 定时器绑定的执行函数
        self.timer.timeout.connect(self.capture_video)
        # 3.2.启动定时器
        self.timer.start(100)

        # self.capture_video()

    def capture_video(self):
        # =-----------图像显示
        # print(self.img.shape)
        # self.img[:, :, 0] = 0
        # self.img[:, :, 1] = 0
        # self.img[:, :, 2] = 0
        # self.img[slice(None, None, 2), :, :] = 125
        self.img[:, self.line, :] = self.img2[:, self.line, :]
        if self.line < self.img.shape[1]:
            self.line += 1

        q_img = QImage(
            self.img,  # 被显示的图像数据，是ndarray
            self.img.shape[1],  # 图像宽度
            self.img.shape[0],  # 图像高度
            self.img.shape[1] * 3,  # 每行的图像数据长度
            QImage.Format_RGB888
        )
        q_pix = QPixmap(q_img)
        self.lbl_img.setPixmap(q_pix)
        self.lbl_img.setScaledContents(True)


# 1.2. QApplication
app = QApplication([])
widget = VideoWidget()
widget.show()
app.exec()
