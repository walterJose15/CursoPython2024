# cantidad de atributos
def cantidad_atributos(**kwargs):
    cantidad = 0 
    for i in kwargs.items():
        cantidad += 1
        print (cantidad)
    return cantidad

print(cantidad_atributos(a=1,b=2,c=3))


