import random

numero_intentos = 0
numero_secreto = random.randint(1,10) # Return a random integer N such that a <= N <= b
# print(numero_secreto)
numero = -1 # forzamos para que entre en el bucle al poner un número que no está en el rango
while (numero!=numero_secreto): # tenemos que forzar que al menos entre
    numero = int(input('Introduce un número (1-10):'))
    # numero = int(numero)
    # numero_intentos = numero_intentos + 1
    numero_intentos +=1
    if(numero_secreto == numero):
        print(f'Eres un adivino. Has necesitado {numero_intentos} intentos')
    else:
        print('Prueba de nuevo')
else:
    print("Se muestra cuando la condición del while se deja de cumplir")


