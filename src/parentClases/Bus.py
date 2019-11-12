'''
Esta clase sirve tanto para representar el bus de datos como el bus de instrucciones.
'''


class Bus:
    available = True

    def __init__(self):
        self.available = True
        pass

    def getBus(self):
        self.available = False

    def releaseBus(self):
        self.available = True


    def isAvailable(self):
        return self.available
