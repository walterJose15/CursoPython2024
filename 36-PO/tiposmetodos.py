class pajaro:
    alas=True
    #metodo constructor
    def __init__(self, color, especie):
        self.color = color
        self.especie = especie
    
    def piar(self):
        print('pio')

    def volar (self, metros):
        print (f'el pajaro ha volado {metros} metros')

#metodo de instancia
    def pintar_negro(self):
        self.color ="negro"
        print(f"ahora el pajaro es {self.color}")


#metodo de clase
    @classmethod
    def poner_huevos(cls, cantidad):
        print(f"puso {cantidad} huevos")
        cls.alas= False
        print(pajaro.alas)

# metodos estaticos
    @staticmethod
    def mirar():
        print("el pajaro mira")



#creacion de objetos
piolin = pajaro('amarillo', 'canario')
print(piolin.pintar_negro())
print(piolin.poner_huevos(3))





