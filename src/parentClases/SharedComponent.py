class SharedComponent:
    memory = []
    blockSize = 4 #Creo que son 4 bytes

    def getBus(self):

        if self.reservedBus == False:
            # todo: sincronización para bloquear el bus
            self.reservedBus = True
        else:

            pass

    def releaseBus(self):
        self.reservedBus = False
        # todo: sincronización para  liberar el bus

    def isAvailable(self):
        return (not self.reservedBus)
