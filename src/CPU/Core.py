from src.caches.DataCache import *
from src.caches.InstructionCache import *
from src.CPU.InstructionManager import  *

class Core:
    PC = 0
    IR = 0
    busy = False
    clock = 0
    context = 0
    dataBusReference = 0
    instructionBusReference = 0
    dataMemory = 0
    instructionMemory = 0
    instructionsCache = 0
    dataCache = 0
    instructionManager = 0
    fin = False

    #Inicializamos las referencias de memoria y tambien las caches
    def __init__(self, DataBus, InstructionBus, DataMem, InstructionMem):
        self.dataBusReference = DataBus
        self.instructionBusReference = InstructionBus
        self.dataMemory = DataMem
        self.instructionMemory = InstructionMem
        self.instructionsCache = InstructionCache()
        self.dataCache = DataCache()


    def startContext(self,context):
        '''
        Inicializa la configuración de los registros y reloj del core para empezar a correr el hilillo
        :param context: El contexto del hilillo a correr
        :return: True, para indicar que termino.
        '''

        self.context = context
        self.PC = context.getInstructionIndex()
        self.instructionManager = InstructionManager()

        self.run()

        return True


    def run(self):
        '''
        El trabajo realizado por el core durante el ciclo de reloj actual
        '''


        self.fin = False

        while self.fin == False:

            # Revisar si tengo la instruccion en Cache - Hit/Miss

            #Sumamos 384 para simular que la memoria es continua y empieza justo después de la sección de datos
            #Además, se divide entre 16 para encontrar el número de bloque correspondiente
            posMemoria = self.PC + 384 #Esta es la dirección extra en memoria, vista como 1 solo conjunto
            numeroBloque = (posMemoria) // 16

            #Al número de bloque le sacamos el modulo 4 para saber en qué posición de la caché lo deberíamos de colocar/encontrar
            #Esto porque la caché tiene un espacio máximo de 4 bloques
            posicionCache = numeroBloque % 4

            #Ahora debemos de obtener cual palabra, dentro del bloque, es la que estamos buscando
            palabraBloque = -1
            if numeroBloque * 16 == posMemoria:
                palabraBloque = 0
            elif numeroBloque * 16 + 4 == posMemoria:
                palabraBloque = 1
            elif numeroBloque * 16 + 8 == posMemoria:
                palabraBloque = 2
            else:
                palabraBloque = 3

            #print(self.instructionsCache.memoryMapping)

            #todo inicialiar caches

            #Preguntamos si en la posicion adecuada de la caché está el bloque y si además es válido
            if self.instructionsCache.memoryMapping[posicionCache] == numeroBloque and self.instructionsCache.available[posicionCache] == True:

                #En caso positivo, tomamos el valor y seguimos el proceso
                self.ejecutarInstruccion(palabraBloque, posicionCache)

            else:
                #En caso contrario, debemos de solicitar el bus, traer el bloque correspondiente, meterlo a la caché, liberar el bus y seguir como si ahora
                #sí estuviera en caché

                # pida el bus de instrucciones
                if self.instructionBusReference.isAvailable():

                    #Obtenermos el bus de instrucciones
                    self.instructionBusReference.getBus()

                    # sumar 1 al clock (pedir y lock del bus, o solo pedirlo)
                    self.clock += 1

                    #print("--Debug:")
                    #print("Posicion cache: " + str(posicionCache))
                    #print("PC: " + str(self.PC))
                    #print("Cache de instrucciones: " + str(len(self.instructionsCache.memory)))
                    #print("Memoria de instrucciones: " + str(len(self.instructionMemory.memory)))

                    # Cargar el bloque adecuado a la caché
                    for i in range(16):

                        #print(self.instructionsCache.memory)
                        #Traemos cada uno de los campos que necesitamos desde la memoria principal
                        self.instructionsCache.memory[(posicionCache * 16) + i] = self.instructionMemory.memory[self.PC + i]


                    #todo: implementar cache de datos
                    #Al final colocamos el numero de bloque en el mapeo y lo seteamos a disponible
                    #self.dataCache.memoryMapping[posicionCache] = numeroBloque
                    #self.dataCache.available[posicionCache] = True


                    print(self.instructionsCache.memory)

                    #Sumar los clocks necesarios
                    self.clock += 10

                    #Para este punto, ya tenemos el bloque subido a caché, ahora solo falta hacer que se ejecuten

                    #En cual palabra del bloque está la instruccion? => PC % 4 ?
                    #Sobre cual bloque estamos trabajando => posicionCache
                    #todo: No trarse todo el bloque a fuerza!!!!
                    self.ejecutarInstruccion(palabraBloque, posicionCache, self.instructionsCache.memory[posicionCache*16 : posicionCache*16 + 4])

                    #Libera el bus de instrucciones
                    self.instructionBusReference.releaseBus()

                else:
                    #Esperar un ciclo y volver a solicitar el bus de nuevo
                    print("No se pudo obtener el bus")
                    pass

                #este proceso de buscar instruccion, traerla a cache y luego ejecutarla debería de hacer siempre y cuando no tengamos
                # la instruccion 999, así que en ejecutar instruccion, al final debería de haber una forma de saber cuando salirse, y
                # dentro de este método grande, un while "lo que devuelve la instruccion" no sea falso/verdadero, depende de lo que queramos poner

                # traiga la instrucción
                print("Corriendo en el ciclo de reloj: " + str(self.clock))


    #Método que se utiliza para ejecutar cada instrucción individual
    #Tiene el switch grande con las instrucciones
    def ejecutarInstruccion(self, palabraBloque, bloqueCache, instruccionActual):
        '''

        :param palabraBloque: todo volarse esto
        :param bloqueCache:  todo volarse esto x2
        :param bloqueActual: El vector con 4 palabras que corresponden a la instruccion a ejecutar
        :return:
        '''

        #Meter la instruccion en el IR y hacer PC + 4
        #self.IR = self.instructionMemory.memory[(bloqueCache * 16 ) + (palabraBloque * 4)]
        self.PC += 4


        self.IR = instruccionActual[0]


        #Decodificar la instruccion
        if self.IR == 19:
            self.instructionManager.addi(instruccionActual,self.context)
        if self.IR == 71:
            self.instructionManager.add(instruccionActual,self.context)
        if self.IR == 83:
            self.instructionManager.sub(instruccionActual, self.context)
        if self.IR == 72:
            self.instructionManager.mul(instruccionActual, self.context)
        if self.IR == 56:
            self.instructionManager.div(instruccionActual, self.context)
        if self.IR == 5:
            pass
        if self.IR == 37:
            pass
        if self.IR == 99:
            pass
        if self.IR == 100:
            pass
        if self.IR == 111:
            pass
        if self.IR == 103:
            pass
        if self.IR == 999:
            self.fin = True
            pass

