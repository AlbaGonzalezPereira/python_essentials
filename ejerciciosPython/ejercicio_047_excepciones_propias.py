# Cuando ninguna execpcón se ajusta a nuestros errores, creamos una clase con excepción propia
#class HoraequivocadaException(Exception):
#    pass

'''
class ClaseNormal(object):
    pass

try:
    raise ClaseNormal() # permite hacer una excepción de cualquier clase
except ClaseNormal as cn: # TypeError: catching classes that do not inherit from BaseException is not allowed
    print('Except')
'''
#x = ArithmeticError(1, 5, 'hola', True)


class ConflictoError(ArithmeticError):
    def __init__(self, *args, usuario):
        ArithmeticError.__init__(self, *args) 
        self.usuario = usuario
    
    def get_user_name(self):
        return 'Soy ' + self.usuario


def sumar(s1, s2):
    if (s1==s2):
        raise ConflictoError('Hay un conflicto', 'No sé qué hacer', usuario='Fernando')
    return s1 + s2

try:
    sumar(3, 3)
except ConflictoError as ce:
    print(ce) # <class '__main__.ConfictoError'>: Muestra lo mismo que args - ('la suma es imposible', 'No sé qué hacer')
    print(ce.args) # tuple: Contiene la tupla de argumentos posicionales suministrados al constructor - ('la suma es imposible', 'No sé qué hacer')
    print(ce.__dict__) # {'usuario': 'Fernando'}
    print(ce.usuario) # Fernando
    print(ce.get_user_name())  # Soy Fernando

