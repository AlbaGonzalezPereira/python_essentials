class Animal:
    def comer(self):
        pass

class Mamifero(Animal):
    def mamar(self):
        pass

class BichoVolador(Animal):
    def volar(self):
        pass

class Gaviota(BichoVolador):
    pass

class Murcielago(Mamifero, BichoVolador): # herencia múltiple
    pass

print(Animal.__bases__) # (<class 'object'>,)
print(Murcielago.__bases__) # (<class '__main__.Mamifero'>, <class '__main__.BichoVolador'>)
print(Murcielago.__base__) # <class '__main__.Mamifero'>

# Crear una instancia de Gaviota y de un Murcielago
# Crear una función amamantar(animal)
# Determinar si un animal puede o no mamar. Si no puede, lanza un error


def amamantar(animal):
    if isinstance(animal, Mamifero):
        print(f'El animal {animal} puede mamar') 
    else:
        raise TypeError(f'El animal {animal} no puede mamar')
    
def amamantar_otra_forma(animal):    
    if not isinstance(animal, Mamifero):
        raise TypeError('El animal no es un mamífero')
    elif not hasattr(animal, 'mamar'):
        raise AttributeError('El animal no puede mamar')
    else:
        animal.mamar() # llamamos al método
        print('El animal puede mamar')
    
print(Animal.__bases__)
gaviota = Gaviota()
murcielago = Murcielago()
amamantar(gaviota)
amamantar(murcielago)
batman = Murcielago()
# del Mamifero.mamar

try:
    amamantar_otra_forma(batman)
except Exception as e:
    print(e)    


batman.mamar()