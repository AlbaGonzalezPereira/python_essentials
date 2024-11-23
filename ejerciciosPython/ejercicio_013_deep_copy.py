import copy # debería ir al principio, aunque puede ir en cualquier sitio pero antes de ser usado

lista1 = [1, 2, 3]
lista2 = lista1

# Modificar el 2º elemento de la lista 1
# ¿Cómo quedan lista1 y lista2

lista1[1] = 5
print(lista1) # [1, 5, 3]
print(lista2) # [1, 5, 3]
print(lista1 is lista2) # True

lista1 = [1, 2, 3]
lista2 = lista1[:] # crea una lista nueva
lista1[1] = 5
print(lista1) # [1, 5, 3]
print(lista2) # [1, 2, 3]
print(lista1 is lista2) # False

lista1 = [1, 2, [3, 4]]
lista2 = lista1[:]
lista1[0] = 8
lista1[2][0] = 10
print(lista1) # [8, 2, [10, 4]]
print(lista2) # [1, 2, [10, 4]] - en el segundo nivel sigue afectando la modificación

# para resolver esto hay un método que lo resuelve que es copy.deepcopy()
lista1 = [1, 2, [3, 4]]
lista2 = copy.deepcopy(lista1) # SOLUCIÓN, DEEPCOPY
lista1[0] = 8
lista1[2][0] = 10
print(lista1) # [8, 2, [10, 4]]
print(lista2) # [1, 2, [3, 4]]

a= True
b = a
a = False
print(b) # True
print(a is b) # False

