# Las funciones lambda son de un solo uso. Definimos la función donde se va a usar:
capitales =[('A Coruña', 245_000), ('Lugo', 98_000),('Ourense', 105_000), ('Pontevedra', 85_000)]

'''
def es_grande(ciudad):
    return ciudad[1]>100_000
'''
grandes_capitales = filter(lambda ciudad : ciudad[1]>100_000, capitales) # miramos la función es_grande
print(list(grandes_capitales)) # [('A Coruña', 245000), ('Ourense', 105000)]

'''
def sumar(a, b):
    return a + b
x = lambda a, b : a + b

print(x(5,8))
'''
capitales_mayusculas = map(lambda ciudad : (ciudad[0].upper(), ciudad[1]), capitales)
'''
def convertir_mayusculas(ciudad):
    return (ciudad[0].upper(), ciudad[1]) # devolvemos una tupla nueva ya que las tuplas son inmutables
    #return 'Jorge' # podemos devolver cualquier cosa

capitales_mayusculas = map(convertir_mayusculas, capitales)
'''
print(list(capitales_mayusculas)) # [('A CORUÑA', 245000), ('LUGO', 98000), ('OURENSE', 105000), ('PONTEVEDRA', 85000)]
