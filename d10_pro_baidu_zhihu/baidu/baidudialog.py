from PyQt5.QtWidgets import *

"""
    功能：实现百度翻译的界面（纯粹模仿百度翻译页面）
    作者：Louis Young
    日期：2019-04-10
"""


class BaiduDialog(QDialog):

    def __init__(self, crawler, parent=None):
        super().__init__(parent=parent)
        self.__crawler = crawler

        # ----------设计与构建UI界面开始
        # 设计布局
        layout_outer = QVBoxLayout()

        layout_layer1 = QHBoxLayout()
        layout_layer2 = QGridLayout()
        # layout_layer3 = QGridLayout()

        layout_outer.addLayout(layout_layer1)
        layout_outer.addLayout(layout_layer2)
        # layout_outer.addLayout(layout_layer3)

        self.setLayout(layout_outer)

        # 添加组件
        self.edt_english = QLineEdit('英文', self)
        self.edt_english.setEnabled(False)
        self.btn_exchange = QPushButton('<->', self)
        self.edt_chinese = QLineEdit('中文', self)
        self.edt_chinese.setEnabled(False)
        # self.setSizePolicy(QSizePolicy.Preferred,QSizePolicy.Preferred)
        self.btn_translate = QPushButton('翻译', self)

        layout_layer1.addWidget(self.edt_english)
        self.edt_english.setMinimumSize(80, 0)
        layout_layer1.addWidget(self.btn_exchange)
        layout_layer1.addWidget(self.edt_chinese)
        self.edt_chinese.setMinimumSize(80, 0)
        layout_layer1.addSpacing(50)
        layout_layer1.addWidget(self.btn_translate)

        self.edt_input = QTextEdit(self)
        # self.edt_input.setMaximumSize(0, 200)
        self.edt_output = QTextEdit(self)
        # self.edt_output.setMaximumSize(0, 200)
        self.edt_output.setEnabled(False)

        layout_layer2.addWidget(self.edt_input, 0, 0)
        layout_layer2.addWidget(self.edt_output, 0, 1)

        self.scr_info = QScrollArea(self)
        self.scr_info.setMinimumSize(0, 200)
        # layout_layer3.addWidget(self.scr_info, 0, 0)
        # layout_layer3.addWidget(QLabel(self), 0, 1)
        layout_layer2.addWidget(self.scr_info, 1, 0)

        self.setWindowTitle('百度翻译神器')
        # ----------设计与构建UI界面完毕

        # 绑定事件
        self.btn_translate.clicked.connect(self.translate)

    # 槽（slot）函数
    def translate(self):
        print('开始翻译')
        kw = self.edt_input.toPlainText()
        re_translate = self.__crawler.v2transapi(kw)
        print(re_translate['output'])
        # self.edt_output.setPlainText()
        self.edt_output.setText(re_translate['output'])
        self.edt_output.repaint()
