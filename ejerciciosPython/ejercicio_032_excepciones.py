#resultado = 5 / 0 # ZeroDivisionError: division by zero
#print(resultado)

try:
    numero = int(input('Numero: '))
except ValueError as ve:
    print('Ha ocurrido un error: ', ve)
  

# Pedir al usuario dos números y dividirlos
# Capturar la excepción ZeroDivisionError que se producirá si el divisor es 0

try:
    operando_1 = int(input('Introduzca el primer operando: '))
    operando_2 = int(input('Introduzca el segundo operando: '))
    resultado = operando_1 / operando_2
    print(resultado)
except ValueError as ve:
    print('Introduzca un valor correcto: ', ve)
except ZeroDivisionError as zde:
    print('Introduzca un valor diferente a 0 ', zde)