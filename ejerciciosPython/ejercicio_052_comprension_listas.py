def duplicar(numero):
    return numero*2

def triplicar(numero):
    return numero*3

numeros = [1, 2, 3, 4, 5]
duplicados = [duplicar(numero) for numero in numeros]
dobles = [numero*2 for numero in numeros]
print(dobles) # [2, 4, 6, 8, 10]
triples = [triplicar(numero) for numero in numeros]
dobles_pares = [numero*2 for numero in numeros if numero%2==0]
dobles_impares = [numero*2 if numero%2==1 else 'ERROR' for numero in numeros]
print(dobles_impares) # [2, 'ERROR', 6, 'ERROR', 10]

#Comprensión de listas utilizando paréntesis
generador = (numero*2 for numero in numeros)
print(generador) # <generator object <genexpr> at 0x00000223367FA8E0>
lista_generada = list(generador) # es una lista
print(lista_generada) # [2, 4, 6, 8, 10] 
