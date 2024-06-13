"""

Práctica Atributos 1
Crea una clase llamada Casa, y asígnale atributos: color, cantidad_pisos.

Crea una instancia de Casa, llamada casa_blanca, de color "blanco" y cantidad
de pisos igual a 4.
"""


class casa:
    def __init__(self, color, cantidad_pisos): #construccion
        self.color = color                     #atributos
        self.cantidad_pisos = cantidad_pisos

#creacion del objeto
casa_blanca = casa(color="blanco", cantidad_pisos= 4) 

print(f"vendo una casa color {casa_blanca.color} tiene {casa_blanca.cantidad_pisos} pisos")



