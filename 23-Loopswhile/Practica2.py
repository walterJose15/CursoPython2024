"""
Practica 2
Crea un Loop While que reste de uno en uno los números desde el 
50 al 0 (ambos números incluídos) con las siguientes condiciones adicionales:
- Si el número es divisible por 5, mostrar dicho número en 
pantalla (¡recuerda que aquí puedes utilizar la operación módulo dividiendo por 5 y verificando el resto!)
- Si el número no es divisible por 5, continuar ejecutando el loop 
sin mostrar el valor en pantalla (no te olvides de seguir restando para que el programa no corra infinitamente).
"""

numeros = 50

while numeros >= 0:
    if numeros % 5 == 0:
        print(numeros)
    numeros -= 1