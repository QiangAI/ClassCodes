# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'login.ui'
#
# Created by: PyQt5 UI code generator 5.12
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtWidgets


# Qt Designer创建
class Ui_dlg_login(object):
    def setupUi(self, dlg_login):
        dlg_login.setObjectName("dlg_login")
        dlg_login.resize(400, 300)
        self.edt_username = QtWidgets.QLineEdit(dlg_login)
        self.edt_username.setGeometry(QtCore.QRect(60, 50, 291, 31))
        self.edt_username.setObjectName("edt_username")
        self.edt_password = QtWidgets.QLineEdit(dlg_login)
        self.edt_password.setGeometry(QtCore.QRect(60, 110, 291, 31))
        self.edt_password.setObjectName("edt_password")
        self.lbl_captcha = QtWidgets.QLabel(dlg_login)
        self.lbl_captcha.setGeometry(QtCore.QRect(60, 170, 151, 51))
        self.lbl_captcha.setAlignment(QtCore.Qt.AlignCenter)
        self.lbl_captcha.setObjectName("lbl_captcha")
        self.edt_captcha = QtWidgets.QLineEdit(dlg_login)
        self.edt_captcha.setGeometry(QtCore.QRect(220, 180, 131, 31))
        self.edt_captcha.setObjectName("edt_captcha")
        self.btn_login = QtWidgets.QPushButton(dlg_login)
        self.btn_login.setGeometry(QtCore.QRect(140, 240, 111, 41))
        self.btn_login.setObjectName("btn_login")
        self.lbl_captcha.setVisible(False)
        self.edt_captcha.setVisible(False)
        self.retranslateUi(dlg_login)
        self.btn_login.clicked.connect(dlg_login.login)
        QtCore.QMetaObject.connectSlotsByName(dlg_login)

    def retranslateUi(self, dlg_login):
        _translate = QtCore.QCoreApplication.translate
        dlg_login.setWindowTitle(_translate("dlg_login", "Dialog"))
        self.edt_username.setPlaceholderText(_translate("dlg_login", "手机或者邮箱"))
        self.edt_password.setPlaceholderText(_translate("dlg_login", "密码"))
        self.lbl_captcha.setText(_translate("dlg_login", "加载校验码"))
        self.edt_captcha.setPlaceholderText(_translate("dlg_login", "校验码"))
        self.btn_login.setText(_translate("dlg_login", "登录"))
