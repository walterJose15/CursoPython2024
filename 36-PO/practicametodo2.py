"""
Práctica Tipos de Métodos 2
Crea un método de clase revivir() que actúa sobre el atributo 
de clase vivo de la clase Jugador, estableciéndolo en True cada 
vez que es invocado. El valor predeterminado del atributo vivo, debe ser False.
"""

class jugador:
    vivo=False
    @classmethod
    def revivir(cls):
        cls.vivo = True
        
class Jugador:
   vivo = False 
   @classmethod
   def revivir(cls):
      cls.vivo = True

