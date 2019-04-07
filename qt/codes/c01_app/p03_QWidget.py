# coding = utf-8
import sys

from PyQt5.QtCore import Qt
from PyQt5.QtGui import QCursor, QPixmap, QBitmap, QIcon
from PyQt5.QtWidgets import QApplication, QWidget


class MyWidget(QWidget):
    def __init__(self):
        super().__init__()
        self.setWindowTitle('窗体')
        print(self.windowTitle())

        self.setGeometry(100, 100, 400, 300)
        print(self.size())
        print(self.pos())
        print(self.geometry())

        # 使用内置光标
        # 使用CursorShape类型
        self.setCursor(Qt.ForbiddenCursor)
        self.setCursor(Qt.CursorShape(Qt.ForbiddenCursor))
        self.setCursor(Qt.CursorShape(14))  # 不能直接使用整数14，必须是CursorShape类型或者QCursor类型
        print(Qt.ForbiddenCursor, type(Qt.ForbiddenCursor))
        print(self.cursor(), type(self.cursor()))

        # 使用QCursor类型
        self.setCursor(QCursor(Qt.ForbiddenCursor))
        # 使用图像光标-Bitmap(不支持透明光标)
        bp = QBitmap('ico.png')
        bp = bp.scaled(30, 30)  # 缩小
        self.setCursor(QCursor(bp))

        # 使用图像光标-Pixmap（支持透明）
        px = QPixmap('ico.png')
        px = px.scaled(30, 30)  # 缩小
        self.setCursor(QCursor(px))

        # 图标与图标文本
        self.setWindowIcon(QIcon('ico.png'))
        self.setWindowIconText('图标文本')

        print(self.windowIcon())
        print(self.windowIconText())

        # 窗体状态(全屏，最小化等)
        # self.setWindowState(Qt.WindowFullScreen)
        # self.setWindowState(Qt.WindowMaximized)

        # 窗体标记
        # self.setWindowFlag(Qt.Popup)  # 弹出窗体
        # self.setWindowFlag(Qt.ToolTip)  # 提示窗体
        # self.setWindowFlag(Qt.Drawer)   # 抽屉窗体
        # self.setWindowFlag(Qt.CoverWindow, on=True)

        # 辅助标记一起使用
        # self.setWindowFlags(Qt.CoverWindow | Qt.FramelessWindowHint)
        # 判定标志是否设置
        # flags = self.windowFlags() & Qt.FramelessWindowHint
        # print(int(flags),Qt.FramelessWindowHint)
        # print('设置' if flags == Qt.FramelessWindowHint else '没有设置')

        # self.setWindowOpacity(0.5)

        # self.setToolTip('提示信息在此')
        # self.setToolTipDuration(2000)  # 单位是毫秒，提示信息显示的时间长度


app = QApplication(sys.argv)

widget = MyWidget()
widget.show()

# # wid = QDialog(parent=widget)
# wid = QWidget(parent=widget)
# wid.setWindowFlag(Qt.Dialog)
# print(widget.size())
# wid.setGeometry(
#     (widget.size().width() - 200)/2 + widget.pos().x(),
#     (widget.size().height() - 200)/2 + widget.pos().y(),
#     200, 200)
# wid.setWindowTitle('模式窗体')
# wid.setWindowModality(Qt.ApplicationModal)
# # wid.setWindowModality(Qt.NonModal)
# wid.show()

sys.exit(app.exec())
