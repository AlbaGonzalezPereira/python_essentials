# Un closure es una función que nos devuelve una función y permite demorar la ejecución en el tiempo
def convertir(nombre):
    def funcion_interna():
        return nombre.upper()
    return funcion_interna

nombre = 'python'
funcion = convertir(nombre)
nombre = 'java' # aunque cambie de valor no coge este
print(funcion()) # PYTHON
