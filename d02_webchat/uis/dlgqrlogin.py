# coding = utf-8
from PyQt5.QtGui import *
from PyQt5.QtWidgets import *
from uis.ui_login import Ui_ui_login


class DlgQRLogin(QDialog):
    """
    二维码登录对话框
    """

    def __init__(self, chat_):
        super().__init__()
        self.chat = chat_
        self.ui = Ui_ui_login()
        self.ui.setupUi(self)

        # 接收二维码
        self.chat.sign_qr.connect(self.show_qr)

    def show_qr(self, qrcode):
        img_qr = QImage.fromData(qrcode)
        pix_qr = QPixmap.fromImage(img_qr)
        self.ui.lbl_qr.setPixmap(pix_qr)
        self.ui.lbl_qr.setScaledContents(True)
