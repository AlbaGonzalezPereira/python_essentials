# el objetivo de un decorador es coger una función y la va a envolver en un comportamiento que no tiene.
# va a hacer algo que no tiene, como si extendiera

def saludador(funcion_decorada):
    def inner_function(*args, **kwargs):
        print('¡Hola!')
        return funcion_decorada(*args, **kwargs)
    return inner_function

@saludador # decorador
def sumar(s1, s2): # la función sumar va a hacer lo que haga la función saludador
    return s1+s2

print(sumar(3,8)) # ¡Hola! - 11