# coding = utf-8
import sys

import PyQt5.QtGui
import PyQt5.QtWidgets

# def handle_quit():
#     print('退出')
#     # PyQt5.QtWidgets.QApplication.quit()
#     PyQt5.QtWidgets.QApplication.exit(1)
#

app = PyQt5.QtWidgets.QApplication(sys.argv)  # 参数是Qt应用需要使用的命令行参数，没有就是用空里列表

icon = PyQt5.QtGui.QIcon('ico.png')
PyQt5.QtWidgets.QApplication.setWindowIcon(icon)

widget = PyQt5.QtWidgets.QWidget()  # 应用的顶层窗体
widget.setWindowTitle('QT窗体')  # 设置窗体的标题
widget.setGeometry(300, 300, 400, 300)

# button = PyQt5.QtWidgets.QPushButton('使用代码退出', widget)
# button.setGeometry(140, 135, 120, 30)
# button.clicked.connect(handle_quit)

widget.show()  # 显示窗体

status = app.exec()  # 进入消息监控，并处理消息等
# print('应用返回状态：', status)
# # status = 1
sys.exit(status)
