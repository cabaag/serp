# -*- coding: utf-8 -*-

from gi.repository import Gtk
from .DialogNewFile import DialogNewFile


class Handlers():
    def OnDeleteEvent(self, *args):
        Gtk.main_quit(*args)

    def onNewFile(self, button):
        DialogNewFile()