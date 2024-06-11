lista_numeros = [1,2,15,7,2,8,15]

def reducir_lista(lista):
    lista = list(set(lista))
    lista.pop (-1)
    print(lista)
    return lista

def promedio (lista):
    valor_medio = sum(lista)/len(lista)
    return valor_medio

promedio_valores = promedio(reducir_lista(lista_numeros))
print(promedio_valores)


reducir_lista(lista_numeros)
print(promedio(lista_numeros))