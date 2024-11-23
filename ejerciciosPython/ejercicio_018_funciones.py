#Función con argumento con valor por defecto
def sumar(sumando_1 : int, sumando_2 : int = 10) -> int: # el valor por defecto, en caso de ser uno, tiene que estar de segundo
    resultado = sumando_1 + sumando_2
    return resultado

print(sumar(3,2)) # cuando pase el sumando 2, cogerá el valor pasado - 5
print(sumar(8)) # coge el valor por defecto - 18

# Relación indeterminada de parámetros
def saludar(*args : str): # le puedo pasar ninguno o varios strings
    print(args) # si se hiciera un return devolvería una tupla

saludar() # resultado -> ()
saludar('uno') # ('uno',)
saludar('uno','dos') # ('uno', 'dos')
saludar('uno','dos','tres') # ('uno', 'dos', 'tres')