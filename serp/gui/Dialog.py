# -*- coding: utf-8 -*-

from gi.repository import Gtk


class Dialog(Gtk.Dialog):

    def __init__(self, builder, nameWidget=None):
        super(Dialog, self).__init__()

        self = builder.get_object(nameWidget)
        self.__class__ = Dialog

        self.connect("response", self.handler_response)
        self.connect("close", self.hide_dialog)
        self.run()

    def handler_response(self, widget, response, data=None):
        if response == 1:  # Accept button
            self.save_new_file()
        elif response == 2:  # Cancel button
            self.hide_dialog(widget)

    def save_new_file(self):
        print('Watch out!')

    def hide_dialog(self, widget):
        self.hide()
