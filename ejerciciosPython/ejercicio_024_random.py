import random
import math

#random.random
print(random.random()) # n>=0 and n<1
print(math.ceil(random.random()*100)) # n>0 and n<=100

#random.seed
random.seed(100)
print(random.random()) # Con una misma semilla, misma secuencia
print(random.random())
print(random.random())

#random.randrange
random.seed() # Indicamos que tome como semilla la hora
print(random.randrange(0,10)) #Selecciona un elemento de un range
print(random.randrange(0,10,2)) #Selecciona un elemento de un range

#random.randint
print(random.randint(0,3)) #Selecciona un elemento en el segmento [0,3]

#random.choise
lista = ['Alba', 'Pablo', 'Ricardo', 'Manuel', 'Nahir']
print(random.choice(lista))