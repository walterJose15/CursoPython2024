lista = ["a","b","c"]
indice = 0

for item in lista:
    print(indice, item)
    #operadores de asignacion
    indice += 1

print ("\n")
#con enumerate
lista = ["a","b","c"]

for i, item in enumerate(lista):
    print(i, item)

#combinacion enumerate con range

print ("\n")
for i, item in enumerate(range(50,55)):
    print (f"{i} - {item}")

#cfrear lista de tuples
print ("\n")
lista = ["a","b","c"]

mi_tuple = list(enumerate(lista))
print(mi_tuple)
print(mi_tuple[1][1])
