"""
Practica 2

Calcula la diferencia entre el valor máximo y 
el mínimo en la siguiente lista de números, y almacénalo en una variable llamada rango:

lista_numeros = [44542247, 21310, 2134747, 44556475, 121676, 6654067, 353254, 123134, 552512, 611665]
"""

lista_numeros = [44542247, 21310, 2134747, 44556475, 121676, 6654067, 353254, 123134, 552512, 611665]
rangomin= min(lista_numeros)
rangomax= max(lista_numeros)
rango= rangomax-rangomin

print(rango) 