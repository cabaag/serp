# -*- coding: utf-8 -*-

from gi.repository import Gtk


class EntryMultiline(Gtk.Entry):

    def __init__(self, nameWidget=None):

        super(EntryMultiline, self).__init__()
        builder = Gtk.Builder()
        builder.add_from_file("gui/main.glade")
        if nameWidget is not None:
            self = builder.get_object(nameWidget)
        self.set_visible(False)
