mi_archivo = open('prueba.txt')

print (mi_archivo.read())

print(mi_archivo.readline())
print(mi_archivo.readline())

for l in mi_archivo:
    print("aqui dice: + 1")


mi_archivo.close()