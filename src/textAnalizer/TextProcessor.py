from src.textAnalizer.Context import *

class TextProcessor :
    def processFile(self, fileNameList, sharedData,sharedInstructions):
        '''
        Lee las instrucciones de cada hilillo., las almacena en la memoria de instrucciones
        y crea un nuevo contexto por cada hilillo.
        :param fileNameList: La lista con los nombres de archivos txt que corresponden a hilillos
        :param sharedData: La memoria de datos
        :param sharedInstructions: La memoria de instrucciones
        :return: La lista de contextos
        '''

        contextsList = []
        instruction_counter = 0
        file_counter = 0

        for fileName in fileNameList:
            context = Context() #instancia un nuevo contexto
            context.setInstructionIndex((instruction_counter * 4 ) + 384)

            data = open(fileName)

            for line in data:
                #Convierte las palabras de la instruccion a enteros y la almacena en la memoria de instrucciones
                instruction = line.strip().split(" ")

                for i in range(0,len(instruction)):
                    instruction[i] = int(instruction[i])

                sharedInstructions.writeInstruction(instruction,instruction_counter * 4) # 4 = tamaño de la instrucción
                instruction_counter += 1

            context.setId(file_counter)
            contextsList.append(context)
            file_counter+=1

        return contextsList