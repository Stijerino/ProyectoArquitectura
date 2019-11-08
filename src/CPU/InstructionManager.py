'''
Esta clase contiene la logica para cada una de las instrucciones soportadas
por el procesador RISC-V
'''

class InstructionManager:

    def addi(self,instruccionActual,context):
        '''
        Procesa una instrucción addi
        :param instruccionActual: Suma de inmediato, de la forma op,x1,x2,n tal que x1 = x2 + n
        :param context: el contexto del core que contiene los valores en los registros
        '''
        registroDestino = instruccionActual[1]
        registroFuente = instruccionActual[2]
        inmediato = instruccionActual[3]
        suma = context.getRegister(registroFuente) + inmediato
        context.setRegister(registroDestino, suma)

    def add(self,instruccionActual,context):
        '''
        Procesa una instrucción add
        :param instruccionActual: Suma de registros,, de la forma op,x1,x2,x3 tal que x1 = x2 + x3
        :param context: el contexto del core que contiene los valores en los registros
        '''
        registroDestino = instruccionActual[1]
        registroFuente1 = instruccionActual[2]
        registroFuente2 = instruccionActual[3]
        suma = context.getRegister(registroFuente1) + context.getRegister(registroFuente2)
        context.setRegister(registroDestino, suma)



    def sub(self,instruccionActual,context):
        '''
        Procesa una instrucción sub
        :param instruccionActual: Resta de registros,, de la forma op,x1,x2,x3 tal que x1 = x2 - x3
        :param context: el contexto del core que contiene los valores en los registros
        '''
        registroDestino = instruccionActual[1]
        registroFuente1 = instruccionActual[2]
        registroFuente2 = instruccionActual[3]
        resta = context.getRegister(registroFuente1) - context.getRegister(registroFuente2)
        context.setRegister(registroDestino, resta)

    def div(self,instruccionActual,context):
        '''
        Procesa una instrucción div
        :param instruccionActual: Division de registros, de la forma op,x1,x2,x3 tal que x1 = x2 / x3
        :param context: el contexto del core que contiene los valores en los registros
        todo: Entera o flotante?
        '''
        registroDestino = instruccionActual[1]
        registroFuente1 = instruccionActual[2]
        registroFuente2 = instruccionActual[3]
        division = context.getRegister(registroFuente1) // context.getRegister(registroFuente2)
        context.setRegister(registroDestino, division)

    def mul(self,instruccionActual,context):
        '''
        Procesa una instrucción mul
        :param instruccionActual: Multiplicación de registros, de la forma op,x1,x2,x3 tal que x1 = x2 * x3
        :param context: el contexto del core que contiene los valores en los registros
        '''
        registroDestino = instruccionActual[1]
        registroFuente1 = instruccionActual[2]
        registroFuente2 = instruccionActual[3]
        multiplicacion = context.getRegister(registroFuente1) * context.getRegister(registroFuente2)
        context.setRegister(registroDestino, multiplicacion)

    def beq(self,instruccionActual,context,PC,direccionEtiqueta):
        '''
        Procesa una instrucción beq
        :param instruccionActual:  op,x1,x2,etiq tal que cambia PC si x1 = x2
        :param context: el contexto del core que contiene los valores en los registros
        :param PC: El valor viejo del PC
        :param direccionEtiqueta: La direccion a la que debe saltar. Ya debe estar calculada por el llamador

        :return El nuevo valor del contador del programa
        '''

        registro1 = instruccionActual[1]
        registro2 = instruccionActual[2]

        nuevoPC = PC

        if context.getRegister(registro1) == context.getRegister(registro2):
            nuevoPC = PC + direccionEtiqueta * 4

        return nuevoPC


    def bne(self,instruccionActual,context,PC,direccionEtiqueta):
        '''
        Procesa una instrucción bne
        :param instruccionActual: de la forma op,x1,x2,etiq tal que cambia PC si x1 != x2
        :param context: el contexto del core que contiene los valores en los registros
        :param PC: El valor viejo del PC
        :param direccionEtiqueta: La direccion a la que debe saltar. Ya debe estar calculada por el llamador

        :return El nuevo valor del contador del programa
        '''

        registro1 = instruccionActual[1]
        registro2 = instruccionActual[2]

        nuevoPC = PC

        if context.getRegister(registro1) != context.getRegister(registro2):
            nuevoPC = PC + direccionEtiqueta * 4

        return nuevoPC




