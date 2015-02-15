# -*- coding: utf-8 -*-

from .Dialog import Dialog


class Handlers():

    def __init__(self, builder):
        self.builder = builder

    def onNewBase(self, button):
        Dialog(self.builder, "dialogNewBase")
