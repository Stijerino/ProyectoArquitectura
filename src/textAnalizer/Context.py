class Context:
    dataIndex = 0  # entero
    instructionIndex = 0  # entero
    registers = [0 for i in range(0, 32)]  # array de enteros, por el momento hay 32 registros
    core = -1
    id = -1

    def __init__(self):
        self.dataIndex = 0  # entero
        self.instructionIndex = 0  # entero
        self.registers = [0 for i in range(0, 32)]  # array de enteros, por el momento hay 32 registros
        self.core = -1
        self.id = -1


    def setCore(self,core):
        self.core = core


    def setInstructionIndex(self,index):
        self.instructionIndex = index

    def getInstructionIndex(self):
        return self.instructionIndex

    def getRegister(self,register):
        return int(self.registers[register])

    def setRegister(self, register, value):
        self.registers[register] = value

    def printContext(self):


        for r in range(len(self.registers)):
            print("En el registro %d encontramos el valor %d" % ( r, self.registers[r]))


        print("-----------------------------------------------------------------ID: " + str(self.id))
        print("Data Index : %d" % (self.dataIndex))
        print("Instruction Index : %d" % (self.instructionIndex))




        print("Ejecutado por el core: " + str(self.core))

    def setId(self,id):
        self.id = id

