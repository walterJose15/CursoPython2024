""" Crea una funcion llamada devolver_distintos () que reciba 3 Integers como parametros.
1.- si la suma de los 3 numeros es mayor a 15 va a devolver el mumero mayor.
2._ Si la suma de los 3 numeros es menor a 10 va a devolver el numero menor.
3.- si la suma de los 3 numeros es un valor entre 10 y 15 (incluidos) va a devolver el numero de valor intermedio."""

def devolver_distintos(a, b, c):
    suma = a + b + c
    numeros = [a, b, c]
    
    if suma > 15:
        return max(numeros)
    elif suma < 10:
        return min(numeros)
    else:
        numeros.sort()
        return numeros[1]

print(devolver_distintos(5, 5, 5))  # Debería devolver 5 (intermedio)
print(devolver_distintos(10, 3, 4))  # Debería devolver 10 (mayor)
print(devolver_distintos(2, 3, 4))   # Debería devolver 3 (menor)


