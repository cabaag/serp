#!/usr/bin/env python

import gtk

class main:
    def __init__(self):
        self.builder = gtk.Builder()
        self.builder.add_from_file('gtk10.glade')
        self.builder.connect_signals(self)
        self.window = self.builder.get_object("window1")
        self.window.show()

    def on_file_new_activate(self, menuitem, data=None):
        pass

    def on_file_open_activate(self, menuitem, data=None):
        pass

    def on_file_save_activate(self, menuitem, data=None):
        pass

    def on_file_save_as_activate(self, menuitem, data=None):
        pass

    def on_file_quit_activate(self, menuitem, data=None):
        pass

    def on_window1_destroy(self, object, data=None):
        print "quit with cancel"
        gtk.main_quit()

if __name__ == "__main__":
    main = main()
    gtk.main()
