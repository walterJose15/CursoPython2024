"""Escribe una funcion que requiera una cantidad indefinida de argumentos. lo que hara esta funcion es devolver True
si en algun momento se ha ingresado al numero cero repetido dos veces consecutivas
for example
(5,6,1,0,0,9,3,5) True
(6,0,5,1,0,3,0,1) False"""


def numeros_consecutivos(*args):
    for i in range(len(args) - 1):
        if args[i] == 0 and args[i + 1] == 0:
            return True
    return False

print(numeros_consecutivos(1, 2, 3, 0, 0, 4, 5))  
print(numeros_consecutivos(1, 2, 0, 3, 0, 4, 5))  
print(numeros_consecutivos(0, 0))                
print(numeros_consecutivos())                   
