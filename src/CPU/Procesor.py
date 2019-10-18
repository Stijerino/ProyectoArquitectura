from src.sharedMemory.DataMemory import *
from src.sharedMemory.InstructionMemory import *
from src.CPU.Core import *
from src.textAnalizer.Context import *

class Procesor:
    Data = DataMemory
    Instructions = InstructionMemory
    Clock = 0
    Core0 = Core
    Core1 = Core
    nextContext = 0 #El siguiente contexto del array
    numBlocks = 0 #Cambiar
    blockSize = 0 #Cmabiar
    contextList = [Context] * 5 #Resultado de aquel proc de analizer
    availableContext = [True] * 5 #Se cambian según los contextos que yo entregue
    totalHilillos = 0
    doneHilillos = 0

    def initMemory(self):
        pass

    def startProgram(self):
        pass

    def initAvailableContexts(self): #Hay que hacer la inicialización
        pass

    def assignThread(self, pCore, pContext): #Al pCore le paso el pContext
        pass

    def getNextHilillo(self):
        pass