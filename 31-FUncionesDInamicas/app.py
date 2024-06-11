#cualcular el area de un cuadrado y un rectangulo
def calcular_area_forma(lado1, lado2= None):
    if lado2 is None:
        return lado1 **2 #area del cuadrado 
    else:
        return lado1*lado2 #area del rectangulo
    
print(calcular_area_forma(5))
print(calcular_area_forma(3,4))

#crear una funcion que sume los numeros pares
def suma_pares_hasta(n):
    suma = 0
    for i in range (2, n+1,  2):
        suma += i
    return suma

print(suma_pares_hasta(10)) #(2 + 4 + 6 + 8 + 10) = 30

#crear una funcion que permita una sumatoria de cubos y cuadrados
def suma_cuadrado_cubos(n):
    suma_cuadrado = 0
    suma_cubos = 0 
    for i in range (1, n+1):
        if i % 2 == 0:
            suma_cuadrado += i **2
        else:
            suma_cubos += i **3
    return suma_cuadrado, suma_cubos

cuadrados, cubos = suma_cuadrado_cubos(5)
print("suma de cuadrados:", cuadrados) # 2^2 + 4^2 = 20
print("suma de cubos:", cubos) # 1^3 + 3^3 + 5^3 = 153


    