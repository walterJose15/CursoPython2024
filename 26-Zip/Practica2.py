"""
Practica 2

Crea un objeto zip formado a partir de listas, de un 
conjunto de marcas y productos que tú prefieras, dentro de la variable mi_zip.
"""
carros = ['Audi', "Toyota","Chevrolet"]
uso = ["Nuevo", "Usado", "Nevo"]
mi_zip = zip(carros,uso)

for carros, uso in mi_zip:
    
    print(f"El Auto  {carros} es {uso}")