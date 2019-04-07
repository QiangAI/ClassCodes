# coding = utf-8
import sys

from PyQt5.QtWidgets import \
    QApplication, \
    QWidget, \
    QPushButton, \
    QStyleFactory

app = QApplication(sys.argv)

# 内置样式
print(QStyleFactory.keys())  # ['macintosh', 'Windows', 'Fusion']
style = QStyleFactory.create('Fusion')
print(style)

widget = QWidget()
button1 = QPushButton(parent=widget, text='macintosh')
button1.setGeometry(10, 10, 100, 35)

button2 = QPushButton(parent=widget, text='Windows')
button2.setGeometry(10, 60, 100, 35)

button3 = QPushButton(parent=widget, text='Fusion')
button3.setGeometry(10, 110, 100, 35)

button1.setStyle(QStyleFactory.create('macintosh'))
button2.setStyle(QStyleFactory.create('Windows'))
button3.setStyle(QStyleFactory.create('Fusion'))
widget.show()

# widget.setStyle(style)


sys.exit(app.exec())
