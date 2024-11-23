import random

numero_intentos = 0
numero_secreto = random.randint(1,10) # Return a random integer N such that a <= N <= b
# print(numero_secreto)

while (True):
    numero = int(input('Introduce un número (1-10):'))
    # numero = int(numero)
    # numero_intentos = numero_intentos + 1
    numero_intentos +=1
    if(numero_secreto == numero):
        print(f'Eres un adivino. Has necesitado {numero_intentos} intentos')
        break # para salirse del bucle
    else:
        print('Prueba de nuevo')
else:
    print("Else del while") # tiene un tono diferente y dice que nunca se va a ejecutar. No tiene razón de ser



