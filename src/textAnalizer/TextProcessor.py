from src.textAnalizer.Context import *

class TextProcessor :
    def processFile(self, fileNameList, sharedData,sharedInstructions):

        contextsList = []

        for fileName in fileNameList:
            context = Context()

            data = open(fileName)

            for line in data:
                #Coloca las instrucciones en la  memoria de instrucciones
                pass

            contextsList.append(context)

        return contextsList