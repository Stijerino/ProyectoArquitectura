from src.parentClases.SharedComponent import *
import math

class InstructionMemory(SharedComponent):

    memory = [0 for i in range(384,1024)]
    blockSize = 4
    reservedBus = False

    def __init__(self):
        for i in range(384,1024):
            self.memory[i-384] = 0

    def getBus(self):

        if self.reservedBus == False:
            self.reservedBus = True
        else:

            pass
    def releaseBus(self):
        self.reservedBus = False


    def isAvailable(self):
        return (not self.reservedBus)

    def getBlock(self,blockNumber):
        '''
        Encuentra y devuelve un bloque de datos.
        :param blockNumber: El número de bloque a obtener
        :return: un vector con 16 elementos, o [] si el bloque no existe
        #todo: Confirmar que son 16 elementos
        '''

        block = []

        if blockNumber >= 0: #todo: verificar que bloque sea menor que el maximo
            block = [self.memory[blockNumber * 16 + i] for i in range(0,16)] #obtiene los 16 bytes del bloque

        return block

    def writeInstruction(self,instruction,address):
        '''
        Escribe una instruccion con sus 4 palabras en la dirección especifiada
        :param instruction: un vector con las 4 palabras. Deben ser enteros
         :param address: la dirección donde se debe colocar la instruccion
        '''
        blockNumber = math.floor(address / 16)
        blockIndex = (address % 16) // 4


        if blockNumber >= 0 and blockIndex >= 0:
            for i in range(0,4):
                self.memory[blockNumber * 16 + blockIndex * 4 + i] = instruction[i]

    def printMemory(self):
        '''
        Imprime el estado de la memoria de instrucciones
        '''

        print("Estado de la memoria de instrucciones: ")

        for i in range(0,len(self.memory)):
            print(self.memory[i], end=(' ' * (6 - len(str(self.memory[i]))))) #todo: mejorar formato de impresion

            if i %  30 == 29:
                print()
        print()





