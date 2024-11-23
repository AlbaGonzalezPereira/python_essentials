class Pila:
    def __init__(self) -> None:
        self.__pila = list()

    def push(self, elemento) -> None: # es como un método push
        self.__pila.append(elemento) # añade el elemento en el último lugar

    def pop(self) -> any:
        elemento_eliminado = self.__pila.pop()
        return elemento_eliminado
    '''
    ############################### OTRA MANERA ###############################
    def push_artesanal(self, item) -> None:
        self.__pila.insert(0, item) # inserta en la posición que le indiquemos, en este caso, al inicio

    def pop_artesanal(self) -> any:
        item = self.__pila[0]
        del self.__pila[0] # del es para eliminar cualquier cosa
        return item
    ###########################################################################
    '''

    # para que nos saque los elementos de la lista en string. Print de un objeto
    def __str__(self) -> str:
        cadena =''
        for elemento in self.__pila:
            cadena+=f'| {elemento} |\n'
        # return "str"
        return cadena
    
    # representación del objeto. Cuando se hace un print de una estructura con objetos
    def __repr__(self) -> str:
        cadena =''
        for elemento in self.__pila:
            cadena+=f'{elemento}, '
        # return "str"
        return cadena

# clase heredada, con herencia múltiple
#class PilaContadora(Pila, Mamifero): # hereda de la clase Pila y de la clase Mamífero
#class PilaContadora(object): # todas las clases herdan de la superclase Object
class PilaContadora(Pila):
    contador = 0

    def mostrar_contador(self):
        print(PilaContadora.contador)

    # Sobreescritura (override) de método
    def push(self, item) -> None:
        PilaContadora.contador+=1
        # llama al método push de la clase Pila
        #super().push(item) # Opción 1
        Pila.push(self, item) # opción 2

    def pop(self) -> any:
        PilaContadora.contador-=1
        eliminado = super().pop()
        return eliminado



#pila = Pila()
pila = PilaContadora() # funciona exactamente igual porque hereda de la anterior
pila2 = PilaContadora()
pila.push('paraguas')
pila.push('3')
pila.push('jabón')
#print(pila) # <__main__.Pila object at 0x000002328D5F6A50> si no tenemos el método __str__
#ultimo = pila.pop()
#print(ultimo)
pila2.push('sal')
pila2.push('18')
pila.mostrar_contador()
eliminado = pila2.pop()
pila.mostrar_contador()
print(f'Elemento eliminado: {eliminado}')



'''
pila_artesanal = Pila()
pila_artesanal.push_artesanal('1')
pila_artesanal.push_artesanal('2')
pila_artesanal.push_artesanal('3')
pila_artesanal.push_artesanal('4')
print(pila_artesanal)
ultimo_artesanal = pila_artesanal.pop_artesanal()
print(ultimo_artesanal)
'''