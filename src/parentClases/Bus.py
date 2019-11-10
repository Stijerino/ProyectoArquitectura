'''
Esta clase sirve tanto para representar el bus de datos como el bus de instrucciones.
Cuenta con un semaforo mutex como mecanismo de sincronización
'''

import threading

class Bus:
    available = True
    semaphore = 0

    def __init__(self):
        self.available = True
        self.semaphore = threading.Semaphore()
        pass

    def getBus(self):
        self.available = False
        self.semaphore.acquire()

    def releaseBus(self):
        self.available = True
        self.semaphore.release()


    def isAvailable(self):
        return self.available
