from pathlib import path, pureWindorsPath

carpeta = path('C:\\Users\\WalterSanunga\\Documents\\CursoPython\\35-Archivos')

ruta_windowa = pureWindorsPath(carpeta)
print(ruta_windowa)



if not carpeta.exists():
    print ('no existe')
else:
    print('existe')
