# coding=utf-8
import os

import cv2
import numpy as np
from kivy.app import App
from kivy.clock import Clock
from kivy.core.window import Window
from kivy.graphics.texture import Texture
from kivy.uix.button import Button
from kivy.uix.gridlayout import GridLayout
from kivy.uix.image import Image
from kivy.uix.label import Label
from kivy.uix.popup import Popup
from kivy.uix.textinput import TextInput


class CameraView(Image):
    classifier = None
    dev = None
    clk = None
    n = 0
    txt_name = None
    btn_ok = None
    popup = None
    user_name = None
    is_Capture = False
    is_Pause: bool = False

    def start(self):
        self.classifier = cv2.CascadeClassifier(
            "data/haarcascade_frontalface_alt2.xml")
        self.dev = cv2.VideoCapture(0)
        self.clk = Clock.schedule_interval(self.capture2show, 1.0 / 10)
        # 弹出对话框
        content = GridLayout(cols=1, rows=4)
        content.add_widget(Label(text='用户名：', size_hint=(1, 0.25)))
        self.txt_name = TextInput(
            text='',
            multiline=False,
            size_hint=(1, 0.25))
        content.add_widget(self.txt_name)
        content.add_widget(Label(text='', size_hint=(1, 0.25)))
        self.btn_ok = Button(
            text='确定',
            size_hint=(1, 0.25))
        content.add_widget(self.btn_ok)
        self.popup = Popup(title='输入用户名',
                           content=content,
                           size_hint=(None, None),
                           size=(600, 400),
                           auto_dismiss=False)
        self.btn_ok.bind(on_release=self.input_ok)
        Window.bind(on_key_down=self.on_key_down)

    def input_ok(self, _):
        self.user_name = self.txt_name.text
        self.popup.dismiss()
        self.n = 0  # 计数置0
        self.is_Capture = True

    def capture2show(self, delaytime):
        # capture
        status, img = self.dev.read()
        if status:
            # 识别
            faces = self.classifier.detectMultiScale(img,
                                                     scaleFactor=1.2,
                                                     minNeighbors=10)
            # 保存图像
            if self.n < 100 and self.is_Capture and not self.is_Pause:
                if len(faces) > 0:
                    face = faces[0]
                    img_face = img[face[1]:face[1] + face[3], face[0]:face[0] + face[2]]
                    img_face = cv2.resize(img_face, (64, 64))
                    if not os.path.exists('images/%s/' % self.user_name):
                        os.makedirs('images/%s/' % self.user_name)
                    cv2.imwrite('images/%s/%02d.png' % (self.user_name, self.n), img_face)
                    self.n += 1
            elif self.n >= 100:
                self.is_Capture = False
            # 特效处理
            kernel = np.array([
                [-1, -1, 0],
                [-1, 0, 1],
                [0, 1, 1]
            ], np.int32)
            img = cv2.filter2D(img, -1, kernel=kernel, delta=180)
            cv2.putText(img=img, text='Delay:%4.2f' % delaytime, org=(10, 30),
                        fontFace=cv2.FONT_HERSHEY_SIMPLEX, fontScale=1,
                        color=(0, 0, 255), thickness=4)
            if self.is_Capture and not self.is_Pause:
                cv2.putText(
                    img=img,
                    text='Capture:%4d' % self.n,
                    org=(1000, 30),
                    fontFace=cv2.FONT_HERSHEY_SIMPLEX,
                    fontScale=1,
                    color=(255, 0, 0), thickness=4)
            else:
                cv2.putText(
                    img=img,
                    text='Capture: Pause',
                    org=(1000, 30),
                    fontFace=cv2.FONT_HERSHEY_SIMPLEX,
                    fontScale=1,
                    color=(0, 0, 255), thickness=4)
            for face in faces:
                # 标示
                cv2.rectangle(img,
                              pt1=(face[0], face[1]),
                              pt2=(face[0] + face[2], face[1] + face[3]),
                              color=(0, 255, 255),
                              thickness=3)
            img = cv2.flip(img, 0)
            # 显示(to texture)
            self.texture = Texture.create(
                size=(img.shape[1], img.shape[0]),
                colorfmt='bgr')
            # 纹理
            self.texture.blit_buffer(img.tostring(),
                                     colorfmt="bgr",
                                     bufferfmt="ubyte")

    # 处理按键事件
    def on_key_down(self, *args):
        if args[1] == ord('g') and 'meta' in args[4]:
            # 弹出对话框，输入姓名
            self.popup.open()
        if args[1] == ord('e') and 'meta' in args[4]:
            self.is_Pause = not self.is_Pause

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
app.title = "人脸数据采集"
Window.fullscreen = 'auto'
app.run()
