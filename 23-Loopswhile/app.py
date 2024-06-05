monedas =5

while monedas>0:
    print  (f"tengo {monedas}")
    monedas = monedas -1

#ejercicio

respuesta = "s"
while respuesta == "s":
    respuesta = input("Quieres seguir ? (s/n)")
else:
    print ("Gracias")

# break
nombre = input("Tu nombre:")

for letra in nombre:
    if letra == "r":
        break
    print(letra)

# continue
nombre = input("Tu nombre:")

for letra in nombre:
    if letra == "r":
        continue
    print(letra)