# -*- coding: utf-8 -*-

from gi.repository import Gtk


class MainWindow(Gtk.Window):

    def __init__(self, builder):
        super(MainWindow, self).__init__()

        self = builder.get_object("WindowMain")
        self.__class__ = MainWindow
        self.builder = builder

        # self.connect("destroy", lambda w: Gtk.main_quit())
        self.connect("destroy", self.on_window_destroy)

        self.show_all()

    def on_window_destroy(self, widget, data=None):
        print(self.builder.base.nombre)
        Gtk.main_quit()
