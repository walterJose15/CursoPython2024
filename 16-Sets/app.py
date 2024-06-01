#primera forma de declar un set
mi_set = set([1,2,3,4])
print(mi_set)

#segunda forma de declar un set
otr_set = {1,2,3}
print(type(otr_set))
print(otr_set)

#errores en sets
#print(mi_set[0])
#mi_set[0] = 5 
#print (mi_set)

#elementos unicos
mi_set =set((1,2,3,4,5,1,1,1,1,2,2,2,2))
print(mi_set)

#
#mi_set =set((1,2,3,4,5,[2,1],1,1,1,1,2,2,2,2))
#print(mi_set)

#validar si existe un elemento

mi_set = set((1,2,3,4,5))
print(10 in mi_set)

#union de los sets
s1= {1,2,3}
s2= {3,4,5}
s3= s1.union(s2)
print(s3)

#agregar elementos
s1 = {1,2,3,4,6,5}
s1.add(4)
print(s1)

#eliminando sets
s1.remove (3)
print(s1)

#descartar elementos
s1.discard(6)
print(s1)

#eliminar un elemento
s1.pop()
print(s1)