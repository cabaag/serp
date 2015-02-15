# -*- coding: utf-8 -*-

from gi.repository import Gtk
from .Dialog import Dialog


class MainWindow(Gtk.Window):

    base = None

    def __init__(self, builder, base):
        super(MainWindow, self).__init__()

        self = builder.get_object("WindowMain")
        self.__class__ = MainWindow
        self.builder = builder
        print(base)
        self.connect("destroy", self.on_destroy)

        self.show_all()

    def on_destroy(self, widget):
        Gtk.main_quit()

    def on_new_base(self, widget):
        Dialog(self.builder, "dialogNewBase")
