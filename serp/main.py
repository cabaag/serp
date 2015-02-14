# -*- coding: utf-8 -*-

from gi.repository import Gtk
from gui.Handlers import Handlers


class MainWindow(Gtk.Builder):

    def __init__(self):
        super(MainWindow, self).__init__()
        #handlers = {
            #"OnDeleteEvent": Gtk.main_quit,
            #"OnNewFile": hello
        #}
        self.add_from_file("gui/main.glade")
        self.connect_signals(Handlers())
        window = self.get_object("WindowMain")
        window.show_all()
        Gtk.main()
