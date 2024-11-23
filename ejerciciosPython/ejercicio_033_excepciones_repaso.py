try:
    # Este bloque de código puede potencialmente lanzar una excepción
    # como consecuencia de una operación fallida
    pass
except: # captura todos los errores
    pass

#################################################################################################
try:
    # Este bloque de código puede potencialmente lanzar una excepción
    # como consecuencia de una operación fallida
    pass
except BaseException: # captura todos los errores de BaseException -> no hay diferencia con la anterior
    pass

#################################################################################################
try:
    # Este bloque de código puede potencialmente lanzar una excepción
    # como consecuencia de una operación fallida
    pass
except BaseException as be: # recoge la información en el objeto be
    pass

#################################################################################################
try:
    # Este bloque de código puede potencialmente lanzar una excepción
    # como consecuencia de una operación fallida
    pass
# va comprobando si es un error u otro y cuando lo encuentre lanzará la excepción 
# (Importa el orden, al ser hijos de):
except ZeroDivisionError as zde: 
    pass
except ArithmeticError as ae:
    pass
except Exception as e:
    pass
except BaseException as be: 
    pass

#################################################################################################
try:
    # Este bloque de código puede potencialmente lanzar una excepción
    # como consecuencia de una operación fallida
    pass
except (ValueError, IndexError) as ae: # si la excepción es de ValueError o IndexError lo recogerá
    pass
finally: # se ejecuta siempre, haya o no error
    pass

#################################################################################################
try:
    # Este bloque de código puede potencialmente lanzar una excepción
    # como consecuencia de una operación fallida
    pass
except (ValueError, IndexError) as ae: # si la excepción es de ValueError o IndexError lo recogerá
    pass
else: # se ejecuta si no hay error
    pass

#################################################################################################
try:
    # línea 1
    # línea 2
    # línea 3
    # línea 4
    # línea 5
    pass
except IndexError as ie: 
    pass
