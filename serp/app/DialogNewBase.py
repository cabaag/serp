# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'dialogNewBase.ui'
#
# Created: Tue Feb 17 22:19:02 2015
#      by: PyQt5 UI code generator 5.3.1
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtWidgets, QtGui
from .Base import Base


class Ui_DialogNewBase(QtWidgets.QDialog):

    def __init__(self, parent=None):
        super(Ui_DialogNewBase, self).__init__(parent)
        self.parent = parent
        self.setupUi(self)

    def setupUi(self, DialogNewBase):
        DialogNewBase.setObjectName("DialogNewBase")
        DialogNewBase.resize(600, 400)
        DialogNewBase.setMinimumSize(QtCore.QSize(600, 400))
        DialogNewBase.setMaximumSize(QtCore.QSize(600, 400))
        icon = QtGui.QIcon()
        icon.addPixmap(
            QtGui.QPixmap("icons/NewFile.png"),
            QtGui.QIcon.Active, QtGui.QIcon.Off)
        icon.addPixmap(
            QtGui.QPixmap("icons/NewFile.png"),
            QtGui.QIcon.Disabled, QtGui.QIcon.Off)
        icon.addPixmap(
            QtGui.QPixmap("icons/NewFile.png"),
            QtGui.QIcon.Normal, QtGui.QIcon.On)
        icon.addPixmap(
            QtGui.QPixmap("icons/NewFile.png"),
            QtGui.QIcon.Disabled, QtGui.QIcon.On)
        icon.addPixmap(
            QtGui.QPixmap("icons/NewFile.png"),
            QtGui.QIcon.Normal, QtGui.QIcon.Off)
        DialogNewBase.setWindowIcon(icon)
        DialogNewBase.setLocale(
            QtCore.QLocale(QtCore.QLocale.Spanish, QtCore.QLocale.Mexico))
        self.responseButtonBoxNBDialog = QtWidgets.QDialogButtonBox(
            DialogNewBase)
        self.responseButtonBoxNBDialog.setGeometry(
            QtCore.QRect(250, 360, 341, 32))
        self.responseButtonBoxNBDialog.setLocale(
            QtCore.QLocale(QtCore.QLocale.Spanish, QtCore.QLocale.Mexico))
        self.responseButtonBoxNBDialog.setOrientation(QtCore.Qt.Horizontal)
        self.responseButtonBoxNBDialog.setStandardButtons(
            QtWidgets.QDialogButtonBox.Cancel | QtWidgets.QDialogButtonBox.Ok)
        self.responseButtonBoxNBDialog.setObjectName(
            "responseButtonBoxNBDialog")
        self.verticalLayoutWidget = QtWidgets.QWidget(DialogNewBase)
        self.verticalLayoutWidget.setGeometry(QtCore.QRect(10, 10, 581, 331))
        self.verticalLayoutWidget.setObjectName("verticalLayoutWidget")
        self.gridLayout = QtWidgets.QGridLayout(self.verticalLayoutWidget)
        self.gridLayout.setContentsMargins(0, 0, 0, 0)
        self.gridLayout.setObjectName("gridLayout")
        self.nombreLineEditNBDialog = QtWidgets.QLineEdit(
            self.verticalLayoutWidget)
        self.nombreLineEditNBDialog.setObjectName("nombreLineEditNBDialog")
        self.gridLayout.addWidget(self.nombreLineEditNBDialog, 1, 1, 1, 1)
        self.descriptionTextEditNBDialog = QtWidgets.QTextEdit(
            self.verticalLayoutWidget)
        self.descriptionTextEditNBDialog.setObjectName(
            "descriptionTextEditNBDialog")
        self.gridLayout.addWidget(self.descriptionTextEditNBDialog, 2, 1, 1, 1)
        self.nombreLabelNBDialog = QtWidgets.QLabel(self.verticalLayoutWidget)
        self.nombreLabelNBDialog.setObjectName("nombreLabelNBDialog")
        self.gridLayout.addWidget(self.nombreLabelNBDialog, 1, 0, 1, 1)
        self.classesLabelNBDialog = QtWidgets.QLabel(self.verticalLayoutWidget)
        self.classesLabelNBDialog.setObjectName("classesLabelNBDialog")
        self.gridLayout.addWidget(self.classesLabelNBDialog, 3, 0, 1, 1)
        self.desciptionLabelNBDialog = QtWidgets.QLabel(
            self.verticalLayoutWidget)
        self.desciptionLabelNBDialog.setObjectName("desciptionLabelNBDialog")
        self.gridLayout.addWidget(self.desciptionLabelNBDialog, 2, 0, 1, 1)
        self.classesLineEditNBDialog = QtWidgets.QLineEdit(
            self.verticalLayoutWidget)
        self.classesLineEditNBDialog.setInputMethodHints(
            QtCore.Qt.ImhPreferNumbers)
        self.classesLineEditNBDialog.setInputMask("")
        self.classesLineEditNBDialog.setObjectName("classesLineEditNBDialog")
        self.gridLayout.addWidget(self.classesLineEditNBDialog, 3, 1, 1, 1)

        self.retranslateUi(DialogNewBase)
        self.responseButtonBoxNBDialog.accepted.connect(DialogNewBase.accept)
        self.responseButtonBoxNBDialog.rejected.connect(DialogNewBase.reject)
        QtCore.QMetaObject.connectSlotsByName(DialogNewBase)

    def retranslateUi(self, DialogNewBase):
        _translate = QtCore.QCoreApplication.translate
        DialogNewBase.setWindowTitle(
            _translate("DialogNewBase", "Crear nueva Base"))
        self.classesLineEditNBDialog.setText(_translate("DialogNewBase", "0"))
        self.classesLabelNBDialog.setText(
            _translate("DialogNewBase", "Clases"))
        self.desciptionLabelNBDialog.setText(
            _translate("DialogNewBase", "Descripción"))
        self.nombreLabelNBDialog.setText(_translate("DialogNewBase", "Nombre"))

    def accept(self):
        base = Base()
        base.name = self.nombreLineEditNBDialog.text()
        if base.name == "":
            QtWidgets.QMessageBox.warning(
                self, "Advertencia", "La base debe tener un nombre")
        else:
            base.description = self.descriptionTextEditNBDialog.toPlainText()
            base.classes = int(self.classesLineEditNBDialog.text())
            self.parent.createNewBase(base)
            self.close()
