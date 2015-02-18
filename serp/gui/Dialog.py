# -*- coding: utf-8 -*-

from gi.repository import Gtk


class Dialog(Gtk.Dialog):

    def __init__(self, builder, nameWidget=None, base=None):
        super(Dialog, self).__init__()

        self = builder.get_object(nameWidget)
        self.__class__ = Dialog
        self.builder = builder

        self.connect("response", self.handler_response)
        self.connect("close", self.hide_dialog)
        self.connect("delete-event", self.hide_dialog)
        self.show()

    def show_dialog(self):
        self.show()

    def handler_response(self, widget, response, data=None):
        if response == 1:  # A.pyccept button
            self.save_new_file()
        elif response == 2:  # Cancel button
            self.hide_dialog(widget)

    def save_new_file(self):
        base = self.builder.base
        base.nombre = self.builder.get_object("entryNameNB").get_text()
        base.descripcion = self.builder.get_object(
            "entryDescriptionNB").get_text()
        base.clases = self.builder.get_object("entryClasesNB").get_text()

    def hide_dialog(self, widget):
        print("cerrando")
        self.hide()

    def has_base(self):
        return self.builder
