# -*- coding: utf-8 -*-

from .Dialog import Dialog


class Handlers():

    def __init__(self, builder):
        self.builder = builder

    def onNewBase(self, button):
        Dialog(self.builder, "dialogNewBase")
        # print hasattr(self, 'dialog')
        # if not hasattr(self, 'dialog'):
        #     self.dialog = Dialog(self.builder, "dialogNewBase")
        # else:
        #     self.dialog = Dialog(self.builder, "dialogNewBase")

    def check_only_number(self, widget, entry):
        pass
