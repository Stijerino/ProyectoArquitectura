class Core:
    PC = 0
    IR = 0
    busy = False
    clock = 0
    context = 0
    dataBusReference = 0
    instructionBusReference = 0
    'Estos últimos 2 tienen que ser referencias a los buses que se crean al inicio'


    def __init__(self,DataBus, InstructionBus):
        self.dataBusReference = DataBus
        self.instructionBusReference = InstructionBus

    def startContext(self,context):
        '''
        Inicializa la configuración de los registros y reloj del core para empezar a correr el hilillo
        :param context: El contexto del hilillo a correr
        :return: True, para indicar que termino.
        '''

        PC = context.getInstructionIndex()

        self.run()

        return True


    def run(self):
        '''
        El trabajo realizado por el core durante el ciclo de reloj actual
        '''

        print("Corriendo en el ciclo de reloj: " + str(self.clock))
