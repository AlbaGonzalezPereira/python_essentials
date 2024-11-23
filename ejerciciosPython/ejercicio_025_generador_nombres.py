from random import choice
# Crear una lista con los nombres y apellidos de 1000 personas
# Recorrer la lista con un for y mostrarla por pantalla

nombres = ('Alba', 'Pablo', 'Ricardo', 'Manuel', 'Nahir')
apellidos = ('Rodríguez', 'Sánchez', 'López', 'Martínez', 'Gómez')

nombres_completos = list()
for i in range(1000):
    nombre_completo = f'{choice(nombres)} {choice(apellidos)} {choice(apellidos)}'
    nombres_completos.append(nombre_completo)

for nombre in nombres_completos:
    print(nombre)