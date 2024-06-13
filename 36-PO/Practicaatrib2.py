"""
Práctica Atributos 3
Crea una clase llamada Personaje, y asígnale el siguiente atributo de clase:

real = False

Crea una instancia llamada harry_potter con los siguientes atributos de instancia:

especie = "Humano"

magico = True

edad = 17
"""
class personaje:
    real = False

    def __init__(self, especie, magico, edad): 
        self.especie = especie                     
        self.magico = magico
        self.edad = edad

harry_potter = personaje(especie="humano", magico=True, edad=17)

print(f'El personaje es harry_potter un {harry_potter.especie} salio de un cuento {harry_potter.magico} de adas y tiene {harry_potter.edad} ')