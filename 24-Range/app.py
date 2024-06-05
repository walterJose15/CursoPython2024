#forma tradicional
lista = [1,2,3,4]


for num in lista:
    print(num)  
print("\n")

#codigo optimizado
for num in range(1,5):
    print(num)
print("\n")

#Creacion lista en un alinea

lista = list(range(1,101, 3))
print(lista)