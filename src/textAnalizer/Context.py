class Context:
    dataIndex = 0 #entero
    instructionIndex = 0 #entero
    registers = [0] * 32 #array de enteros, por el momento hay 32 registros

    def getRegister(self):
        return "algún registro que se pidió"

    def setRegister(self):
        print("He seteado el registro R con el valor #")

    def printContext(self):
        print("Data Index : %d" % (self.dataIndex))
        print("Instruction Index : %d" % (self.instructionIndex));
        for r in range(len(self.registers)):
            print("En el registro %d encontramos el valor %d" % ( r, self.registers[r]))

