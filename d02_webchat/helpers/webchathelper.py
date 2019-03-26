# coding = utf-8
import itchat
from PyQt5.QtCore import *


class WebChatHelper(QThread):
    sign_qr = pyqtSignal(bytes)
    sign_login_ok = pyqtSignal()
    sign_coming_msg = pyqtSignal(str)

    def __init__(self):
        super().__init__()

    def run(self):
        print('开始登录')

        @itchat.msg_register(msgType=itchat.content.TEXT, isGroupChat=True)
        def recv_msg(msg):
            if msg['MsgType'] == 1:
                self.sign_coming_msg.emit(msg['Content'])

        # 登录
        itchat.login(
            qrCallback=self.qr_callback,
            loginCallback=self.login_callback)

        itchat.run()

    def qr_callback(self, uuid, status, qrcode):
        # if status == 0:
        self.sign_qr.emit(qrcode)

    def login_callback(self):
        print('登录成功')
        self.sign_login_ok.emit()

    def get_friends(self):
        lst_user = []
        friends = itchat.get_chatrooms()
        for friend_ in friends:
            user = {}
            user['NickName'] = friend_['NickName']
            user['UserName'] = friend_['UserName']
            lst_user.append(user)
        return lst_user

    def send_msg(self, user_, msg_):
        itchat.send_msg(msg=msg_, toUserName=user_)
