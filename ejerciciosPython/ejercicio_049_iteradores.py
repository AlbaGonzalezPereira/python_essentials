'''
lista = ['a', 'b', 'c']
lista_mayusculas = (letra.upper() for letra in lista)
print(type(lista)) # <class 'list'>
#print(type(lista_mayusculas)) # <class 'generator'>
lista.append('z')
for item in lista_mayusculas:
    print(item, end=',') # A,B,C,Z,
'''

'''
x = range(10)
print(type(x)) # <class 'range'>
print(len(x)) # 10
'''

class Componente:
    def __init__(self, nombre):
        self.nombre = nombre

    def __str__(self):
        print(self.nombre)

class Ordenador:
    def __init__(self):
        self.__index = 0
        self.__componentes = []

    def add_component(self, componente : Componente):
        self.__componentes.append(componente)

    def __iter__(self): # RECORDAR
        return self # TypeError: iter() returned non-iterator of type 'Ordenador'
    
    def __next__(self): # RECORDAR
        if (self.__index == len(self.__componentes)):
            self.__index = 0 # iniciamos en 0
            raise StopIteration # RECORDAR
        componente = self.__componentes[self.__index] # devuelve el componente siguiente
        self.__index+=1
        return componente

mi_ordenador = Ordenador()
cpu = Componente('Intel i5')
ram = Componente('128 Gbytes')
hd = Componente('2 TB SSD')
mi_ordenador.add_component(cpu)
mi_ordenador.add_component(ram)
mi_ordenador.add_component(hd)

for componente in mi_ordenador:
    print(componente) # TypeError: 'Ordenador' object is not iterable

for componente in mi_ordenador:
    print(componente)