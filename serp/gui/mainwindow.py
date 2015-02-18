# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'mainwindow.ui'
#
# Created: Tue Feb 17 21:49:31 2015
#      by: PyQt5 UI code generator 5.3.1
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_MainWindow(QtWidgets.QMainWindow):

    def __init__(self, parent=None):
        super(Ui_MainWindow, self).__init__(parent)
        self.setupUi(self)

    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(800, 600)
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(MainWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 800, 23))
        self.menubar.setObjectName("menubar")
        self.menuFile = QtWidgets.QMenu(self.menubar)
        self.menuFile.setObjectName("menuFile")
        MainWindow.setMenuBar(self.menubar)
        self.statusbar = QtWidgets.QStatusBar(MainWindow)
        self.statusbar.setObjectName("statusbar")
        MainWindow.setStatusBar(self.statusbar)
        self.actionNuevo = QtWidgets.QAction(MainWindow)
        icon = QtGui.QIcon()
        icon.addPixmap(
            QtGui.QPixmap("icons/NewFile.png"),
            QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.actionNuevo.setIcon(icon)
        self.actionNuevo.setObjectName("actionNuevo")
        self.actionAbrir = QtWidgets.QAction(MainWindow)
        self.actionAbrir.setObjectName("actionAbrir")
        self.actionAbrir_recientes = QtWidgets.QAction(MainWindow)
        self.actionAbrir_recientes.setObjectName("actionAbrir_recientes")
        self.actionGuardar = QtWidgets.QAction(MainWindow)
        self.actionGuardar.setObjectName("actionGuardar")
        self.actionGuardar_como = QtWidgets.QAction(MainWindow)
        self.actionGuardar_como.setObjectName("actionGuardar_como")
        self.actionExportar = QtWidgets.QAction(MainWindow)
        self.actionExportar.setObjectName("actionExportar")
        self.actionGuardar_imagen = QtWidgets.QAction(MainWindow)
        self.actionGuardar_imagen.setObjectName("actionGuardar_imagen")
        self.actionCerrar = QtWidgets.QAction(MainWindow)
        self.actionCerrar.setObjectName("actionCerrar")
        self.actionSalir = QtWidgets.QAction(MainWindow)
        self.actionSalir.setShortcut("")
        self.actionSalir.setShortcutContext(QtCore.Qt.WindowShortcut)
        self.actionSalir.setObjectName("actionSalir")
        self.menuFile.addAction(self.actionNuevo)
        self.menuFile.addAction(self.actionAbrir)
        self.menuFile.addAction(self.actionAbrir_recientes)
        self.menuFile.addSeparator()
        self.menuFile.addAction(self.actionGuardar)
        self.menuFile.addAction(self.actionExportar)
        self.menuFile.addSeparator()
        self.menuFile.addAction(self.actionGuardar_imagen)
        self.menuFile.addSeparator()
        self.menuFile.addAction(self.actionCerrar)
        self.menuFile.addSeparator()
        self.menuFile.addAction(self.actionSalir)
        self.menubar.addAction(self.menuFile.menuAction())

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "MainWindow"))
        self.menuFile.setTitle(_translate("MainWindow", "Archivo"))
        self.actionNuevo.setText(_translate("MainWindow", "Nuevo"))
        self.actionNuevo.setShortcut(_translate("MainWindow", "Ctrl+N"))
        self.actionAbrir.setText(_translate("MainWindow", "Abrir"))
        self.actionAbrir_recientes.setText(
            _translate("MainWindow", "Abrir recientes..."))
        self.actionGuardar.setText(_translate("MainWindow", "Guardar"))
        self.actionGuardar_como.setText(
            _translate("MainWindow", "Guardar como"))
        self.actionExportar.setText(_translate("MainWindow", "Exportar"))
        self.actionGuardar_imagen.setText(
            _translate("MainWindow", "Guardar imagen"))
        self.actionCerrar.setText(_translate("MainWindow", "Cerrar"))
        self.actionSalir.setText(_translate("MainWindow", "Salir"))
