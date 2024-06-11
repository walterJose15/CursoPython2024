"""
def nombre_funcion(parametros):
    bloque del codigo
    return Value
"""

# cfrear un afucnion que suma 2 numeros 
def sumar(a,b):
    resultado = a+b
    return resultado

suma = sumar(5,6)
print(f"suma = {suma}")

#verificar si un numero es par
def es_par(numero):
    if numero % 2 == 0:
        return True
    else:
        return False
    
#llamar a la funcion 
print(es_par(1))
print(es_par(101))

#calcular el factorial de un numero
def x(n):
    if n ==0:
        return 1
    else :
        #aqui se aplica recursividad factorial que se llama asi mismo
        return n * x(n-1)
    
#llamar a la funcion 
print(x(5))