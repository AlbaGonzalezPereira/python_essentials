class Engendro:
    def __init__(self, nombre, salud) -> None:
        self.nombre = nombre
        self.salud = salud

    def __eq__(self, other: object) -> bool:
        print('En el __eq__')
        return self.salud == other.salud
    
    def __str__(self) -> str: # como el método toString() en java
        return self.nombre

e1 = Engendro('Alien', 100)    
e2 = Engendro('E.T.', 200)
e3 = Engendro('Spiderman', 100)
e4 = e2

print(e1==e3) # False, Mira si son iguales en cuanto a Contenido
'''
print(e1 is e3) # False, Identidad
print(e4 is e2) # True
print(e4.nombre, e2.nombre)
e4.nombre = 'Batman'
print(e4.nombre, e2.nombre)
print(e4, e2)
'''