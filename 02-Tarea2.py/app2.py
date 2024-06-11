"""escribe una funcion (puedes poner cualquier nombre que quieras) que reciba cualquier palabra como parametro, 
y que devuelva todas sus letras unicas (sin repetir)pero en orden alfabetico.
por ejemplo si al invocar esta funcion pasamos la palabra "entretenido, deberia devolver ["d","e","i","n","o","r","t"]"""

def letras_unicas_walter(palabra):
    letras_unicas = set(palabra)
    letras_ordenadas = sorted(letras_unicas)
    return letras_ordenadas
print(letras_unicas_walter("walter")) 
