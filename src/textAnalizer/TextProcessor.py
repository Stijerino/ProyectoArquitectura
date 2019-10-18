from src.textAnalizer.Context import *

class TextProcessor :
    def processFile(self, fileName, sharedData,sharedInstructions):
        context = Context()
        contextsList = [context] * 10 #así se simula que es una lista de contextos
        return contextsList