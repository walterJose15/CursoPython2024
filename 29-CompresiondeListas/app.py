#sintaxis

#forma tradicional
palabra = "python"
lista= []

for item in palabra:
    lista.append(item)

    #print(lista)

#comprension de listas
lista = [item for item in 'python']
#print(lista)

#comprension de listas con numeros
#nueva_lista = [expresion for item in iterable if condicion == True]
lista = [item/2 for item in range(0,21 ,2)]
print(lista)

#usando if
lista =[n if n **2 > 10 else 'No' for n in range(0,21,2)]
print (lista)

#ejemplo
numeros = [1,2,3,4,5,6,7,8,9,10]
resultado = ['par' if numero %2 == 0 else 'impar' for numero in numeros]
print(resultado)

# comevrtir de metros a pies
metros = [10,20,30,40,50]
pies = [p *3.281 for p in metros]
print(pies)