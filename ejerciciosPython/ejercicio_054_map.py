# Para coger una colección de datos y aplicarles un proceso a cada uno de sus datos
capitales =[('A Coruña', 245_000), ('Lugo', 98_000),('Ourense', 105_000), ('Pontevedra', 85_000)]

def convertir_mayusculas(ciudad):
    return (ciudad[0].upper(), ciudad[1]) # devolvemos una tupla nueva ya que las tuplas son inmutables
    #return 'Jorge' # podemos devolver cualquier cosa

capitales_mayusculas = map(convertir_mayusculas, capitales)
print(list(capitales_mayusculas))