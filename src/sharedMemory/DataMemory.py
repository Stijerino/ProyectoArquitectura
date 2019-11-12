from src.parentClases.SharedComponent import *

class DataMemory (SharedComponent):

    memory = [i for i in range(0, 384)]
    blockSize = 4
    bus = True

    def __init__(self):
        for i in range (384):
            self.memory[i] = i

    def traerBloque(self,numeroBloque):
        '''
        Trae el bloque completo
        :param numeroBloque: El numero de bloque a traer
        :return: un vector de 4 elementos, osea el bloque.
        '''

        direccion = (numeroBloque * self.blockSize)

        return self.memory[direccion: direccion + 4]

    def escribirPalabra(self,direccion,palabra):
        '''
        Escribe una palabra en memoria
        :param direccion: la direccion en memoria donde se debe escribir la palabra
        :param palabra:
        :return:
        '''
        self.memory[direccion] = palabra



    def printMemory(self):
        '''
        Imprime el estado de la memoria de Datos
        '''

        print("Estado de la memoria de Datos: ")

        for i in range(0,len(self.memory)):
            print(self.memory[i], end=(' ' * (6 - len(str(self.memory[i])))))

            if i %  30 == 29:
                print()
        print()