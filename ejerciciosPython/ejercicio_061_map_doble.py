def sumar(a, b):
    return a + b

numeros = [1, 2, 3]
delta = [5, 8, 10]

resultado = map(sumar, numeros, delta)
print(list(resultado)) # [6, 10, 13]