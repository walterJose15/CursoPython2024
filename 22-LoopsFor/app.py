lista = ["a","b","c","d"]

for item in lista:
    numero_letra = lista.index(item) + 1
    print(f"letra {numero_letra}:{item}")


#ejemplo
lista = ['pablo', 'laura', 'jose', 'luis', 'julia']
for item in lista:
  if item.startswith('l'):
    print(item)
  else:
    print("Nombre que no comienze con L")

#ejemplo numero
numeros = [1,2,3,4,5]
mi_valor = 0
for item in numeros:
  mi_valor = mi_valor + item
  print(mi_valor)

#directamente
for a,b in [[11,2],[2,3],[5,6]]:
     print(f"{a}-{b}")
