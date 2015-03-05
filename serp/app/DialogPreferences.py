# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'dialogPreferences.ui'
#
# Created: Wed Feb 18 20:40:21 2015
#      by: PyQt5 UI code generator 5.3.1
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtWidgets


class Ui_Dialog(QtWidgets.QDialog):

    def __init__(self, parent=None):
        super(Ui_Dialog, self).__init__(parent)
        self.setupUi(self)

    def setupUi(self, DialogPreferences):
        DialogPreferences.setObjectName("DialogPreferences")
        DialogPreferences.resize(600, 400)
        self.tabWidget = QtWidgets.QTabWidget(DialogPreferences)
        self.tabWidget.setGeometry(QtCore.QRect(0, 0, 600, 361))
        self.tabWidget.setObjectName("tabWidget")
        self.editorTab = QtWidgets.QWidget()
        self.editorTab.setObjectName("editorTab")
        self.tabWidget.addTab(self.editorTab, "")
        self.globalTab = QtWidgets.QWidget()
        self.globalTab.setObjectName("globalTab")
        self.tabWidget.addTab(self.globalTab, "")
        self.buttonBox = QtWidgets.QDialogButtonBox(DialogPreferences)
        self.buttonBox.setGeometry(QtCore.QRect(420, 370, 176, 27))
        self.buttonBox.setOrientation(QtCore.Qt.Horizontal)
        self.buttonBox.setStandardButtons(
            QtWidgets.QDialogButtonBox.Cancel | QtWidgets.QDialogButtonBox.Ok)
        self.buttonBox.setObjectName("buttonBox")

        self.retranslateUi(DialogPreferences)
        QtCore.QMetaObject.connectSlotsByName(DialogPreferences)

    def retranslateUi(self, DialogPreferences):
        _translate = QtCore.QCoreApplication.translate
        DialogPreferences.setWindowTitle(
            _translate("DialogPreferences", "Preferencias"))
        self.tabWidget.setTabText(self.tabWidget.indexOf(
            self.editorTab), _translate("DialogPreferences", "Tab 1"))
        self.tabWidget.setTabText(self.tabWidget.indexOf(
            self.globalTab), _translate("DialogPreferences", "Tab 2"))
