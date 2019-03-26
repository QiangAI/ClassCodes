# coding = utf-8
"""
作用：组合界面，业务封装，形成独立的应用逻辑
"""
from PyQt5.QtCore import *
from helpers.webchathelper import WebChatHelper
from uis.dlgqrlogin import DlgQRLogin
from uis.widchatmain import WidChatMain


class WebChatApp(QObject):
    """
    负责组合登录界面，聊天界面，微信访问模块，形成微信聊天的功能
    """

    def __init__(self):
        super().__init__()

        # 调用辅助类实现登录
        self.chat = WebChatHelper()

        self.ui_login = DlgQRLogin(self.chat)
        self.ui_login.show()
        self.ui_main = WidChatMain(self.chat)
        # self.ui_main.show()
        self.chat.sign_login_ok.connect(self.show_chat_main)
        self.chat.start()  # 辅助类开始工作

    def show_chat_main(self):
        # 隐藏登录
        self.ui_login.hide()
        # 释放登录
        self.ui_login.destroy()
        # 加载用户列表
        self.ui_main.show_user_list()
        # 显示聊天窗体
        self.ui_main.show()
