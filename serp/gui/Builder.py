# -*- coding: utf-8 -*-

from gi.repository import Gtk
from .Handlers import Handlers
from gui.MainWindow import MainWindow
from classes.Base import Base


class Builder(Gtk.Builder):

    def __init__(self):
        super(Builder, self).__init__()
        self.builder = Gtk.Builder()
        self.builder.add_from_file("main.glade")
        self.builder.connect_signals(Handlers(self.builder))

        MainWindow(self.builder, Base())
