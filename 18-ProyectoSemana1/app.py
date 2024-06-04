texto = input("Ingresa un texto a eleccion: ")
letras = []

texto = texto.lower()

letras.append(input("Ingrese la primera letra: ".lower()))
letras.append(input("Ingresa la segunda letra: ".lower()))
letras.append(input("Ingresa la tercera letra: ".lower()))

print("\n")
print("CANTIDAD DE LETRAS")
cantidad_letras1 = texto.count(letras[0])
cantidad_letras2 = texto.count(letras[1])
cantidad_letras3 = texto.count(letras[2])

print(f"Hemos encontrado la letra'{letras[0]}' repetida {cantidad_letras1} veces")
print(f"Hemos encontrado la letra'{letras[1]}' repetida {cantidad_letras2} veces")
print(f"Hemos encontrado la letra'{letras[2]}' repetida {cantidad_letras3} veces")

print("\n")
print ("CANTIDAD DE PALABRAS")
palabras = texto.split()
print(f"Hemos encontrado{len(palabras)} palabras en tu texto")
