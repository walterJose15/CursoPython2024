"""match valor: 
    case patron1:
        #codigo a ejecutar si el valor coincide con patron 1
    case patron2:
        #codigo a ejecutar si el valor coincide con patron 2
    case_:
        #codigo a ejecutar si el valor no coincide con ningun patron"""

#ejemplo / comparacion de numero 
number=1
match number:
    case 1:
        print("Uno")
    case 2:
        print("Dos")
    case 3:
        print("Tres")
    case _:
        print("Otro numero")

#comparacion de tipos
value = {"a": 1}
match value:
    case int():
        print("Es un entero")
    case str():
        print("Es una cadena")
    case list():
        print("Es una lista")
    case _:
        print("Tipo desconocido")    

#desempaquetado de tuplas
coord = (5, 7)
match coord:
    case (0,0):
        print ("Punto de Origen")
    case (x,0):
        print(f"Eje x en {x}")
    case (0,y):
        print(f"Eje y en {y}")
    case (x,y):
        print(f"Punto en {x}, {y}")
    case _: 
        print ("Coordenadas desconocidas")