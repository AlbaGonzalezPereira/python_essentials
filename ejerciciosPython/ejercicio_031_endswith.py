ficheros = ('imagen1.jpg','datos.txt', 'juegos.zip', 'imagen2.jpg')

# Utilizando comprensión de listas, obtener los ficheros .jpg
# Utilizar método endswith

# comprensión de listas:
ficheros_jpg = [fichero for fichero in ficheros if fichero.endswith('.jpg')]
print(ficheros_jpg)

# similar al anterior pero añadiendo el fichero a la lista de ficheros_imagen
ficheros_imagen = list()
for fichero in ficheros:
    if(fichero.endswith('.jpg')):
        ficheros_imagen.append(fichero)
print(ficheros_imagen)