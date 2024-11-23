# Crear la clase factura
# Crear una instancia
from gtts import gTTS
import os

class Factura:
    def __init__(self, numero_factura, nombre_empresa, nif_empresa, nombre_cliente, nif_cliente, importe) -> None:
        self.numero_factura = numero_factura
        self.nombre_empresa = nombre_empresa
        self.nif_empresa = nif_empresa
        self.nombre_cliente = nombre_cliente
        self.nif_cliente = nif_cliente
        self.importe = importe

    # método que guarda una factura en un archivo txt - más sencillo
    def guardar(self):
        # Guarda los datos de la factura en un fichero
        fichero = open('factura.txt', mode='w', encoding='utf-8') # abrimos un fichero
        fichero.write('Núm. Factura: '+ self.numero_factura + '\n' + 'Nombre de la empresa: '+ self.nombre_empresa + '\n' + 'NIF empresa: ' + self.nif_empresa + '\n' + 'Nombre cliente: '+ self.nombre_cliente + '\n' + 'NIF cliente: ' + self.nif_cliente + '\n' + 'Importe: ' + str(self.importe)) # escribimos en el fichero
        fichero.close() # cerramos el fichero

    #método para que nos guarde una factura en un archivo .txt por número
    def guardar_mejorado(self):
        with open(f'{self.numero_factura}.txt', mode = 'w', encoding='utf-8') as fichero:
            fichero.write('Núm. Factura: '+ self.numero_factura)
            fichero.write('\n')
            fichero.write('Nombre de la empresa: '+ self.nombre_empresa)
            fichero.write('\n')
            fichero.write('NIF empresa: ' + self.nif_empresa)
            fichero.write('\n')
            fichero.write('Nombre cliente: '+ self.nombre_cliente)
            fichero.write('\n')
            fichero.write('NIF cliente: ' + self.nif_cliente)
            fichero.write('\n')
            fichero.write('Importe: ' + str(self.importe)) # escribimos en el fichero

    # método para que una factura que nos cante los datos
    def hacer_locucion(self, idioma):
        cadena_locucion = f'La factura con número {self.numero_factura} de {self.nombre_empresa}, cuyo ciente es {self.nombre_cliente}, tiene un importe de {self.importe}'
        tts = gTTS(cadena_locucion, lang=idioma)
        tts.save(f'{self.numero_factura}.mp3') # crea un mp3 de lo que se escribe arriba
        os.system(f'start {self.numero_factura}.mp3') # lo ejecuta

factura1 = Factura('001', 'Carnicería Lucas', 'G-67654332', 'Alba González', '78765454R', '35.7€')
factura2 = Factura('002', 'Pescadería Julia', 'X-12345678', 'Julia Malvido', '12345768L', '300.0€')
factura1.pagado = True # Crea un atributo en tiempo de ejecución
print(factura1)
print(f'El número de factura {factura1.numero_factura} es del cliente {factura1.nombre_cliente}')
factura1.guardar()
factura2.guardar_mejorado()
factura1.hacer_locucion('es')
factura2.hacer_locucion('es')
