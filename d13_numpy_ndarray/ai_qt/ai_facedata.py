#!/usr/bin/python
# coding = utf-8
import os
import sys

import cv2
import numpy as np
from PyQt5.QtCore import *
from PyQt5.QtGui import *
from PyQt5.QtWidgets import *


def emboss(src):
    kernel = np.array([
        [-1, -1, 0],
        [-1, 0, 1],
        [0, 1, 1]
    ], np.int32)

    des = cv2.filter2D(src,  # 被卷积计算的效果
                       -1,  # 输出(在C中是地址，在Python必须是整数,而且是无效地址)
                       kernel=kernel,  # 卷积核
                       delta=180)  # 偏移
    return des


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

        self.classifier = cv2.CascadeClassifier(
            "data/haarcascade_frontalface_alt2.xml")
        self.dev = cv2.VideoCapture(0)
        self.n = 0

        self.timer.timeout.connect(self.capture_video)
        self.timer.start(100)

    def capture_video(self):
        status, img = self.dev.read()
        img = cv2.cvtColor(img, cv2.COLOR_BGR2RGB)

        # --------------------------
        # 扑捉人脸
        faces = self.classifier.detectMultiScale(img,
                                                 scaleFactor=1.2,
                                                 minNeighbors=10)
        # 保存人脸图像
        if len(faces) > 0 and self.n < 100:
            face = faces[0]  # 因简单的原因，只保存第一张图像
            img_face = img[face[1]:face[1] + face[3], face[0]:face[0] + face[2]]
            img_face = cv2.resize(img_face, (64, 64))
            if not os.path.exists('imgdir/'):
                os.makedirs('imgdir/')
            cv2.imwrite('imgdir/img_%02d.png' % self.n, img_face)
            self.n += 1


        # 图像处理
        img = emboss(img)

        # 标识图像
        for face in faces:
            # 标示
            cv2.rectangle(img,
                          pt1=(face[0], face[1]),
                          pt2=(face[0] + face[2], face[1] + face[3]),
                          color=(255, 0, 0),
                          thickness=3)
        cv2.putText(
            img=img,
            text='Capture:%4d' % self.n,
            org=(1000, 30),
            fontFace=cv2.FONT_HERSHEY_SIMPLEX,
            fontScale=1,
            color=(255, 0, 0), thickness=4)

        # --------------------------
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
