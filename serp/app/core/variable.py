# -*- coding: utf-8 -*-


class Variable():

    """Clase base para los diferentes tipos de variables que puede soportar un
    Objeto"""

    def __init__(self, name=0, value=0, tipe="numeric"):
        self.name = name
        self.value = value
        self.tipe = tipe

    @property
    def name(self):
        return self._name

    @name.setter
    def name(self, value):
        self._name = value

    @property
    def value(self):
        return self._value

    @value.setter
    def value(self, value):
        self._value = value

    @property
    def tipe(self):
        return self._tipe

    @tipe.setter
    def tipe(self, value):
        self._tipe = value


class VariableNumerica(Variable):

    """Clase que almacena los datos de una variable numérica, el tipo de datos
    que se podrá ingresar serán unicamente de tipo numérico, en cualquier otro
    caso el valor por defecto será 0 """

    def __init__(self):
        self._minimum_value = None
        self._maximum_value = None

    @property
    def minimum_value(self):
        return self._minimum_value

    @minimum_value.setter
    def minimum_value(self, value):
        if self.maximum_value is not None:
            try:
                if value < self.maximum_value:
                    self._minimum_value = value
                else:
                    print("error, minimo es mayor")
                    raise ValueError
            except ValueError as e:
                print(e)
        else:
            self._minimum_value = value

    @property
    def maximum_value(self):
        return self._maximum_value

    @maximum_value.setter
    def maximum_value(self, value):
        if self.minimum_value is not None:
            try:
                if value > self.minimum_value:
                    self._maximum_value = value
                else:
                    print("error, maximo es menor")
                    raise ValueError
            except ValueError as e:
                print(e)
        else:
            self._maximum_value = ValueError

    @property
    def value(self):
        return self._value

    @value.setter
    def value(self, value):
        error = False
        if hasattr(self, 'minimum_value'):
            try:
                if value < self.minimum_value:
                    raise ValueError
            except ValueError as ex:
                error = True
                raise ex
        if hasattr(self, 'maximum_value'):
            try:
                if value > self.maximum_value:
                    raise ValueError
            except ValueError as ex:
                error = True
                raise ex
        if not error:
            self._value = value
