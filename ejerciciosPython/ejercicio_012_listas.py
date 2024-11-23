# formas de crear listas
lista = ['luns', 'martes', 'mercores', 'xoves', 'venres', 'sabado', 'domingo']
lista = []
lista = list() # crea una lista (vacía si no le pasamos nada). Es un constructor
#lista = list((3,4,5)) # crea una lista a partir de una tupla (3,4,5)
tupla = (3,4,5)
lista = list(tupla)
# modificar elementos de una lista
lista[1] = 6 # Asignación -> en este caso modificamos el 4 por el 6 - 3,6,5
lista.insert(1,10) # Inserción - 3, 10, 6, 5
lista.append(20) # agrega un objeto al final de la lista - 3, 10, 6, 5, 20
print(lista) # comprobamos

############################## ORDENAR ####################################
#lista.sort() # método que ordena una lista y la modifica
#print(lista) # [3, 5, 6, 10, 20]
lista_ordenada = sorted(lista) # sorted() ordena pero no modifica la lista. Devuelve una nueva lista ordenada. Lo usaremos cuando no quiera modificar la original
print(lista_ordenada)# [3, 10, 6, 5, 20]
lista_ordenada.sort(reverse=True)
print(lista_ordenada) # [20, 10, 6, 5, 3] ordena al revés

############################## SLICING #################################################
print(lista[0:2]) # [3, 10] muestra el rango del índice 0 al 2, sin coger el de índice 2
print(lista[1:2]) # [10]
print(lista[:3]) # [3, 10, 6] - coge del primero hasta el elemento del índice dado
print(lista[3:]) # [5, 20]
print(lista[:]) # [3, 10, 6, 5, 20] # genera una lista nueva sin modificar la original
print(lista[0:4:2]) # [3, 6] - coge del 0 al 4 de 2 en 2
print(lista[-1:]) # [20]
print(lista[-2:]) # [5, 20]
print(lista[-3:-1]) # [6, 5]
mi_slice = slice(0,2) # prepara un corte
print(lista[mi_slice]) # [3, 10]

lista.reverse() # Invierte la lista pero no ordena

# in - para preguntar si un elemento está en una lista
print(3 in lista) # True
print(3 not in lista) # False