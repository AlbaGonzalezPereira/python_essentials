姓名 = 'Alba'
print(f'Mi nombre es {姓名}') # Mi nombre es Alba

# with open('datos.txt', mode='w') as fichero: # No escribe la tilde
with open('datos.txt', mode='w', encoding='utf-8') as fichero: # abre un fichero que se llama datos.txt, que se escribe encima del anterior y que utiliza en utf-8
    fichero.write('Línea 1') 
# con with el ficehro se cierra cuando acaba el bloque de línea