class pajaro:
    def __init__(self, color, especie):
        self.color = color
        self.especie = especie


# creacion de objetos 
mi_pajaro = pajaro ('negro', 'tucan')
otro_pajaro = pajaro ('morado','halcon')

print(f'Mi pajaro es un {mi_pajaro.especie} y de color {mi_pajaro .color}')
print(f'Mi pajaro es un {otro_pajaro.especie} y de color {otro_pajaro .color}')

