'''
Crear la función contratar que recibe los argumentos:
nombre (tipo str, longitud>0)
edad (tipo int, >=18)

Comprobar con assert que los tipos y los valores de nombre y edad son correctos
'''

def contratar(nombre : str, edad : int):
    assert isinstance(nombre, str), "El nombre debe ser una cadena de caracteres" # garantizamos que el nombre es un str
    nombre = nombre.strip() # quitamos los espacios en blanco a ambos lados
    assert len(nombre) > 0, "El nombre no puede estar vacío" # ponemos lo que queremos que sea verdadero
    assert isinstance(edad, int), "La edad debe ser un número entero"
    assert edad >= 18, "La edad debe ser mayor o igual a 18"
    print(f'{nombre} ha sido contratad@')

# contratar('       ', 18) # utilizando strip() da error -> AssertionError: El nombre no puede estar vacío
nombre_contrato = input('Introduzca su nombre: ')
edad_contrato = int(input('Introduzca su edad: '))
contratar(nombre_contrato, edad_contrato)