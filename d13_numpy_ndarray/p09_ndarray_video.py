import cv2
from PyQt5.QtCore import *
from PyQt5.QtGui import *
from PyQt5.QtWidgets import *


# 1.1. QWidget
class VideoWidget(QWidget):
    # 2.1 实现构造器，创建标签框，用来显示视频
    def __init__(self):
        super().__init__()
        # 窗体800*600
        # 标签框
        self.resize(800, 600)
        # 2.2. 标签
        self.lbl_img = QLabel(self, text='<font size=20>数据采集中...</font>')
        # 文本与图像居中
        self.lbl_img.setAlignment(Qt.AlignCenter)
        # 大小设置
        self.lbl_img.setGeometry((800 - 640) / 2, (600 - 360) / 2, 640, 360)
        # -----------------------------
        # 4.1.创建设备
        self.dev_video = cv2.VideoCapture(0)  # 驱动摄像头
        # -----------------------------
        # 3. 创建定时器
        self.timer = QTimer()
        # 3.1. 定时器绑定的执行函数
        self.timer.timeout.connect(self.capture_video)
        # 3.2.启动定时器
        self.timer.start(100)

    def capture_video(self):
        # 4.2
        status, img = self.dev_video.read()
        img = cv2.cvtColor(img, cv2.COLOR_BGR2RGB)
        if status:
            pass  # 图像显示
            # =-----------图像显示
            q_img = QImage(
                img,  # 被显示的图像数据，是ndarray
                img.shape[1],  # 图像宽度
                img.shape[0],  # 图像高度
                img.shape[1] * 3,  # 每行的图像数据长度
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
