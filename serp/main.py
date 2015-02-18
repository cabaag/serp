#!/usr/bin/env python
# -*- coding: utf-8 -*-
# from gui.Builder import Builder
# from gi.repository import Gtk


# class main():

#     def __init__(self):
#         Builder()


# print("hi")
# if __name__ == "__main__":
#     print("hola")
#     main = main()
#     Gtk.main()


from gui.mainwindow import Ui_MainWindow
import sys
from PyQt5 import QtWidgets

if __name__ == "__main__":
    app = QtWidgets.QApplication(sys.argv)
    ex = Ui_MainWindow()
    ex.show()
    sys.exit(app.exec_())
