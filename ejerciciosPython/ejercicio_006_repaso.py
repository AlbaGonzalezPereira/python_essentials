# hacer lista, tupla, diccionario, conjunto y recorrerlos

animales = ['mono', 'perro', 'gato']
for animal in animales:
    print('Animal:', animal)

numeros_primos = (1, 3, 5, 7)
for numero_primo in numeros_primos:
    print(numero_primo, end=';')

print()
almacen_datos = {'galletas', 3, True }
for dato in almacen_datos:
    print(dato)

jugador_localidad = {'nombre':'Fernando', 'localidad':'Pontevedra'}
for clave, valor in jugador_localidad.items():
    print(clave, valor)

