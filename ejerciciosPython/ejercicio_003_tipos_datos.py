# La función type() devuelve el tipo de un objeto que se le pase. Python es un lenguage fuertemente tipado, de tipo dinámico
print(type(3)) # int
print(type(3.5)) # float
print(type(True)) # boolean
print(type('Hola')) # str

print(float(3)) # 3.0
print(int(3.8)) # 3 --> pérdida de información, trunca los decimales
print(int('3')) # 3 - int
# print(int('tres')) #ValueError
print(type(str(3.8))) # str
print(bool(0)) # False
print(bool(1)) # True
print(bool('True')) # True - bool