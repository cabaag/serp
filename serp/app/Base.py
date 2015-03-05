# -*- coding: utf-8 -*-


class Base():

    def __init__(self):
        self.description = ""
        self.classes = 0
        self.modified = False

    @property
    def name(self):
        return self._name

    @name.setter
    def name(self, value):
        self._name = value

    @property
    def description(self):
        return self._description

    @description.setter
    def description(self, value):
        self._description = value

    @property
    def classes(self):
        return self._classes

    @classes.setter
    def classes(self, value):
        if value < 0:
            self.__classes = 0
        else:
            self._classes = value

    @property
    def modified(self):
        return self._modified

    @modified.setter
    def modified(self, value):
        self._modified = value

    def showMeta(self):
        print(self.name, self.description, self.classes, self.modified)
