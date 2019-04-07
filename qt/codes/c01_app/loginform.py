# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'form.ui'
#
# Created by: PyQt5 UI code generator 5.12
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_Form(object):
    def setupUi(self, Form):
        Form.setObjectName("Form")
        Form.resize(400, 300)
        self.btn_login = QtWidgets.QPushButton(Form)
        self.btn_login.setGeometry(QtCore.QRect(60, 240, 120, 40))
        self.btn_login.setObjectName("btn_login")
        self.btn_cancel = QtWidgets.QPushButton(Form)
        self.btn_cancel.setGeometry(QtCore.QRect(220, 240, 120, 40))
        self.btn_cancel.setObjectName("btn_cancel")
        self.frame = QtWidgets.QFrame(Form)
        self.frame.setGeometry(QtCore.QRect(30, 30, 341, 181))
        self.frame.setFrameShape(QtWidgets.QFrame.Panel)
        self.frame.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame.setObjectName("frame")
        self.txt_username = QtWidgets.QLineEdit(self.frame)
        self.txt_username.setGeometry(QtCore.QRect(120, 30, 180, 30))
        self.txt_username.setObjectName("txt_username")
        self.txt_password = QtWidgets.QLineEdit(self.frame)
        self.txt_password.setGeometry(QtCore.QRect(120, 80, 180, 30))
        self.txt_password.setObjectName("txt_password")
        self.label = QtWidgets.QLabel(self.frame)
        self.label.setGeometry(QtCore.QRect(50, 30, 60, 30))
        font = QtGui.QFont()
        font.setFamily("Hei")
        font.setPointSize(14)
        self.label.setFont(font)
        self.label.setAlignment(QtCore.Qt.AlignRight | QtCore.Qt.AlignTrailing | QtCore.Qt.AlignVCenter)
        self.label.setObjectName("label")
        self.label_2 = QtWidgets.QLabel(self.frame)
        self.label_2.setGeometry(QtCore.QRect(50, 80, 60, 30))
        font = QtGui.QFont()
        font.setFamily("Hei")
        font.setPointSize(14)
        self.label_2.setFont(font)
        self.label_2.setAlignment(QtCore.Qt.AlignRight | QtCore.Qt.AlignTrailing | QtCore.Qt.AlignVCenter)
        self.label_2.setObjectName("label_2")

        self.retranslateUi(Form)
        self.btn_login.clicked.connect(Form.login)
        self.btn_cancel.clicked.connect(Form.reset)
        QtCore.QMetaObject.connectSlotsByName(Form)

    def retranslateUi(self, Form):
        _translate = QtCore.QCoreApplication.translate
        Form.setWindowTitle(_translate("Form", "登录"))
        self.btn_login.setText(_translate("Form", "登录"))
        self.btn_cancel.setText(_translate("Form", "取消"))
        self.label.setText(_translate("Form", "用户："))
        self.label_2.setText(_translate("Form", "口令："))
