def sumar(s1, s2):
    r = s1 + s2
    del s1
    del s2
    return r

sumando_1 = 5
sumando_2 = 6
resultado = sumar(sumando_1, sumando_2)
print(resultado)