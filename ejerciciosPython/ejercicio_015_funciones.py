#####################FUNCIONES ######################
# Se define con la palabra def, un verbo y ()
# Puede recibir o no argumentos
# Puede devolver o no algo

#Función CON argumentos (con sugerencia de tipo int) y CON retorno
def sumar(sumando_1 : int, sumando_2 : int) -> int : 
    '''
    (docstring)
    Suma dos números enteros y devuelve el resultado
    '''
    resultado = sumando_1 + sumando_2
    return resultado # retorna el resultado

# guardo el valor que devuelve en una variable:
rdo = sumar(3, 8) # Positional arguments 
rdo = sumar(sumando_1=3, sumando_2=8) # es recomendable ponerlo así

# Función CON argumentos y SIN retorno
def saludar(nombre): #no retorna nada
    print(f'Hola {nombre}')

#Función SIN argumentos y SIN retorno
def escribe_hola(): # no recibe argumentos
    print('Hola')
