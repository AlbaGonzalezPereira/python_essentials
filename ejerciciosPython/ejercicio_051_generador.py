import time

# 1. Solución tradicional. 
# Hasta que no están todos los elementos de la lista no comienza el proceso
def get_numeros():
    numeros = []
    for numero in range(3):
        time.sleep(2) # tiempo de espera de 2 sg
        numeros.append(numero)
    return numeros

# SOLUCIÓN NORMAL:
print('Empezando sin generador...')
numeros = get_numeros() 
for numero in numeros:
    print('Procesando: ', numero)
    time.sleep(2) # tiempo de espera de 2 sg


######################################################################################################

# 2. Solución mediante generador
# Se procesa cada elemento según va generándose
def get_numeros_generador():
    for numero in range(3):
        time.sleep(2) # tiempo de espera de 2 sg
        yield numero # retorna ese valor pero la función sigue ejecutándose

# SOLUCIÓN CON EL GENERADOR:
print('Empezando con generador...')
numeros = get_numeros_generador() 
for numero in numeros:
    print('Procesando: ', numero)
    time.sleep(2) # tiempo de espera de 2 sg




    
