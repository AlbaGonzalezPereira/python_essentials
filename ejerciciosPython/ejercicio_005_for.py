numeros = (1,2,3,4,-8) #tupla

for numero in numeros:
    print(numero*2,end='-')

#EJERCICIO:
# Haced una lista con 5 nombres propios
nombres = ['Juan', 'Ana', 'Pedro', 'Sofía', 'Nuria']

#Recorred lista y preguntad si el nombre contiene la letra 'a'
for nombre in nombres:
    #if nombre.find('a') > -1: # si es 'A' no la encontraría -> el método find() devuelve la posición
    if nombre.upper().find('A') >-1: # convierte el nombre a mayúsculas y busca si hay una 'A' en el nombre
        print(nombre)
