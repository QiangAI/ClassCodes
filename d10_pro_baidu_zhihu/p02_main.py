import sys

import baidu.baiduapp
from PyQt5.QtWidgets import QApplication

"""
    功能：启动百度翻译器应用模块
    作者：Louis Young
    日期：2019-04-10
"""

qt = QApplication(sys.argv)
app = baidu.baiduapp.BaiduApp()
app.start()
sys.exit(qt.exec())
