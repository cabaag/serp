# -*- coding: utf-8 -*-
from gi.repository import Gtk


class MyWidget(object):

    def __init__(self, nameWidget=None):
        builder = Gtk.Builder()
        builder.add_from_file("gui/main.glade")
        builder.connect_signals(Handlers())
        builder.get_object(nameWidget)

    def get_object(self, nameWidget=None):
        builder = Gtk.Builder()
        builder.add_from_file("gui/main.glade")
        builder.connect_signals(Handlers())
        return builder.get_object(nameWidget)
