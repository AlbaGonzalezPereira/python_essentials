# Filtra los elementos de una función.
# Coge una colección de datos y obtiene un subconjunto que cumple una condición.
capitales =[('A Coruña', 245_000), ('Lugo', 98_000),('Ourense', 105_000), ('Pontevedra', 85_000)]

def es_grande(ciudad):
    return ciudad[1]>100_000

def contiene_a(ciudad):
        return 'a' in ciudad[0]

grandes_capitales = filter(es_grande, capitales)
print(list(grandes_capitales)) # [('A Coruña', 245000), ('Ourense', 105000)]

ciudades_con_a = filter(contiene_a, capitales)
print(list(ciudades_con_a)) # [('A Coruña', 245000), ('Pontevedra', 85000)]


