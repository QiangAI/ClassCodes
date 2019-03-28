import sys

from PyQt5.QtWidgets import QApplication
from translators.transapp import TransApp

"""
程序入口
"""
app = QApplication(sys.argv)
trans_app = TransApp()
sys.exit(app.exec())
