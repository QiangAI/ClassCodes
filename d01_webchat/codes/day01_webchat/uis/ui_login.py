# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'ui_login.ui'
#
# Created by: PyQt5 UI code generator 5.12
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_ui_login(object):
    def setupUi(self, ui_login):
        ui_login.setObjectName("ui_login")
        ui_login.resize(400, 300)
        self.lbl_qr = QtWidgets.QLabel(ui_login)
        self.lbl_qr.setGeometry(QtCore.QRect(0, 0, 400, 300))
        font = QtGui.QFont()
        font.setFamily("STHeiti")
        font.setPointSize(24)
        self.lbl_qr.setFont(font)
        self.lbl_qr.setAlignment(QtCore.Qt.AlignCenter)
        self.lbl_qr.setObjectName("lbl_qr")

        self.retranslateUi(ui_login)
        QtCore.QMetaObject.connectSlotsByName(ui_login)

    def retranslateUi(self, ui_login):
        _translate = QtCore.QCoreApplication.translate
        ui_login.setWindowTitle(_translate("ui_login", "Dialog"))
        self.lbl_qr.setText(_translate("ui_login", "加载二维码....."))
