"""
Practica 3

Utiliza el método choice() de la librería random para obtener 
un elemento al azar de la lista de nombres a continuación, y 
almacena el nombre escogido en una variable llamada sorteo.

nombres = ["Carlos", "Julia", "Nicole", "Laura", "Mailen"]
"""
from random import *
nombres = ["Carlos", "Julia", "Nicole", "Laura", "Mailen"]
Sorteo=choice(nombres)
print(Sorteo)