def is_open(window):
    print(f'Evaluando si {window} está abierta')
    # return True
    return False

# Si una de las expresiones es True, no evalúa la siguiente
if (is_open('Ventana1')) or (is_open('Ventana2')): # evalúa si la primera es true
    print('Hay una ventana abierta')

# Evalúa todas las expresiones
if (is_open('Ventana3')) | (is_open('Ventana4')): # | -> evalúa todas las expresiones
    print('Hay una ventana abierta')

# Si una de las expresiones es False, no evalúa la siguiente
if (is_open('Ventana5')) and (is_open('Ventana6')): # evalúa si la primera es true
    print('Todas las ventanas están abiertas')

# Evalúa todas las expresiones
if (is_open('Ventana7')) & (is_open('Ventana8')): # | -> evalúa todas las expresiones
    print('Todas las ventanas están abiertas')