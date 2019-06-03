import sys

import itchat
from PyQt5.QtCore import *
from PyQt5.QtGui import *
from PyQt5.QtWidgets import *


class WebChatHelper(QThread):
    # 成员数据
    login_uuid = None

    # 定义信号
    qr = pyqtSignal(bytes)  # 发送登录二维码信号
    login = pyqtSignal()  # 发送登录成功信号
    chatrooms = pyqtSignal(list)  # 发送聊天室列表信号

    msg = pyqtSignal(str)

    # 线程任务运行函数
    def run(self):
        @itchat.msg_register(itchat.content.INCOME_MSG, isFriendChat=True, isGroupChat=True, isMpChat=True)
        def recv_msg(msg):
            self.msg.emit(msg['Content'])

        # 登录
        itchat.auto_login(
            hotReload=False,
            qrCallback=self.qr_call,  # 登录二维码下载回调函数设置
            loginCallback=self.login_call)  # 登录成功回调函数设置

        # 初始化加载聊天室列表
        chatroom_list = itchat.get_chatrooms()  # get_friends(update=False)
        self.chatrooms.emit(chatroom_list)

        # 这个线程持续与保持微信登录状态
        itchat.run()
        # 微信登录二维码回调函数

    # 登录过程回调：二维码下载回调函数
    def qr_call(self, uuid, status, qrcode):
        self.login_uuid = uuid  # 保存登录产生的UUID
        # 二进制打开文件
        if status == '0':
            print('发送登录二维码信号')
        self.qr.emit(qrcode)

    # 登录过程回调：登录成功回调函数
    def login_call(self):
        # check_login会导致重新登录
        # if itchat.check_login(uuid=self.login_uuid) == '200':  # 检测UUID是否登录成功
        #     print('发送登录成功信号')
        self.login.emit()

    # 发送消息
    def seng_msg(self, msg_, user_):
        r = itchat.send_msg(msg_, user_)
        print(r)


# 二维码窗体
class LoginDialog(QDialog):
    main_show = pyqtSignal()

    # 初始化窗体
    def __init__(self, chat, parent=None):
        super().__init__(parent=parent)
        self.chat = chat
        # 居中
        screen = QApplication.desktop()
        screen_w = screen.width()
        screen_h = screen.height()

        self.setWindowFlags(Qt.CustomizeWindowHint)
        self.setGeometry(
            (screen_w - 400) / 2, (screen_h - 400) / 2,
            400, 400)
        self.lbl_qr = QLabel(self, text='<font size=20>加载二维码中...</font>')
        self.lbl_qr.setAlignment(Qt.AlignCenter)
        self.lbl_qr.setGeometry(0, 0, 400, 400)
        self.chat.qr.connect(self.show_qr)
        self.chat.login.connect(self.login_ok)

    # 接受二维码，并显示
    def show_qr(self, qrcode):
        img_qr = QImage.fromData(qrcode)
        pix_qr = QPixmap.fromImage(img_qr)
        self.lbl_qr.setPixmap(pix_qr)
        self.lbl_qr.setScaledContents(True)

    def login_ok(self):
        print('显示聊天窗体')
        self.hide()
        self.main_show.emit()
        self.close()  # 关闭
        self.destroy()  # 释放


# 微信聊天窗体
class MainWidget(QWidget):
    def __init__(self, chat):
        super().__init__()
        self.chat = chat
        # 窗体初始化
        screen = QApplication.desktop()
        screen_w = screen.width()
        screen_h = screen.height()
        self.setWindowFlags(
            Qt.CustomizeWindowHint |
            Qt.WindowMinimizeButtonHint |
            Qt.WindowCloseButtonHint
        )
        self.setGeometry(
            (screen_w - 800) / 2, (screen_h - 600) / 2,
            800, 600)
        # 显示用户的列表框
        self.lst_users = QListView(self)
        self.mod_users = QStandardItemModel()
        self.lst_users.setGeometry(0, 0, 300, 600)
        self.lst_users.setModel(self.mod_users)
        self.chat.chatrooms.connect(self.show_chatroom_list)
        self.lst_users.clicked.connect(self.select_user)
        self.chat.msg.connect(self.recv_msg)

    def show_chatroom_list(self, chatrooms_):
        for room in chatrooms_:
            room_item = QStandardItem(QIcon('user.jpg'), room["NickName"])
            room_item.setData(room['UserName'])
            self.mod_users.appendRow(room_item)

    def select_user(self, index):
        # 返回选择的行
        row = index.row()
        # 获取用户名：userName
        self.current_user = [
            self.mod_users.item(row).data(),
            index.data()
        ]
        print("选择用户：", self.current_user)
        # 发送消息
        print('消息发送：', self.current_user[0])
        self.chat.seng_msg('测试', self.current_user[0])

    def recv_msg(self, msg):
        self.setWindowTitle(msg)


# 业务应用
class WebChatApp(QObject):
    # 获取当前用户（微信序列，用户昵称）
    current_user = None

    # 构造器
    def __init__(self):
        super().__init__()
        # 微信模块
        self.web_chat = WebChatHelper()
        # 二维码窗体
        self.ui_login = LoginDialog(self.web_chat)
        # 微信聊天窗体
        self.ui_main = MainWidget(self.web_chat)
        self.ui_login.main_show.connect(self.ui_main.show)
        self.ui_login.show()
        self.ui_main.hide()
        self.web_chat.start()


# 使用下面这个if，可以独立运行，也可以作为模块调用
if __name__ == '__main__':
    qt_app = QApplication(sys.argv)
    app = WebChatApp()
    status = qt_app.exec()
    sys.exit(status)
