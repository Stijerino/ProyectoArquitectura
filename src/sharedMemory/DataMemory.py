from src.parentClases.SharedComponent import *

class DataMemory (SharedComponent):

    memory = [i for i in range(0, 384)]
    blockSize = 4
    bus = True

    def __init__(self):
        for i in range (384):
            self.memory[i] = i


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