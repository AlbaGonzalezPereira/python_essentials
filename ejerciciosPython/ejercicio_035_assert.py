def sumar(s1, s2):
    assert isinstance(s1, int), "s1 no es int"
    assert isinstance(s2, int), "s2 no es int"
    resultado = s1 + s2
    return resultado

print(sumar(3, 8)) # 11
print(sumar(3, 8.2)) # AssertionError: s2 no es int -> estos errores no se tratan