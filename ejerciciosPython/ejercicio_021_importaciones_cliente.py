from ejercicio_020_importaciones import sumar
from ejercicio_020_importaciones import restar
from ejercicio_020_importaciones import multiplicar
from ejercicio_020_importaciones import dividir
# from ejercicio_020_importaciones import sumar, restar, multiplicar, dividir -> se puede hacer así

if __name__=='__main__':
    operando_1 = int(input('ingresa el primer operando: '))
    operando_2 = int(input('ingresa el segundo operando: '))
    suma = sumar(operando_1, operando_2)
    resta = restar(operando_1, operando_2)
    multiplicacion = multiplicar(operando_1, operando_2)
    division = dividir(operando_1, operando_2)
    print(f'La suma de {operando_1} + {operando_2} es: {suma}')
    print(f'La resta de {operando_1} - {operando_2} es: {resta}')
    print(f'La división de {operando_1} * {operando_2} es: {multiplicacion}')
    print(f'La división de {operando_1} / {operando_2} es: {division}')

    operacion = int(input('Qué operación quieres realizar (0-sumar, 1-restar, 2-multiplicar, 3-dividir)?: '))
    
    if operacion==0:
        operacion_real = 'suma'
        resultado = sumar(operando_1, operando_2)
        print(f'El resultado de la {operacion_real} es {resultado}')
    elif operacion==1:
        operacion_real='resta'
        resultado = restar(operando_1, operando_2)
        print(f'El resultado de la {operacion_real} es {resultado}')
    elif operacion==2:
        operacion_real = 'multiplicación'
        resultado = multiplicar(operando_1, operando_2)
        print(f'El resultado de la {operacion_real} es {resultado}')
    elif operacion==3:
        operacion_real = 'división'
        resultado = dividir(operando_1, operando_2)
        
    else:
        print('La operación no se ha podido realizar. Número incorrecto de operación')
    
    if(operacion==0 | operacion==1 | operacion==2 | operacion==3):
        print(f'El resultado de la {operacion_real} es {resultado}')

   