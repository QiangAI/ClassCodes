# coding = utf-8
from PyQt5.QtGui import *
from PyQt5.QtWidgets import *
from PyQt5.QtCore import *
from uis.ui_webchatmain import Ui_Form


class WidChatMain(QWidget):
    def __init__(self, chat_):
        super().__init__()
        self.chat = chat_
        self.ui = Ui_Form()
        self.ui.setupUi(self)

        self.__y = 5   # 对话消息的位置

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
        self.and_msg(msg=msg)

    def show_msg(self, msg, user):
        if user == self.current_user:
            self.and_msg(msg=msg, align_left=False)
        # self.setWindowTitle(msg)

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

    # 添加消息到滚动框
    def and_msg(self, msg, align_left=True):
        lbl_msg = QLabel(self.ui.scrollAreaWidgetContents)
        lbl_msg.setText(msg)
        lbl_msg.resize(350, 350)
        lbl_msg.show()
        # 下面代码居右，需要计算字符串长度，调整x位置（这里省略）。
        if align_left:
            print('发送消息',msg)
            lbl_msg.setAlignment(Qt.AlignLeft)
            lbl_msg.move(0, self.__y)
        else:
            print('接收消息',msg)
            lbl_msg.setAlignment(Qt.AlignRight)
            lbl_msg.move(0, self.__y)
        self.__y += 28



