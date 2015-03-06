# -*- coding: utf-8 -*-


class Variable():

    """Clase base para los diferentes tipos de variables que puede soportar un
    Objeto"""

    def __init__(self, name="", value=0, type="numeric"):
        self._name = name
        self._value = value
        self._type = type

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
    def type(self):
        return self._type

    @type.setter
    def type(self, value):
        self._type = value


class VariableCuantitativa(Variable):

    """Clase que almacena los datos de una variable numérica, el tipo de datos
    que se podrá ingresar serán unicamente de tipo numérico, en cualquier otro
    caso el valor por defecto será 0 """

    def __init__(self):
        super(VariableCuantitativa, self).__init__()
        self._minimum_value = None
        self._maximum_value = None
        self._value = None

    @property
    def minimum_value(self):
        return self._minimum_value

    @minimum_value.setter
    def minimum_value(self, value):
        try:
            if not isinstance(value, int) and not isinstance(value, float):
                raise TypeError
            if (self._maximum_value is not None and
                    value >= self._maximum_value):
                raise ValueError
            self._minimum_value = value
        except TypeError:
            print("Minimo, Variable no numerica")
        except ValueError:
            print("Límite inferior es mayor que el limite superior, "
                  "%d > %d" % (value, self._maximum_value))

    @property
    def maximum_value(self):
        return self._maximum_value

    @maximum_value.setter
    def maximum_value(self, value):
        try:
            if not isinstance(value, float) and not isinstance(value, int):
                raise TypeError
            if (self._minimum_value is not None and
                    value <= self._minimum_value):
                raise ValueError
            self._maximum_value = value
        except TypeError:
            print("Maximo, Variable no numerica")
        except ValueError:
            print("Límite superior es menor que el limite inferior, "
                  "%d < %d" % (value, self._minimum_value))

    @property
    def value(self):
        return self._value

    @value.setter
    def value(self, value):
        try:
            if not isinstance(value, int) and not isinstance(value, float):
                raise TypeError
            elif (self._minimum_value is not None and
                  value < self._minimum_value):
                raise ValueError('minimo')
            elif (self._maximum_value is not None and
                  value > self._maximum_value):
                raise ValueError('maximo')
            else:
                self._value = value
        except TypeError:
            print("Valor no numerico")
        except ValueError as e:
            print("Valor fuera del rango", e)


class VariableCualitativa(Variable):

    """Clase que almacena los datos de una variable cualitativa, el tipo de
    datos que se podrá ingresar serán unicamente cadenas de caracteres, en
    cualquier otro caso el valor por defecto será vacio """

    def __init__(self):
        super(VariableCualitativa, self).__init__()
        self._type = "cualitativa"

    @property
    def value(self):
        return self._value

    @value.setter
    def value(self, value):
        try:
            if not isinstance(value, str):
                raise ValueError
            self._value = value
        except ValueError:
            print("Valor no cualitativo = %d" % value)


class VariableBooleana(object):

    """Clase que almacena los datos de una variable booleana, el tipo de
    datos que se podrá ingresar serán unicamente True o False, en
    cualquier otro caso el valor por defecto False """

    def __init__(self):
        super(VariableBooleana, self).__init__()
        self._type = "booleana"
        self._value = False

    @property
    def value(self):
        return self._value

    @value.setter
    def value(self, value):
        try:
            if not isinstance(value, bool):
                raise ValueError
            self._value = value
        except ValueError:
            print("Valor no booleano")
            self._value = False
