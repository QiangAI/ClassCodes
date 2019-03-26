# coding = utf-8
"""
作者：Louis Young
作用：启动应用
"""
import sys

from PyQt5.QtWidgets import QApplication
from apps.webchatapp import WebChatApp

web_app = QApplication(sys.argv)
chat_app = WebChatApp()
sys.exit(web_app.exec())
