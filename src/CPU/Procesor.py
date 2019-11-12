from src.sharedMemory.DataMemory import *
from src.sharedMemory.InstructionMemory import *
from src.CPU.Core import *
from src.textAnalizer.Context import *
from src.textAnalizer.TextProcessor import *
from src.buses.InstructionBus import *
from src.buses.DataBus import  *
from src.textAnalizer.OutputPrinter import *

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
    outputPrinter = 0
    barrera = threading.Semaphore()

    # Indican si los nucleos estan disponibles
    availableCore0 = True
    availableCore1 = False #TODO MUY IMPORTANTE: Cambiar esto hasta que ya se quieran probar los hilillos sincronizados

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
        Instancia los hilos, las caches, buses, manejador de salida y realiza la asignación de hilillos.
        '''

        self.dataBus = DataBus()
        self.instructionBus = InstructionBus()
        self.outputPrinter = OutputPrinter("salida.txt")
        self.barrera = threading.Semaphore()

        #todo Inicializar caches

        self.core0 = Core(0,self.dataBus,self.instructionBus, self.dataMemory, self.instructionsMemory, self.outputPrinter)
        self.core1 = Core(1,self.dataBus,self.instructionBus, self.dataMemory, self.instructionsMemory, self.outputPrinter)



        hilos = []

        #Agarra los contextos y los asigna a los respectivos hilillos
        lastContextIndex = 0



        while lastContextIndex < self.totalHilillos:


            if self.availableCore0 == True:
                self.availableCore0 = False

                #Crea un nuevo hilo. Solo hasta que el hilo termine se desocupa el core
                if(lastContextIndex < self.totalHilillos):

                    self.contextList[lastContextIndex].setCore(0)
                    hilo0 = threading.Thread(target=self.assignThread,args=(self.core0,self.contextList[lastContextIndex]))
                    lastContextIndex += 1
                    hilos.append(hilo0)


                #availableCore0 = True

            if self.availableCore1 == True:
                self.availableCore1 = False

                # Crea un nuevo hilo. Solo hasta que el hilo termine se desocupa el core
                if (lastContextIndex < self.totalHilillos):
                    self.contextList[lastContextIndex].setCore(1)

                    hilo1 = threading.Thread(target=self.assignThread2,args=(self.core1, self.contextList[lastContextIndex]))
                    hilos.append(hilo1)



                    lastContextIndex += 1


                #availableCore1 = True


            for h in hilos:
                h.start()
            hilos = []

        #No imprime los resultados hasta que todos los hilos hayan terminado
        for i in range(0,self.totalHilillos+1):
            self.barrera.acquire()




    def assignThread(self, pCore, pContext): #Al pCore le paso el pContext
        '''
        Funcion intermediaria. Corre el hilo con el contexto actuak
        :param pCore:
        :param pContext:

        '''
        pCore.startContext(pContext)
        self.availableCore0 = True
        self.barrera.release()
        return

    def assignThread2(self, pCore, pContext):  # Al pCore le paso el pContext
        '''
        Funcion intermediaria. Corre el hilo con el contexto actual
        :param pCore:
        :param pContext:

        '''
        pCore.startContext(pContext)
        self.availableCore1 = True
        self.barrera.release()
        return

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