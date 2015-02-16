# -*- coding: utf-8 -*-

from gi.repository import Gtk
from Handlers import Handlers
from MainWindow import MainWindow
import imp
Base = imp.load_source('Base', '../classes/Base.py')


class Builder(Gtk.Builder):

    def __init__(self):
        super(Builder, self).__init__()
        self.builder = Gtk.Builder()
        self.builder.add_from_file("main.glade")
        self.builder.connect_signals(Handlers(self.builder))

        self.base = Base.Base()
        MainWindow(self, self.base)
