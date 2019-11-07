class Context:
    dataIndex = 0 #entero
    instructionIndex = 0  #entero
    registers = [0] * 32  #array de enteros, por el momento hay 32 registros

    def setInstructionIndex(self,index):
        self.instructionIndex = index

    def getInstructionIndex(self):
        return self.instructionIndex

    def getRegister(self,register):
        return int(self.registers[register])

    def setRegister(self, register, value):
        self.registers[register] = value

    def printContext(self):
        print("Data Index : %d" % (self.dataIndex))
        print("Instruction Index : %d" % (self.instructionIndex));
        for r in range(len(self.registers)):
            print("En el registro %d encontramos el valor %d" % ( r, self.registers[r]))

