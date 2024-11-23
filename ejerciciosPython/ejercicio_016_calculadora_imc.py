# Ejercicio:
# Crear una función que calcule el Índice de Masa Corporal y retorne el resultado
# Utilizar en la llamada keyworks arguments y añadir comentarios de tipo 'docstring'
# para explicar la función

def calcular_imc(peso : float, altura : float) -> float :
    '''
    Calcula el índice de masa corporal de una persona (IMC)
    El IMC se trata de una medida de asociación entre lo que se pesa y lo que se mide. 
    Su fórmula es: IMC = peso(kg) / altura(m)2
    '''
    imc = peso / (altura**2)
    return imc


# Peso inferior al normal -> menos de 18.5
# Normal -> 18.5 - 24.5
# Peso superior al normal -> 25.0 - 29.9
# Obesidad -> Más de 30.0

def calcular_estado(imc : float) -> str:
    '''
    Devuelve una cadena de caracteres con el estado del paciente
    '''
    if(imc > 30.0):
        return 'Tienes obesidad'
    elif(imc >= 25.0):
        return 'Tu peso es superior al normal'
    elif(imc>=18.5):
        return 'Tu peso es normal'
    else:
        return 'Tu peso es inferior al normal'

if __name__=='__name__':
    print('SOY EL 16')
    print(__name__) # __name__ nos dice si el script en el que está es el principal