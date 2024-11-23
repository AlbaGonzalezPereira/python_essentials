# LISTA -> puedes agregar o quitar elementos
lista = [3, True, 'Hola', [3, 4,'Adiós', True]] # colección de elementos u objetos de 4 elementos, con otra lista dentro
print(lista)
print(lista[0]) # 3 -> Acceso a un elemento concreto
# recorremos los elementos de una lista. Las listas son objetos iterables
for item in lista:
    print("ITEM:", item)
    print("Hola")
    print("Python")

# TUPLAS -> no puedes modificar el tamaño. Son iterables
tupla = (3, True, 'Hola', [3, 4, 'Adios', True]) 
tupla = (3,) #tupla con un solo elemento en Python
print(tupla)
print(tupla[2]) # 'Hola' -> Acceso a un elemento concreto
#recorremos la tupla
for elemento in tupla:
    print(elemento)

# CONJUNTOS -> Sirven para saber si hay concordancias, entre intersecciones y el orden no importa.No duplicados
conjunto = {3, 4, 8, 10, 10, 10} # es como un Set, elimina los duplicados. 
print(conjunto) # el orden en el conjunto no se respeta, es aleatorio
print(10 in conjunto) # preguntamos si el elemento está en el conjunto, ya que no tiene orden ni índice
#recorremos el conjunto
for element in conjunto:
    print("Conjunto:", element)

# DICCIONARIOS -> no hay claves duplicadas, es comno un Map
diccionario = {'nombre':'Fernando', 'edad':50, 'edad':48}
print(diccionario) #{'nombre': 'Fernando', 'edad': 48} -> elimina la última
print(diccionario['nombre']) # 'Fernando' -> accedemos por la clave 
# En los diccionarios, podemos recorrer las claves, podemos recorrer los valores o podemos recorrerlo todo:
# recorremos la clave
for clave in diccionario.keys():
    print(clave)
# recorremos los valores
for valor in diccionario.values():
    print(valor)
# recorremos todo, clave y valor
for clave, valor in diccionario.items():
    print(clave, valor)

