from PyQt5.QtWidgets import *

"""
负责翻译器的界面
    |- 聚合翻译类一起工作
"""


class UiTranslator(QWidget):
    def __init__(self, tr):
        super().__init__()
        self.translator = tr

        # 窗体的属性
        self.setWindowTitle('马哥牌翻译器')
        self.setGeometry(400, 200, 400, 300)
        # 文本输入框（输入需要翻译的单词）
        self.edt_keyword = QLineEdit(self)
        self.edt_keyword.setGeometry(10, 10, 250, 30)

        # 按钮（事件提交）
        self.btn_translate = QPushButton(self)
        self.btn_translate.setText('翻译')
        self.btn_translate.setGeometry(270, 10, 120, 30)

        # 标签框（显示结果）
        self.lbl_info = QLabel(self)
        self.lbl_info.setGeometry(10, 50, 380, 250)
        self.lbl_info.setText('翻译结果')
        # self.lbl_info.setAlignment(Qt.AlignTop)

        # 处理事件
        self.btn_translate.clicked.connect(self.baidu_translate)

    def baidu_translate(self):
        # 获取文本
        str_keyword = self.edt_keyword.text()
        # 调用翻译器
        result = self.translator.translate(str_keyword)
        print('返回结果:', result)
        # 显示结果(处理显示结果)
        self.lbl_info.setText('文本')
