#archivo = open('prueba2.txt', 'w')
#archivo.write('hola''\n')
#archivo.write ('mundo')

#modificar archivo
archivo = open('prueba2.txt', 'a')

lista = ["hola","mundo","estoy","feliz"]
for l in lista:
    archivo.writelines(l + '\n')
archivo.write ('bienvenidos') # agregar texto 
archivo.close()