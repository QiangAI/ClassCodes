# coding = utf-8

from PyQt5.QtWidgets import *
from uis.ui_webchatmain import *


class WidWebChatMain(QWidget):

    def __init__(self, chat_, parent=None):
        super().__init__(parent=parent)
        self.chat = chat_
        self.ui_main = Ui_Form()
        self.ui_main.setupUi(self)
        # self.show()

# app = QApplication(sys.argv)
#
# ui_main = WidWebChatMain()
#
# sys.exit(app.exec())
