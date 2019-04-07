# coding = utf-8
import sys

from PyQt5.QtWidgets import \
    QApplication, \
    QWidget, \
    QPushButton, \
    QLabel

app = QApplication(sys.argv)

# 定义样式表
css = '''
QPushButton#button1{
    border:4px double red;
}
QLabel[text='样式2']{
    background:qconicalgradient( 
        cx:0.5, cy:0.5, angle:0, 
        stop:0 rgba(255, 0, 0, 255), 
        stop:0.25 rgba(0, 255, 0, 255), 
        stop:0.5 rgba(0, 0, 255, 255), 
        stop:0.75 rgba(0, 0, 0, 0), 
        stop:1.0 rgba(0, 0, 0, 255)
    );
}
'''
# app.setStyleSheet(css)

widget = QWidget()
widget.setGeometry(300, 300, 400, 200)
button1 = QPushButton(parent=widget, text='样式1')
button1.setObjectName('button1')
button1.setGeometry(10, 10, 100, 35)

label = QLabel(parent=widget, text='样式2')

label.setGeometry(10, 60, 100, 100)

widget.setStyleSheet(css)
widget.show()

sys.exit(app.exec())
