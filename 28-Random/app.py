from random import *

#randint
aleatorio= randint(1,50)
print(aleatorio)

#Uniform
aleatorio = round(uniform(1,5),1)
print(aleatorio)

#random
print(random())

#choise
colores = ["azul","verde","negro","rojo"]
aleatorio=choice(colores)
print(aleatorio)

#shufle
numeros = list(range(5,50,5))
print(numeros)
shuffle(numeros)
print(numeros)