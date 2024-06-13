import os

ruta = os.getcwd()
#print (ruta) detalla la direccion de la carpeta

ruta = os.makedirs ('C:\\Users\\WalterSanunga\\Documents\\CursoPython\\35-Archivos\\otra carp')
#print(ruta) #crea una carpeta en el directorio

os.rmdir("'C:\\Users\\WalterSanunga\\Documents\\CursoPython\\35-Archivos\\otra carp'")
#print(ruta) # elimina la carpeta creada


elemento = os.path.split (ruta)
#print(elemento)