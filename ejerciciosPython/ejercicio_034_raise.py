# Una clase es un fragmento de código que tiene variables y métodos
# Es troquel
# Una clase es una instanciación de objetos
'''

# Definición de la clase
class Enemigo:
    pass

# Instanciación
ene = Enemigo()
lista = list()
tupla = tuple()
# Alumno()
# Circunferencia()
ValueError('El valor no es correcto')
'''

########################## RAISE ##################################################
def sumar (s1 : int, s2 : int):
    resultado = s1 + s2
    return resultado

print(sumar(1, 2)) # 3
print(sumar('Uno', 'Dos')) # UnoDos
print(sumar(True, True)) # 2

# queremos que compruebe que los tipos son correctos y si son que lance un error
def sumar (s1 : int, s2 : int):
    if (not isinstance(s1, int)):
        raise TypeError('El primer sumando debe ser de tipo int')
    resultado = s1 + s2
    return resultado

try:
    print(sumar(1, 2)) 
    print(sumar('Uno', 'Dos')) 
    print(sumar(True, True))
except TypeError as te:
    print(te) # podríamos hacer un raise aquí