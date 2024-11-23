class Paleta:
    def __init__(self) -> None:
        self.__index = 0
        self.__colores = ['Rojo', 'Verde', 'Negro', 'Blanco', 'Azul']

    def __iter__(self): # devuelve el iterador
        return self 
    
    def __next__(self):
        if (self.__index == len(self.__colores)):
            self.__index = 0 # iniciamos en 0 para que en el siguiente for empiece en el inicio
            raise StopIteration # RECORDAR - hace que el next pare pero no sale error
        else:
            color = self.__colores[self.__index] # devuelve el componente siguiente
            self.__index+=1
            return color

paleta = Paleta()

for color in paleta:
    print(color)