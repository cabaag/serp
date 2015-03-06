# -*- coding: utf-8 -*-


import unittest
import imp
# import sys
# sys.path.append('../../app/core')

# import Variable

Objeto = imp.load_source('Objeto', '../../app/core/Objeto.py')
Variable = imp.load_source('Variable', '../../app/core/Variable.py')
Matriz = imp.load_source('Matriz', '../../app/core/Matriz.py')


class CoreTest(unittest.TestCase):

    # Prueba para las matrices

    def test_matriz_observacional(self):
        matriz = Matriz.MatrizObservacional()

        objects = [
            Objeto.Objeto("objeto1"),
            Objeto.Objeto("objeto2"),
            Objeto.Objeto("objeto3"),
            Objeto.Objeto("objeto4")
        ]
        matriz.objects = objects
        matriz.addObject(Objeto.Objeto("objeto5"))
        for x in matriz.objects:
            print(x.name)

        variables = [
            Variable.Variable("variable1"),
            Variable.Variable("variable2"),
            Variable.Variable("variable3"),
            Variable.Variable("variable4")
        ]
        matriz.variables = variables
        matriz.addVariable(Variable.Variable("variable2"))
        matriz.addVariable(Variable.Variable("variable5"))
        for x in matriz.variables:
            print(x.name)

    # Pruebas para las clases de variable

    def test_variable_cuantitativa(self):

        variable = Variable.VariableCuantitativa()
        variable.minimum_value = 0
        variable.maximum_value = 7
        variable.value = 5
        self.assertGreater(variable.maximum_value, variable.minimum_value)
        self.assertGreaterEqual(variable.maximum_value, variable.value)
        self.assertLessEqual(variable.minimum_value, variable.value)

    def test_variable_cualitativa(self):
        variable = Variable.VariableCualitativa()
        variable.value = "hola"
        self.assertEqual(variable.value, "hola")

    def test_variable_booleana(self):
        variable = Variable.VariableBooleana()
        variable.value = True
        self.assertEqual(variable.value, True)

if __name__ == '__main__':
    unittest.main()
