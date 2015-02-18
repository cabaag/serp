# -*- coding: utf-8 -*-

from gi.repository import Gtk
from .Handlers import Handlers
from .MainWindow import MainWindow
import imp
# Base = imp.load_source('Base', '../classes/Base.py')
Base = imp.load_source('Base', 'classes/Base.py')


class Builder(Gtk.Builder):

    base = Base.Base()
    builder = Gtk.Builder()

    def __init__(self):
        super(Builder, self).__init__()
        self.builder.add_from_file("gui/main.glade")
        # self.builder.add_from_file("main.glade")
        self.builder.connect_signals(Handlers(self))

        MainWindow(self)

    def get_object(self, nameWidget):
        return self.builder.get_object(nameWidget)
