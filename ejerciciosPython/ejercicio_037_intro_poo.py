class Alumno:
    # No se pueden hacer sobrecargas de constructores, ni de funciones, pero permite inicializar los argumentos
    def __init__(self, nombre, email, poblacion : str = 'Santiago de Compostela') -> None: # init nos garantiza el contructor
        '''
        Inicializador de Alumno

        Parámetros:
        - nombre: str, nombre del alumno.
        - email: str, email del alumno.
        - población: str, población de residencia, por defecto.... 'Santiago de Compostela'.
        '''
        print('En el método __init__ de Alumno') # se llama cuando se instancia un objeto
        # Definición de los atributos: 
        # self es similar al this en java, hace referencia al propio objeto, es un objeto pero no se puede omitir
        self.nombre = nombre 
        self.email = email 
        self.poblacion = poblacion # valor por defecto en caso de no pasar el atributo
        self.activo = True

    #Método
    def presentar(self):
        print(f'Soy {self.nombre} y mi dirección de correo es {self.email}')  


# Instanciación, creación de objeto, creación de instancia
alba = Alumno('Alba', 'alba@gmail.com', 'Pontevedra')
# Acceso a atributo -> alba.nombre
print(alba.nombre) # mostramos el valor del atributo nombre del objeto alba - Alba
# Invocación a un método
alba.presentar() # Soy Alba y mi dirección de correo es alba@gmail.com