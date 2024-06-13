"""
Práctica Abrir y Manipular Archivos 1
Abre el archivo texto.txt e imprime su contenido.
"""
mi_archivo = open('prueba.txt')
#print(mi_archivo.read())

"""

Práctica Crear y Escribir Archivos 1
Abre el archivo llamado "mi_archivo.txt", y cambia su contenido por el texto "Nuevo texto".

Imprime el contenido completo de "mi_archivo.txt" al finalizar.
"""

archivo = open ('mi_archivo.txt', 'w')
archivo.write ('nuevo texto')
archivo.close()

archivo = open('mi_archivo.txt' , 'r')
print(archivo.read())
archivo.close()