'''
Crear una lista
Pedir al usuario cuatro nombres y agregarlos a la lista
Mostrar la lista
Ordenar la lista
Mostrar la lista
Pedir al usuario un nombre y mostrar si está o no en la lista
Si el nombre no existe, agregarlo en la primera posición

'''
################ con while y un contador ####################
nombres = []
contador = 0
while (contador < 4):
    nombre = input(f'Ingresa el nombre número {contador+1}: ')
    nombres.append(nombre)
    contador += 1

print(nombres)
nombres.sort()
print(nombres)
nombre_usuario = input('Ingresa un nombre a buscar: ')
if(nombre_usuario in nombres):
    print(f'El nombre de {nombre_usuario} está en la lista')
else:
    print(f'El nombre de {nombre_usuario} no está en la lista')
    nombres.insert(0, nombre_usuario)
    print(nombres)

##################### con range() y con nombres en mayúsculas para evitar búsquedas erróneas ###########################
nombres_dados = []
for numero in range(4):
    nombre_pedido = input(f'Ingresa un nombre: ')
    nombres_dados.append(nombre_pedido.upper()) # podemos usar capitalize() y quedaría mejor 
    # el método capitalize() pone la primera letra en mayúsculas y las otras en minúsculas
print(nombres_dados)
nombres_dados.sort()
print(nombres_dados)
nombre_usu = input('Ingresa el nombre a buscar en la lista: ').upper()
if(nombre_usu in nombres_dados):
    print(f'El nombre de {nombre_usu} ya está en la lista')
else:
    print(f'El nombre {nombre_usu} no está en la lista')
    nombres_dados.insert(0, nombre_usu)
    print(f'Añadiendo... {nombre_usu} a la lista de nombres')
    print(nombres_dados)