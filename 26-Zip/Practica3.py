"""
Practica 3
Crea el zip con las traducciones los números del 1 al 5 en español, portugués e inglés (en el mismo orden), y convierte el objeto generado en una lista almacenada en la variable numeros:
uno / um / one
dos / dois / two
tres / três / three
cuatro / quatro / four
cinco / cinco / five
El resultado deberá seguir la estructura:
[(uno, um, one), (dos, dois, two), ... ]
"""
espanol = ["Uno", "Dos","Tres","Cuatro","Cinco"]
portugues= ["Un", "Dois","Tr3s","Quatro","Cinco"]
ingles= ["One", "Two","Three","Four","Five"]

Idioma = list (zip(espanol, portugues,ingles))
print(Idioma)