# -*- coding: utf-8 -*-


class Objeto():

    """Clase que al ser instanciada hará referencia a un objeto dentro de
    la base el cuál tendrá diferentes tipos de variables almacenadas en
    la misma las cuales podrán ser de atributos heterogéneos"""

    def __init__(self, name=""):
        self._name = name
        self._variables = None
        self._clase = 0

    @property
    def name(self):
        return self._name

    @name.setter
    def name(self, value):
        self._name = value

    @property
    def variables(self):
        return self._variables

    @variables.setter
    def variables(self, value):
        self._variables = value

    @property
    def clase(self):
        return self._clase

    @clase.setter
    def clase(self, value):
        self._clase = value
