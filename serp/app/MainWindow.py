# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'mainwindow.ui'
#
# Created: Tue Feb 17 22:33:03 2015
#      by: PyQt5 UI code generator 5.3.1
#
# WARNING! All changes made in this file will be lost!

import os
from PyQt5 import QtCore, QtGui, QtWidgets
from .DialogNewBase import Ui_DialogNewBase
from .DialogPreferences import Ui_Dialog
from .MainFrame import Ui_Form


class Ui_MainWindow(QtWidgets.QMainWindow):

    def __init__(self, parent=None):
        super(Ui_MainWindow, self).__init__(parent)
        self.setupUi(self)

    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(800, 600)
        MainWindow.setLocale(
            QtCore.QLocale(QtCore.QLocale.Spanish, QtCore.QLocale.Mexico))
        self.centralwidget = Ui_Form(self)
        self.centralwidget.setObjectName("centralwidget")
        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(MainWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 800, 23))
        self.menubar.setObjectName("menubar")
        self.menuFile = QtWidgets.QMenu(self.menubar)
        self.menuFile.setObjectName("menuFile")
        self.menuEdit = QtWidgets.QMenu(self.menubar)
        self.menuEdit.setObjectName("menuEdit")
        self.menuDatos = QtWidgets.QMenu(self.menubar)
        self.menuDatos.setObjectName("menuDatos")
        self.menuOperaciones = QtWidgets.QMenu(self.menubar)
        self.menuOperaciones.setObjectName("menuOperaciones")
        self.menuReconocimiento = QtWidgets.QMenu(self.menubar)
        self.menuReconocimiento.setObjectName("menuReconocimiento")
        MainWindow.setMenuBar(self.menubar)
        self.statusbar = QtWidgets.QStatusBar(MainWindow)
        self.statusbar.setObjectName("statusbar")
        MainWindow.setStatusBar(self.statusbar)
        self.actionNew = QtWidgets.QAction(MainWindow)
        icon = QtGui.QIcon()
        icon.addPixmap(
            QtGui.QPixmap("icons/NewFile.png"),
            QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.actionNew.setIcon(icon)
        self.actionNew.setObjectName("actionNew")
        self.actionOpen = QtWidgets.QAction(MainWindow)
        icon1 = QtGui.QIcon()
        icon1.addPixmap(
            QtGui.QPixmap("icons/Open.png"),
            QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.actionOpen.setIcon(icon1)
        self.actionOpen.setObjectName("actionOpen")
        self.actionOpen_recents = QtWidgets.QAction(MainWindow)
        self.actionOpen_recents.setObjectName("actionOpen_recents")
        self.actionSave = QtWidgets.QAction(MainWindow)
        self.actionSave.setObjectName("actionSave")
        self.actionExport = QtWidgets.QAction(MainWindow)
        self.actionExport.setObjectName("actionExport")
        self.actionSave_snapshot = QtWidgets.QAction(MainWindow)
        self.actionSave_snapshot.setObjectName("actionSave_snapshot")
        self.actionClose = QtWidgets.QAction(MainWindow)
        self.actionClose.setObjectName("actionClose")
        self.actionQuit = QtWidgets.QAction(MainWindow)
        self.actionQuit.setShortcutContext(QtCore.Qt.WindowShortcut)
        self.actionQuit.setObjectName("actionQuit")
        self.actionPreferences = QtWidgets.QAction(MainWindow)
        self.actionPreferences.setObjectName("actionPreferences")
        self.menuFile.addAction(self.actionNew)
        self.menuFile.addAction(self.actionOpen)
        self.menuFile.addAction(self.actionOpen_recents)
        self.menuFile.addSeparator()
        self.menuFile.addAction(self.actionSave)
        self.menuFile.addAction(self.actionExport)
        self.menuFile.addSeparator()
        self.menuFile.addAction(self.actionSave_snapshot)
        self.menuFile.addSeparator()
        self.menuFile.addAction(self.actionClose)
        self.menuFile.addSeparator()
        self.menuFile.addAction(self.actionQuit)
        self.menuEdit.addAction(self.actionPreferences)
        self.menubar.addAction(self.menuFile.menuAction())
        self.menubar.addAction(self.menuEdit.menuAction())
        self.menubar.addAction(self.menuDatos.menuAction())
        self.menubar.addAction(self.menuOperaciones.menuAction())
        self.menubar.addAction(self.menuReconocimiento.menuAction())

        # self.actionSave.setEnabled(False)
        self.retranslateUi(MainWindow)
        self.actionQuit.triggered.connect(MainWindow.close)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "SERP"))
        self.menuFile.setTitle(_translate("MainWindow", "Archivo"))
        self.menuEdit.setTitle(_translate("MainWindow", "Editar"))
        self.menuDatos.setTitle(_translate("MainWindow", "Datos"))
        self.menuOperaciones.setTitle(_translate("MainWindow", "Operaciones"))
        self.menuReconocimiento.setTitle(
            _translate("MainWindow", "Reconocimiento"))
        self.actionNew.setText(_translate("MainWindow", "Nuevo"))
        self.actionNew.setShortcut(_translate("MainWindow", "Ctrl+N"))
        self.actionOpen.setText(_translate("MainWindow", "Abrir"))
        self.actionOpen.setShortcut(_translate("MainWindow", "Ctrl+O"))
        self.actionOpen_recents.setText(
            _translate("MainWindow", "Abrir recientes..."))
        self.actionSave.setText(_translate("MainWindow", "Guardar"))
        self.actionSave.setShortcut(_translate("MainWindow", "Ctrl+S"))
        self.actionExport.setText(_translate("MainWindow", "Exportar"))
        self.actionSave_snapshot.setText(
            _translate("MainWindow", "Guardar imagen"))
        self.actionClose.setText(_translate("MainWindow", "Cerrar"))
        self.actionQuit.setText(_translate("MainWindow", "Salir"))
        self.actionQuit.setShortcut(_translate("MainWindow", "Ctrl+Q"))
        self.actionPreferences.setText(
            _translate("MainWindow", "Preferencias"))

        self.actionNew.triggered.connect(self.showDialogNewBase)
        self.actionSave.triggered.connect(self.saveBase)
        self.actionPreferences.triggered.connect(self.showDialogPreferences)

    def showDialogNewBase(self):
        dialogNewBase = Ui_DialogNewBase(self)
        dialogNewBase.exec_()

    def createNewBase(self, base):
        self.base = base
        self.base.showMeta()
        self.setWindowTitle("SERP - " + base.name)
        self.actionSave.setEnabled(True)

    def saveBase(self, base):
        directoryPath = os.getenv('HOME') + "/" + self.base.name + ".serp"
        dialog = QtWidgets.QFileDialog()
        dialog.f
        archivo = dialog.getSaveFileName(
            self, "Guardar base", directoryPath, "Base (*.serp)")
        if archivo[0] is not "":
            if ".serp" in archivo[0]:
                f = open(archivo[0], "w")
            else:
                f = open(archivo[0] + ".serp", "w")
            f.write(self.base.name)
            f.close()
            self.base.modified = False

    def showDialogPreferences(self):
        dialogPreferences = Ui_Dialog(self)
        dialogPreferences.exec_()
