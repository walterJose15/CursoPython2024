"""
Práctica Métodos 3
Crea una instancia de la clase Alarma, que tenga un método 
llamado postergar(cantidad_minutos). El método debe imprimir en pantalla el mensaje

"La alarma ha sido pospuesta {cantidad_minutos} minutos"
"""
class alarma:
    def postergar(self,cantidad_minutos):
        print(f'la alarma ha sido postergada {cantidad_minutos} minutos')

alarma=alarma()
alarma.postergar(3)