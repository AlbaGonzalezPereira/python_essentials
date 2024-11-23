class Animal:
    def comer(self):
        print('Soy un Animal y estoy comiendo')

class Mamifero(Animal):
    def comer(self):
        print('Soy un Mamifero y estoy comiendo')

class BichoVolador(Animal):
    def comer(self):
        print('Soy un BichoVolador y estoy comiendo')

class Murcielago(Mamifero, BichoVolador): 
    pass




# ¿Cómo come un Murcielago que tiene método comer?
# Con su propio método

# ¿Cómo come un Murciélago que no tiene el método comer()?
# Si hay un método comer() en todas las superclases, 
# elige la primera de las que hereda directamente (empieza por la izquierda)
# Si no todas las superclases tienen el método, coge en la primera en la que encuentra el método

# Si en las superclases directas no tiene el método, se va a las superclases de estas, en este caso Animal

# Si la clase derivada hereda de la superclase y de una de las clases derivadas de esta, 
# da un error MRO: class Murcielago(Animal, BichoVolador)
# TypeError: Cannot create a consistent method resolution order (MRO) for bases Animal, BichoVolador
'''
class Murcielago(Animal, BichoVolador): 
    pass
'''
# si se invierte el orden (BichoVolador, Animal) no da problema

batman = Murcielago() 
batman.comer() # 'Soy un Mamifero y estoy comiendo'