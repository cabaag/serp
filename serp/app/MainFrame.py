# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'form.ui'
#
# Created: Wed Feb 18 19:08:51 2015
#      by: PyQt5 UI code generator 5.3.1
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_Form(QtWidgets.QWidget):

    def __init__(self, parent=None):
        super(Ui_Form, self).__init__(parent)
        # print(self.parentWidget())
        self.setupUi(self)
        # print(self.size())
        # print(self.findChild(QtWidgets.QFrame, "frame").size())

    def setupUi(self, Form):
        Form.setObjectName("Form")
        Form.resize(800, 600)
        Form.setStyleSheet("background-color: rgb(0, 255, 127);")
        self.frame = QtWidgets.QFrame(Form)
        self.frame.setGeometry(QtCore.QRect(0, 0, 641, 481))
        self.frame.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame.setObjectName("frame")
        self.frame.resize(self.size())
        self.dial = QtWidgets.QDial(self.frame)
        self.dial.setGeometry(QtCore.QRect(20, 0, 50, 64))
        self.dial.setObjectName("dial")

        self.retranslateUi(Form)
        QtCore.QMetaObject.connectSlotsByName(Form)

    def retranslateUi(self, Form):
        _translate = QtCore.QCoreApplication.translate
        Form.setWindowTitle(_translate("Form", "Form"))
