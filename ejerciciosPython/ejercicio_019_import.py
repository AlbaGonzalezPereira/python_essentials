import random # Nivel de peligrosidad CERO
# import random as loquesea # CON ALIAS - Nivel de peligrosidad CERO
# from random import randint # Nivel de peligrosidad BAJO
# from random import * # Nivel de peligrosidad LOCURA

def randint(n1, n2):
    return "Soy randint"

# aleatorio = randint(0,5) # coge la última definida, en este caso la función definida fuera de random
# print(aleatorio)
# print(randint(3,8)) # se ejecuta la función declarada
print(random.randint(1,10)) # se ejecuta la función del módulo random
print(randint(1,10))