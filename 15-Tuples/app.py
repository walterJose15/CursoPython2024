#son inmutables -> no se puedes editar

mi_tupla = (1,2,(10,20),4)
print(type(mi_tupla))
print(mi_tupla[2][0])

#concersion
mi_tupla = list(mi_tupla)
print(type(mi_tupla))

#asignar
t = (1,2,3)
x,y,z = t
print(x,y,z)


#aplicando metodos en tuplas count() - index()
t = (1,2,3,2,2)
print(t.count(2))
print(t.index(1))