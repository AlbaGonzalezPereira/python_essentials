###### Tipos básicos de apertura: 
# r-lectura, 
# w-escritura con borrado,
# a-escritura a continuacion (append)
#
###### Tipos básicos de apertura según el tipo de dato:
# t-texto
# b-binary
#
# Por defecto: mode='rt'
# Por defecto, siempre texto (t)
'''
fichero = open('C:/Users/usuario/Documents/Alba/ejerciciosPython/borrar.txt', mode='r', encoding='utf-8') # los ficheros se abren con open()
fichero.write('Hola')
fichero.readline() # io.UnsupportedOperation: not readable
fichero.close() # apertura con función y cierre con método
'''
fichero_poema = open('./poema.txt', mode='rt', encoding='utf-8')
#print(fichero_poema.read()) # Todo el fichero, str
print(fichero_poema.read(20)) # Cadena de caracteres con los 20 primeros - 'Hay dulzura infantil'
print(fichero_poema.read(20)) # lee los 20 siguientes - En la mañana quieta
fichero_poema.seek(0) # Pone el puntero en la posición 0
print(fichero_poema.readline()) # readline() lee una línea y avanza. Lee un salto de línea
print(f'#{fichero_poema.readline().replace('\n','')}#') # para que no lea los saltos de línea, los sacamos - #En la mañana quieta.#
print(fichero_poema.readlines()) # Todo, list - ['En la mañana quieta.\n', 'Los árboles extienden\n', 'Sus brazos a la tierra.\n', .....
print(fichero_poema.readlines(15)) # ['Hay dulzura infantil\n']
fichero_poema.close()

fichero = open('./poema.txt', mode = 'w', encoding='utf-8')

for line in open('./poema.txt', encoding='utf-8'): # lee línea a línea
    print(line)
    break

for line in open('./poema.txt', encoding='utf-8'): # lee línea a línea
    print(line)
    break

