#!/usr/bin/python
# coding=utf-8
import cv2
import numpy as np
from PIL import Image as PILImage, ImageDraw, ImageFont
from cnn import *
from facepreprocess import FacePreprocess
from kivy.app import App
from kivy.clock import Clock
from kivy.core.window import Window
from kivy.graphics.texture import Texture
from kivy.uix.image import Image


class CameraView(Image):
    classifier = None
    dev = None
    clk = None
    n = 0
    model_path = 'models/face.model'
    session = None
    target_dict = None
    predict = None

    def start(self):
        self.predict = tf.argmax(y_, 1)
        pp = FacePreprocess('images/', 'trains/')
        self.target_dict = pp.get_target_dict()
        self.classifier = cv2.CascadeClassifier(
            "data/haarcascade_frontalface_alt2.xml")
        self.dev = cv2.VideoCapture(0)
        self.clk = Clock.schedule_interval(self.capture2show, 1.0 / 10)
        #  读取训练的明模型
        saver = tf.train.Saver()
        self.session = tf.Session()
        saver.restore(self.session, self.model_path)

    def capture2show(self, delaytime):
        # capture
        status, img = self.dev.read()
        if status:
            # 识别
            faces = self.classifier.detectMultiScale(img,
                                                     scaleFactor=1.2,
                                                     minNeighbors=10)
            # 特效处理
            # kernel = np.array([
            #     [-1, -1, 0],
            #     [-1, 0, 1],
            #     [0, 1, 1]
            # ], np.int32)
            # img = cv2.filter2D(img, -1, kernel=kernel, delta=180)
            cv2.putText(img=img, text='Delay:%4.2f' % delaytime, org=(10, 30),
                        fontFace=cv2.FONT_HERSHEY_SIMPLEX, fontScale=1,
                        color=(0, 0, 255), thickness=4)
            cv2.putText(
                img=img,
                text='Recognizing...',
                org=(1000, 30),
                fontFace=cv2.FONT_HERSHEY_SIMPLEX,
                fontScale=1,
                color=(255, 0, 0), thickness=4)

            if len(faces) > 0:
                face = faces[0]
                # 识别，并标识
                img_face = img[face[1]:face[1] + face[3], face[0]:face[0] + face[2]]
                img_face = cv2.resize(img_face, (32, 32))
                result = self.session.run(self.predict, feed_dict={x: [img_face]})
                # print(result)
                print(self.target_dict[result[0]])
                cv2.rectangle(img,
                              pt1=(face[0] - 40, face[1] - 40),
                              pt2=(face[0] + face[2] + 40, face[1] + face[3] + 40),
                              color=(0, 255, 255),
                              thickness=3)
                # cv2和PIL中颜色的hex码的储存顺序不同
                cv2img = cv2.cvtColor(img, cv2.COLOR_BGR2RGB)
                pilimg = PILImage.fromarray(cv2img)
                draw = ImageDraw.Draw(pilimg)  # 图片上打印
                # 参数1：字体文件路径，参数2：字体大小
                font = ImageFont.truetype("msyh.ttf", 36, encoding="utf-8")
                # 参数1：打印坐标，参数2：文本，参数3：字体颜色，参数4：字体
                draw.text((face[0], face[1] - 120), self.target_dict[result[0]], (255, 0, 0), font=font)
                img = cv2.cvtColor(np.array(pilimg), cv2.COLOR_RGB2BGR)
                # cv2.putText(
                #    img=img,
                #    text=self.target_dict[result[0]],
                #    org=(face[0] + 20, face[1] - 60),
                #    fontFace=cv2.FONT_HERSHEY_SIMPLEX,
                #    fontScale=1,
                #    color=(0, 0, 255), thickness=4)
            img = cv2.flip(img, 0)

            # 显示(to texture)
            self.texture = Texture.create(
                size=(img.shape[1], img.shape[0]), colorfmt='bgr')
            # 纹理
            self.texture.blit_buffer(img.tostring(),
                                     colorfmt="bgr",
                                     bufferfmt="ubyte")

    def close(self):
        # close camera
        Clock.unschedule(self.clk)
        if self.dev and self.dev.isOpened():
            self.dev.release()


class AiApp(App):
    view = None

    def build(self):
        self.view = CameraView()
        return self.view

    # 启动摄像头
    def on_start(self):
        self.view.start()

    # 关闭摄像头
    def on_stop(self):
        self.view.close()


app = AiApp()
app.title = "人脸识别"
Window.fullscreen = 'auto'
app.run()
