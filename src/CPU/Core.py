class Core:
    PC = 0
    IR = 0
    busy = False
    Clock = 0
    dataBusReference = 0
    instructionBusReference = 0
    'Estos últimos 2 tienen que ser referencias a los buses que se crean al inicio'


    def __init__(self,Context, DataBus, InstructionBus):
        #Cargar el Context al core
        self.dataBusReference = DataBus
        self.instructionBusReference = InstructionBus