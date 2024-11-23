'''
Crear la clase Vehiculo, con los métodos arrancar y parar - print('Soy un vehículo')
Crear las clases derivadas Automovil, Barco, Avion
Sobreescribir los métodos arrancar y parar
Programar los métodos avanzar, aparcar, atracar y aterrizar
Crear una instancia de cada clase derivada
Arrancar y utilizar alguno de los métodos específicos
'''
# Clase padre Vehiculo. Las demás heredan de ella
class Vehiculo:
    def __init__(self, nombre) -> None:
        print('Estamos en el init de Vehículo')
        self.nombre = nombre
    
    # definimos los métodos arrancar y parar:
    def arrancar(self):
        print('Soy un vehículo y voy a arrancar')
    def parar(self):
        print('Soy un vehículo y voy a parar')

# clase derivada Automovil:
class Automovil(Vehiculo):
    def arrancar(self):
        super().arrancar() # llamaría al método arrancar() de la clase padre
        # Vehiculo.arrancar(self) # Notación alternativa
        print(f'Soy un automovil llamado {self.nombre} y voy a arrancar')

    def parar(self):
        print(f'Soy un automóvil llamado {self.nombre} y voy a parar')

    def avanzar(self):
         print(f'Soy un automóvil llamado {self.nombre} y voy a avanzar')
    
    def aparcar(self):
         print(f'Soy un automóvil llamado {self.nombre} y voy a aparcar')

# clase derivada Barco:
class Barco(Vehiculo):
    astillero = 'lo que sea'
    def __init__(self, nombre, eslora):
        super().__init__(nombre) # llamamos al constructor de la clase Vehiculo
        self.eslora = eslora # tiene un atributo propio

    def arrancar(self):
        super().arrancar()
        print(f'Soy un barco llamado {self.nombre} con {self.eslora} de eslora y voy a arrancar')

    def parar(self):
        print(f'Soy un barco llamado {self.nombre} y voy a parar')

    def avanzar(self):
         print(f'Soy un barco llamado {self.nombre} y voy a avanzar')

    def atracar(self):
         print(f'Soy un barco llamado {self.nombre} y voy a atracar')

# clase derivada Avión:
class Avion(Vehiculo):
    def arrancar(self):
        super().arrancar()
        print(f'Soy un avión llamado {self.nombre} y voy a arrancar')

    def parar(self):
        print(f'Soy un avión llamado {self.nombre} y voy a parar')

    def avanzar(self):
         print(f'Soy un avión llamado {self.nombre} y voy a avanzar')

    def aterrizar(self):
         print(f'Soy un avión llamado {self.nombre} y voy a aterrizar')


# Creamos los objetos de las clases derivadas:
automovil_1 = Automovil('Audi') # Estamos en el init de Vehículo
barco_1 = Barco('Titanic', 30)
avion_1 = Avion('Boeing')

# Utilizamos los métodos arrancar y otro a mayores para cada objeto:
automovil_1.arrancar() # Soy un automovil llamado Audi y voy a arrancar
automovil_1.aparcar()
barco_1.arrancar()
barco_1.atracar()
print(barco_1.nombre)
print(barco_1.eslora)
avion_1.arrancar()
avion_1.aterrizar()

#Introspección -> como un objeto es capaz de reflexionarse a sí mismo
# isinstance() --> nos dice si un objeto es instancia o no de una clase determinada:
print(isinstance(barco_1, Barco)) # True
print(isinstance(barco_1, Vehiculo)) # True
print(isinstance(barco_1, object)) # True
print(isinstance(barco_1, Automovil)) # False

# issubclass() --> determina si una clase es derivada de otra clase:
print(issubclass(Barco, Vehiculo)) # True
print(issubclass(Vehiculo, Barco)) # False
print(issubclass(Barco, object)) # True

#hasattr --> determina si un objeto tiene un atributo. Se ejecuta sobre los objetos
print(hasattr(automovil_1, 'eslora')) # False
print(hasattr(barco_1, 'eslora')) # True
print(hasattr(barco_1, 'astillero')) # True (consulta de un atributo de clase)
print(hasattr(barco_1, 'arrancar')) # True (OJO!!! arrancar es un método pero Python lo gestiona como atributo)

print(hasattr(barco_1, 'avanzar'))# True
print(hasattr(Barco, 'avanzar')) # True
print(hasattr(Vehiculo, 'nombre')) # False --> se crea en ejecución

# Atributo __dict__
print(Barco.__dict__) # Aplicado a una clase proporciona un diccionario con los métodos y atributos de clase - {'__module__': '__main__', .....}
print(barco_1.__dict__) # Aplicado a un objeto proporciona un diccionario con los atributos de instancia - {'nombre': 'Titanic', 'eslora': 30}

# Atributo __name__
# Aplica a clases
print(type(Barco.__name__)) # proporciona un str con el nombre de la clase
# print(barco_1.__name__) # error

# Atributo __module__
# Aplica a clases y objetos
print(Barco.__module__) # '__main__' o el nombre del módulo si no es el principal
print(barco_1.__module__) # '__main__'

from ejercicio_040_pila import Pila
print(Pila.__module__) # 'ejercicio_040_pila' ya que no está en el módulo principal

#Atributo __bases__
# Aplica a clases. Proporciona las superclases directas
print(Barco.__bases__) # (<class '__main__.Vehiculo'>,)