# coding = utf-8
import sys

from PyQt5.QtGui import QFont, QFontDatabase, QPalette, QColor
from PyQt5.QtWidgets import QWidget, QApplication, QPushButton

app = QApplication(sys.argv)
widget = QWidget()
widget.setWindowTitle('调色板与字体')
widget.setGeometry(300, 300, 400, 300)
db = QFontDatabase()
# fonts = db.families(QFontDatabase.SimplifiedChinese)
fonts = db.families(QFontDatabase.Any)
for f in fonts:
    print(f)
font = QFont('Weibei SC', 30)
widget.setFont(font)

button1 = QPushButton(parent=widget, text='窗体字体')
button1.setGeometry(10, 10, 200, 80)
button1.setFont(font)

pal = QPalette()
pal.setColor(QPalette.Background, QColor(255, 0, 0))
# QPalette.ToolTipText作用于QTooltip，而不是窗体的tooltip属性
# pal.setColor(QPalette.ToolTipText,  QColor(255, 0, 255))
widget.setPalette(pal)
# 提示信息的颜色可以使用样式表（很多文本类的属性都可以）
widget.setToolTip('<font color=red>提示颜色</font>')

widget.show()
sys.exit(app.exec())
