# coding = utf-8
from PyQt5.QtGui import *
from PyQt5.QtWidgets import *
from uis.ui_webchatmain import Ui_Form


class WidChatMain(QWidget):
    def __init__(self, chat_):
        super().__init__()
        self.chat = chat_
        self.ui = Ui_Form()
        self.ui.setupUi(self)

        # 处理chat发送过来的信号
        self.chat.sign_coming_msg.connect(self.show_msg)

        # 添加模式
        self.model = QStandardItemModel()
        self.ui.listView.setModel(self.model)

        # 绑定信号处理
        self.ui.listView.clicked.connect(self.select_user)
        # 点击信息
        self.ui.pushButton.clicked.connect(self.send_msg)

    def select_user(self, index):
        # 获取当前用户
        row = index.row()
        self.current_user = self.model.item(row).data()  # 绑定模型中不显示的数据

    def send_msg(self):
        # 获取文本信息
        msg = self.ui.lineEdit.text()
        # 发送(辅助类)
        self.chat.send_msg(self.current_user, msg)  # 判定下用户是否选择

    def show_msg(self, msg):
        self.setWindowTitle(msg)

    def show_user_list(self):
        # 调用辅助类获取列表
        lst_users = self.chat.get_friends()
        # 显示列表到列表框
        for user_ in lst_users:
            user_name = user_['UserName']  # 发送的使用用户ID
            nick_name = user_['NickName']  # 显示
            icon_head = QIcon('imgs/user.jpg')
            item_ = QStandardItem(icon_head, nick_name)
            item_.setData(user_name)
            self.model.appendRow(item_)
