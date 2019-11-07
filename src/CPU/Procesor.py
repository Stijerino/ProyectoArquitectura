from src.sharedMemory.DataMemory import *
from src.sharedMemory.InstructionMemory import *
from src.CPU.Core import *
from src.textAnalizer.Context import *
from src.textAnalizer.TextProcessor import *
from src.buses.InstructionBus import *
from src.buses.DataBus import  *

import glob
import threading

class Procesor:
    dataMemory = DataMemory
    instructionsMemory = InstructionMemory
    clock = 0
    core0 = Core
    core1 = Core
    nextContext = 0 #El siguiente contexto del array
    numBlocks = 0 #Cambiar
    blockSize = 0 #Cmabiar
    contextList = []
    availableContext = [True] * 5 #Se cambian según los contextos que yo entregue
    totalHilillos = 0
    doneHilillos = 0

    dataBus = 0
    instructionBus = 0

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

        self.initAvailableContexts()

        #todo: imprimir solo cuando se hayan acabado los hililos
        self.printResults()




    def initAvailableContexts(self): #Hay que hacer la inicialización
        '''
        Instancia los hilos, las caches, buses y realiza la asignación de hilillos.
        '''

        self.dataBus = DataBus()
        self.instructionBus = InstructionBus()

        #todo Inicializar caches

        self.core0 = Core(self.dataBus,self.instructionBus, self.dataMemory, self.instructionBus)
        #self.core1 = Core(self.dataBus, self.instructionBus)

        #Ind2ican si los nucleos estan disponibles
        availableCore0 = True
        availableCore1 = True

        #Agarra los contextos y los asigna a los respectivos hilillos
        lastContextIndex = 0

        while lastContextIndex < self.totalHilillos:
            if availableCore0 == True:
                availableCore0 = False

                #Crea un nuevo hilo. Solo hasta que el hilo termine se desocupa el core
                #hilo0 = threading.Thread(target=self.core0.startContext, args=(self.contextList[lastContextIndex]))

                if(lastContextIndex < self.totalHilillos):
                    hilo0 = threading.Thread(target=self.assignThread(self.core0,self.contextList[lastContextIndex]))
                    ++lastContextIndex
                    hilo0.start()

                lastContextIndex+=1

            else:
                if availableCore1 == True:
                    #lastContextIndex +=1
                    availableCore1 = False
                else:
                    #todo: Debe aplicar algun mecanismo de sincronización para esperar a que alguno de los 2 hilos
                    pass



        pass

    def assignThread(self, pCore, pContext): #Al pCore le paso el pContext
        '''
        Funcion intermediaria. Corre el hilo con el contexto actuak
        :param pCore:
        :param pContext:

        '''
        pCore.startContext(pContext)

    def getNextHilillo(self):
        pass


    def printResults(self):
        '''
        Imprime la lista de contextos y el estado de la memoria
        :return:
        '''
        self.dataMemory.printMemory()
        self.instructionsMemory.printMemory()
        print("Lista de contextos:")
        for context in self.contextList:
            context.printContext()

        print("--Total de contextos: " + str(len(self.contextList)))