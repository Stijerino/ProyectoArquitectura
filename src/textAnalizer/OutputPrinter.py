'''
Esta clase se encarga de generar una salida de forma sincronizada entre hilos. De este modo, es posible
observar de forma controlada el comportamiento de los 2 cores para debug y revisión del proyecto.
'''

import threading
import time

class OutputPrinter:

    semaphore = 0
    file_handler = 0
    debugging = 1

    def __init__(self, output_filename):
        '''
        Inicializa el semáforo y abre el archivo.
        Es responsabilidad del llamador hacer un llamado al método closeFile
        :param output_filename: El nombre y ruta relativa del archivo de salida.
        '''
        self.semaphore = threading.Semaphore()
        self.file_handler = open(output_filename,"w")

    def debug(self,message):

        if self.debugging == 1:
            self.log(message)
            time.sleep(0.0000000000000000000000001)  # todo: esperar un poco para que el mismo hilo no obtenga otra vez la impresion


    def log(self,message):
        '''
        Imprime un mensaje tanto en consola como en el archivo de salida
        :param message:  El mensaje a imprimir.
        '''
        self.printMessage(message)
        self.printFile(message)



    def printMessage(self,message, end = '\n'):
        '''
        Imprime un mensaje en un archivo.
        :param message: El mensaje
        :param end: Opcional. La forma en la que se quiere terminar el mensaje. Salto de línea por defecto
        '''
        self.semaphore.acquire()
        print(message, end=end)
        self.semaphore.release()

    def printFile(self, message):
        '''
        Imprime un mensaje en una línea de texto de forma sincronizada.
        :param message: El mensaje a imprimir
        '''
        self.semaphore.acquire()
        self.file_handler.write(message + "\n")
        self.semaphore.release()



    def closeFile(self):
        '''
        Cierra el archivo.
        '''
        self.file_handler.close()