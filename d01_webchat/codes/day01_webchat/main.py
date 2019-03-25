# coding = utf-8
import sys

import app.webchatapp
from PyQt5.QtWidgets import *

qt_app = QApplication(sys.argv)
webchat = app.webchatapp.WebChatApp()
sys.exit(qt_app.exec())
