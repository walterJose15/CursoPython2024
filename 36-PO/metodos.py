class pajaro:

    #metodo constructor
    def __init__(self, color, especie):
        self.color = color
        self.especie = especie
    
    def piar(self):
        print('pio')

    def volar (self, metros):
        print (f'el pajaro ha volado {metros} metros')


# creacion de objetos 
piolin = pajaro ('amarillo', 'canario')
print (piolin.especie)
# llamar el metodo piar
piolin.piar()
# llamar el lmetodo volar
piolin.volar(3)
