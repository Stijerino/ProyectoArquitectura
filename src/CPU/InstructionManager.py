'''
Esta clase contiene la logica para cada una de las instrucciones soportadas
por el procesador RISC-V
'''

import math

from src.CPU.Core import *
import threading

class InstructionManager:

    semaforo0 = 0
    semaforo1 = 0

    def __init__(self,semaforo0, semaforo1):
        self.semaforo0 = semaforo0
        self.semaforo1 = semaforo1

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

    def beq(self,instruccionActual,context,PC):
        '''
        Procesa una instrucción beq
        :param instruccionActual:  op,x1,x2,etiq tal que cambia PC si x1 = x2
        :param context: el contexto del core que contiene los valores en los registros
        :param PC: El valor viejo del PC

        :return El nuevo valor del contador del programa
        '''

        registro1 = instruccionActual[1]
        registro2 = instruccionActual[2]
        offset = instruccionActual[3]

        nuevoPC = PC

        if context.getRegister(registro1) == context.getRegister(registro2):
            nuevoPC = PC + (offset * 4)

        return nuevoPC


    def bne(self,instruccionActual,context,PC):
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
        offset = instruccionActual[3]

        nuevoPC = PC

        if context.getRegister(registro1) != context.getRegister(registro2):
            nuevoPC = PC + (offset * 4)

        return nuevoPC


    def lw(self,instruccionActual, context, cacheDatosPropia, busDatos, memoriaDatos):
        '''
        Carga en un registro el valor almacenado en una posición de memoria


        :param instruccionActual: De la forma x1,x2,n donde M[N + ]
        :param context: El contexto con los registrosa
        :param cacheDatosPropia: La referencia a la cache de datos del core actual
        :param busDatos: Referencia al bus de datos
        :param memoriaDatos: Referencia a la memoria de datos
        :return True si logro leer el bloque, de lo contrario False (Cuando no obtiene el bus de datos)
        '''

        registroDestino = instruccionActual[1]
        registroFuente = instruccionActual[2]
        inmediato = instruccionActual[3]


        #Calcula el bloque al que pertenece la dirección de memoria
        direccion = inmediato + context.getRegister(registroFuente)
        print("dir")
        print(direccion)

        numeroBloque = int(math.floor(direccion / 4))
        indicePalabra = int(math.floor(direccion % 4))


        #todo Bloquear el bus de datos
        busDatos.getBus()

        #Verifica si el dato esta en la cache del nucleo "actual"
        if not cacheDatosPropia.contieneBloque(numeroBloque):
            #Si el dato no esta en la cache entonces trae el bloque a cache
            cacheDatosPropia.cargarBloque(numeroBloque, memoriaDatos)

            for i in range (20):
                self.esperarHilo()

        #En este punto el bloque ya esta cargado en la cache:
        dato = cacheDatosPropia.obtenerDato(numeroBloque,indicePalabra)
        context.setRegister(registroDestino,dato)

        #todo liberar el bus
        busDatos.releaseBus()

    def jal(self,instruccionActual,context,PC):
        '''
        Procesa una instrucción jal
        :param instruccionActual: de la forma op,x1,x2,etiq tal que cambia PC si x1 != x2
        :param context: el contexto del core que contiene los valores en los registros
        :param PC: El valor viejo del PC

        :return El nuevo valor del contador del programa
        '''

        registro = instruccionActual[1]
        inmediato = instruccionActual[3]

        context.setRegister(registro, PC)

        nuevoPC = PC + inmediato

        return nuevoPC

    def jalr(self,instruccionActual,context,PC):
        '''
        Procesa una instrucción jalr
        :param instruccionActual: de la forma op,x1,x2,etiq tal que cambia PC si x1 != x2
        :param context: el contexto del core que contiene los valores en los registros
        :param PC: El valor viejo del PC

        :return El nuevo valor del contador del programa
        '''

        registro1 = instruccionActual[1]
        registro2 = instruccionActual[2]
        inmediato = instruccionActual[3]

        #print("Imprimiendo cosas en JALR")
        #print("registro 1 = %d, registro 2 = %d, inmdiato = %d" % (registro1, registro2, inmediato))

        context.setRegister(registro1, PC)

        nuevoPC = context.getRegister(registro2) + inmediato

        #print("Nuevo PC = %d" % nuevoPC)

        return nuevoPC

    def sw(self, instruccionActual, context,cacheDatosPropia,busDatos,memoriaDatos,otraCacheDatos):
        '''
        Insturccion SW
        :param instruccionActual: forma x1,x2,n donde M[x2+n] = x1
        :param context: la referencia al contexto con los registros
        :param cacheDatosPropia: referencia a la cache de datos del nuecleo "actual"
        :param busDatos: referencia al bus de datos
        :param memoriaDatos: referencia a la memoria de datos
        :return: True si logro escribir, de lo contrario False (Cuando no agarra el bus de datos)
        '''

        #todo bloquear el bus de datos
        busDatos.getBus()

        registroDireccion = instruccionActual[1]
        registroValor = instruccionActual[2]
        inmediato = instruccionActual[3]

        palabra = context.getRegister(registroValor)
        direccion = context.getRegister(registroDireccion) + inmediato

        #Escribe en la memoria de datos
        memoriaDatos.escribirPalabra(direccion,palabra)

        for i in range (5):
            self.esperarHilo()



        #Actualiza el dato si se encuentra en la cache actual
        numeroBloque = int(math.floor(direccion / 4))
        indicePalabra = int(math.floor(direccion % 4))

        #todo Invalida la cache del otro nucleo si tiene el bloque
        #Hace la invalidación cuando tiene el bus
        otraCacheDatos.invalidarBloque(numeroBloque)

        #Actualiza el dato si se encuentra en la cache actual

        if cacheDatosPropia.contieneBloque(numeroBloque):
            #Actualiza el dato
            cacheDatosPropia.escribirPalabra(numeroBloque,indicePalabra,palabra)

        #todo liberar el bus
        busDatos.releaseBus()


    def esperarHilo(self):
        if threading.current_thread().name == "1":
            self.semaforo0.release()
            self.semaforo1.acquire()
        else:
            self.semaforo1.release()
            self.semaforo0.acquire()











