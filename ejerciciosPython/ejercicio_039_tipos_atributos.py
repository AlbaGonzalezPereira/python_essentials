'''
(1) Crear un aula con 3 alumnos.
(2) Agregar un método mostrar_alumnos en el aula que muestre los datos de los alumnos.
(Después...)
(3) Añadir un nuevo alumno al aula.
(4) Mostrar los alumnos.
'''

class Alumno:
    fondo_comun = 10 # Variable (atributo) de clase, misma variable a todos los objetos -> es como una variable estática en java
    def __init__(self, nombre, email):
        self.nombre = nombre # Variable (atributo) de instancia
        self.email = email

    # método que muestra los datos de un alumn@
    def mostrar_datos(self):
        print(f'Nombre: {self.nombre} - email: {self.email} - fondo común: {Alumno.fondo_comun}') # también se puede poner self.fondo_comun auqnue no es correcto
        # Alumno.fondo_comun = 20 # modificaría en el siguiente objeto el fondo_comun


class Aula:
    def __init__(self, identificador, capacidad, alumnos) -> None:
        self.identificador = identificador # son atributos públicos
        self.capacidad = capacidad
        self.__alumnos = alumnos # __ hace que los atributos sean privados. vale para métodos también
        # se pueden acceder a los atributos privados mediante _class__atributo - _Aula__alumnos

    # método que muestra los datos de los alumnos de un aula
    def mostrar_alumnos(self):
        for alumno in self.__alumnos:
            # print(f'{alumno.nombre} - {alumno.email}')
            alumno.mostrar_datos() # llamamos al método mostrar_datos por cada alumno
    
    # Declaración de método privado __método()
    def __metodo_privado(self):
        pass

    def agregar_alumno(self, alumno):
        assert isinstance(alumno, Alumno), 'No es un alumno'
        if (len(self.__alumnos) < self.capacidad) :
            self.__alumnos.append(alumno)
            # print('Alumno agregado correctamente')
        else:
            raise Exception('No se puede agregar el alumno. El aula ha alcanzado su máximo de capacidad')
            # print('No se ha podido agregar al alumno. Capacidad superada') - evitar print
            
# creamos 3 alumnos:
alumno_1 = Alumno('Juan', 'juan@gmail.com')
alumno_2 = Alumno('maría', 'maria@gmail.com')
alumno_3 = Alumno('Jose', 'jose@gmail.com')

# creamos una lista con los 3 alumnos creados:
lista_alumnos = [alumno_1,alumno_2,alumno_3] 

# creamos un aula:
aula_1 = Aula('aula001', 50, lista_alumnos)

# llamamos al método mostrar_alumnos():
aula_1.mostrar_alumnos() # Nombre: Juan, email: juan@gmail.com ...

# creamos un nuevo alumno
alumno_4 = Alumno('Pepe', 'pepe@gmail.com')

# añadimos el alumno_4 a la lista de alumnos
# lista_alumnos.append(alumno_4)  # modificamos la lista original, es peligroso
# aula_1.alumnos.append(alumno_4) # al poner el atributo privado da error - AttributeError: 'Aula' object has no attribute 'alumnos'
aula_1.agregar_alumno(alumno_4) # usamos el método agregar_alumno para añadirlo

# mostramos los datos del aula
print(f'Mostrando datos del {aula_1.identificador}...')
aula_1.mostrar_alumnos()