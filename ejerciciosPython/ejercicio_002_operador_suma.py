#operador suma --> operador sobrecargado
print(3+4) #7 - int OPERACIÓN ARITMÉTICA
print('3' + '4')# '34' - str CONCATENA
print(3,4) #3 4 --> se imprimen los caracteres (3 y 4) separados por espacios
print(3,4,sep='*')#3*4 --> se imprimen los caracteres (3 y 4) separados por *
print(3,4,sep='raton')
print() # salto de línea
print(3,4,sep='***') # 3***4
print(3,4,end='==') # 3 4== (sin salto de línea)
print(3,4,sep='***', end='==') # 3***4==

def saludar(*nombre : object, sep = " "): #va a recibir un número indeterminado de nombres separados por espacios
    print()

nombre='Fernando'
#numero_caracteres = len('Fernando') #la función len() devuelve un entero y el resultado lo puedo meter en una variable
numero_caracteres = len(nombre)
print(numero_caracteres)

#Fernando tiene 8 caracteres
print(nombre,'tiene',numero_caracteres,'caracteres.')
#print(nombre+'tiene'+numero_caracteres+'caracteres.') #da error porque numero_caracteres es número y no es capaz de concatenar
print(nombre+' tiene '+str(numero_caracteres)+' caracteres.') #utilizamos la función str()

#f-string --> generar una cadena de caracteres
print(f'{nombre} tiene {numero_caracteres} caracteres.') #interpolación de variables
