# -*- coding: utf-8 -*-


class MatrizObservacional():

    """Clase de la Matriz Obsrvacional, aquella que contentrá la muestra de
    los objetos tomados para su posterior estudio"""

    def __init__(self):
        self._objects = None
        self._variables = None

    @property
    def objects(self):
        return self._objects

    @objects.setter
    def objects(self, objects):
        self._objects = list()
        for objeto in objects:
            self.addObject(objeto)

    @property
    def variables(self):
        return self._variables

    @variables.setter
    def variables(self, variables):
        self._variables = list()
        for variable in variables:
            self.addVariable(variable)

    def addObject(self, newObject):
        listObjects = self._objects
        try:
            for objeto in listObjects:
                if newObject.name is objeto.name:
                    raise NameError(objeto.name)
            self._objects.append(newObject)
        except NameError as repetido:
            print("Identificador de objeto repetido ->", repetido)

    def addObjects(self, listObjects):
        for objeto in listObjects:
            self.addObject(objeto)

    def addVariable(self, newVariable):
        listVariables = self._variables
        try:
            for variable in listVariables:
                if newVariable.name is variable.name:
                    raise NameError(variable.name)
            self._variables.append(newVariable)
        except NameError as repetido:
            print("Identificador de variable repetido ->", repetido)

    def addVariables(self, listVariables):
        for variable in listVariables:
            self.addObject(variable)


class MatrizSemejanza(object):

    """Clase de la Matriz Obsrvacional, aquella que contentrá la semejanza que
    existe entre un objeto y contra cada uno de los demás objetos de la base,
    ya sea similaridad o disimilaridad"""

    def __init__(self, type="disimilaridad"):
        self._objetos = None
        self._type = type

    @property
    def objetos(self):
        return self._objetos

    @objetos.setter
    def objetos(self, value):
        self._objetos = value

    @property
    def type(self):
        return self._type

    @type.setter
    def type(self, value):
        self._type = value
