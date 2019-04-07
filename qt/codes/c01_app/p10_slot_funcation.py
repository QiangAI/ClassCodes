# coding = utf-8
import sys

from PyQt5.QtWidgets import QApplication, QWidget, QPushButton

# def handel_click():
# widget.setWindowTitle('参数：{checked_}'.format(checked_=checked_))
# widget.setWindowTitle('参数：%(checked_)s' % {'checked_': checked_})
# widget.close()


app = QApplication(sys.argv)

widget = QWidget()
widget.setGeometry(100, 100, 300, 300)
button = QPushButton(parent=widget, text='信号与槽')
# button.clicked.connect(handel_click)
button.clicked.connect(widget.close)

widget.show()

sys.exit(app.exec())
