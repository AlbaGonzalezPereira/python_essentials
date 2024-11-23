'''
Modos son (opcional, por defecto r):
- w (escritura -borra el anterior si lo hay-)
- a (escritura -añadiendo-)
- r (lectura)

Encoding (opcional):
- utf-8
'''
fichero = open('salida.dat', mode='w') # abrimos un fichero
fichero.write('Este texto quiero quede escrito') # escribimos en el fichero
fichero.close() # cerramos el fichero

with open('salida.ttr', mode='w', encoding='utf-8') as mi_fichero: # with open cierra el fichero al final del bloque
    mi_fichero.write('Esto también')