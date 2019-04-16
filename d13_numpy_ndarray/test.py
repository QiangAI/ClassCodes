#!/usr/bin/python
# coding = utf-8
import sys

import cv2
from PyQt5.QtCore import *
from PyQt5.QtGui import *
from PyQt5.QtWidgets import *


class MainWidget(QWidget):
    def __init__(self):
        super(MainWidget, self).__init__()
        self.timer = QTimer()
        # 窗体初始化
        screen = QApplication.desktop()
        screen_w = screen.width()
        screen_h = screen.height()
        self.setWindowFlags(
            Qt.CustomizeWindowHint |
            Qt.WindowMinimizeButtonHint |
            Qt.WindowCloseButtonHint
        )
        # self.setWindowState(Qt.WindowFullScreen)
        self.setGeometry(
            (screen_w - 800) / 2, (screen_h - 600) / 2,
            800, 600)
        # 显示视频图像
        self.lbl_qr = QLabel(self, text='<font size=20>视频采集中...</font>')
        self.lbl_qr.setAlignment(Qt.AlignCenter)
        self.lbl_qr.setGeometry((800 - 640) / 2, (600 - 360) / 2, 640, 360)
        self.show()

        self.dev = cv2.VideoCapture(0)

        self.timer.timeout.connect(self.capture_video)
        self.timer.start(100)

    def capture_video(self):
        status, img = self.dev.read()
        img = cv2.cvtColor(img, cv2.COLOR_BGR2RGB)
        image = QImage(img,  # 图像的子节数组(numpy.ndarray)
                       img.shape[1],  # 图像高度
                       img.shape[0],  # 图像宽度
                       img.shape[1] * 3,  # 每行的字节数
                       QImage.Format_RGB888)  # 图像的格式3个子节
        png1 = QPixmap(image)
        self.lbl_qr.setPixmap(png1)
        self.lbl_qr.setScaledContents(True)


app = QApplication(sys.argv)
ui_main = MainWidget()
sys.exit(app.exec())
