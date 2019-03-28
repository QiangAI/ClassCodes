from PyQt5.QtCore import QObject
from translators.transfrombaidu import BaiDuTranslator
from translators.uitrans import UiTranslator
"""
翻译应用的组合
    |- UI
    |- 百度翻译的功能
"""


class TransApp(QObject):
    def __init__(self):
        super().__init__()
        self.translator = BaiDuTranslator()
        self.ui = UiTranslator(self.translator)
        self.ui.show()

