class Factura:
    def __init__(self, importes):
        self.importes = importes

def obtener_total(self):
    return sum(self.importes)

# Creamos una instancia de Factura
f = Factura([1,2,3,4,5])

#incorporamos un nuevo método a Factura
Factura.dame_total = obtener_total # asignamos la función, no el resultado

print(f.dame_total()) # 15