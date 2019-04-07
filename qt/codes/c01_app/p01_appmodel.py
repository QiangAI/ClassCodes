# coding = utf-8
import PyQt5.QtWidgets

app = PyQt5.QtWidgets.QApplication([])  # 参数是Qt应用需要使用的命令行参数，没有就是用空里列表
widget = PyQt5.QtWidgets.QWidget()  # 应用的顶层窗体
widget.setWindowTitle('QT窗体')  # 设置窗体的标题
widget.show()  # 显示窗体
status = app.exec()  # 进入消息监控，并处理消息等
