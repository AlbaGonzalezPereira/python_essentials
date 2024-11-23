from unidecode import unidecode
'''
Crear una lista de palabras prohibidas
Pedir una palabra al usuario
Comprobar si la palabra está en las palabras prohibidas
'''

palabras_prohibidas = ['brócoli', 'lechuga', 'puerro']
#print(palabras_prohibidas)

#Función que elimina las tildes:

def eliminar_tilde(palabra : str) -> str:
    palabra = palabra.replace('A', 'A').replace('É','E').replace('Í', 'I').replace('Ó', 'O').replace('Ú','U')
    return palabra


# Comprensión de listas -> for con una transformación
lista_mayusculas = [eliminar_tilde(ingrediente.upper()) for ingrediente in palabras_prohibidas]
print(lista_mayusculas)

palabra = input('Pon una palabra: ')
if eliminar_tilde(palabra.upper()) in palabras_prohibidas:
    print(f'La palabra {palabra} es una de las palabras prohibidas')
else: 
    print(f'La palabra {palabra} no es una de las palabras prohibidas')


#Probando
ingredientes = ['brócoli', 'lechuga', 'puerro']

ingrediente = input('Introduce un ingrediente: ')
if unidecode(ingrediente.upper()) in ingredientes:
    print(f'El ingrediente {ingrediente} está en la lista')
else: 
    print(f'El ingrediente {ingrediente} no está en la lista')