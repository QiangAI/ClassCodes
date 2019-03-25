# coding = utf-8

import uis.ui_login
from PyQt5.QtCore import *
from PyQt5.QtWidgets import *


class DlgQRLogin(QDialog):

    def __init__(self, chat_, parent=None):
        super().__init__(parent=parent)
        self.chat = chat_
        self.ui_login = uis.ui_login.Ui_ui_login()
        self.ui_login.setupUi(self)

        self.setWindowFlags(Qt.CustomizeWindowHint)

        # self.show()

# app = QApplication([])    # (sys.argv)
#
# dlg = DlgQRLogin()
#
# app.exec()
