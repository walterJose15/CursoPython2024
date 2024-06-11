"""
Practica 3
Crea una función llamada numeros_persona que reciba, como primer 
argumento, un nombre, y a continuación, una cantidad indefinida de números.
La función debe devolver el siguiente mensaje:
"{nombre}, la suma de tus números es {suma_numeros}"
"""

def numero_persona(nombre, *args):
    suma_numeros = sum(args)
    return f"{nombre}, la suma de tus numeros es {suma_numeros}" 

print (numero_persona('jose', 1,2,3,4))
