# -*- coding: utf-8 -*-

from gi.repository import Gtk


class DialogNewFile(Gtk.Dialog):

    def __init__(self):
        super(DialogNewFile, self).__init__()
        builder = Gtk.Builder()
        builder.add_from_file("gui/main.glade")
        self = builder.get_object("dialogNewFile")
        self.show()
