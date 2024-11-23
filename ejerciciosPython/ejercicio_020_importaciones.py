'''
Crear un módulo con las funciones:
- sumar
- restar
- multiplicar
- dividir

Crear un programa Python que importe de manera EXPLÍCITA cada una de las funciones 
y haga uso de alguna de ellas.

Utilizar la estructura if __name__=='__main__'
'''

def sumar(operando_1, operando_2):
    '''
    Calcula la suma de dos números
    '''
    resultado = operando_1 + operando_2
    return resultado

def restar(operando_1, operando_2):
    '''
    Calcula la resta de dos números
    '''
    resultado = operando_1 - operando_2
    return resultado

def multiplicar(operando_1, operando_2):
    '''
    Calcula la multiplicación de dos números
    '''
    resultado = operando_1*operando_2
    return resultado 

def dividir(operando_1, operando_2):
    '''
    Calcula la división de dos números
    '''
    resultado = operando_1/operando_2
    return resultado 