from src.sharedMemory.DataMemory import *
from src.sharedMemory.InstructionMemory import *
from src.CPU.Core import *
from src.textAnalizer.Context import *
from src.textAnalizer.TextProcessor import *

import glob

class Procesor:
    dataMemory = DataMemory
    instructionsMemory = InstructionMemory
    Clock = 0
    Core0 = Core
    Core1 = Core
    nextContext = 0 #El siguiente contexto del array
    numBlocks = 0 #Cambiar
    blockSize = 0 #Cmabiar
    contextList = []
    availableContext = [True] * 5 #Se cambian según los contextos que yo entregue
    totalHilillos = 0
    doneHilillos = 0

    def initMemory(self):
        #Inicializa las memorias
        self.dataMemory = DataMemory()
        self.instructionsMemory = InstructionMemory()

    def startProgram(self):

        self.initMemory()

        #Obtiene una lista con todos los hilillos presentes en la carpeta hilillos.
        file_list = glob.glob('../hilillos/' + '*.txt')
        self.totalHilillos = len(file_list)

        textProcessor = TextProcessor()
        self.contextList = textProcessor.processFile(file_list,self.dataMemory,self.instructionsMemory)


        #todo: imprimir solo cuando se hayan acabado los hililos
        self.printResults()




    def initAvailableContexts(self): #Hay que hacer la inicialización
        '''
        '''
        pass

    def assignThread(self, pCore, pContext): #Al pCore le paso el pContext
        pass

    def getNextHilillo(self):
        pass


    def printResults(self):
        '''
        Imprime la lista de contextos y el estado de la memoria
        :return:
        '''
        self.instructionsMemory.printMemory()
        print("Lista de contextos:")
        for context in self.contextList:
            context.printContext()

        print("--Total de contextos: " + str(len(self.contextList)))