'''
Esta clase sirve tanto para representar el bus de datos como el bus de instrucciones.
'''
import threading

class Bus:
    available = True
    semaforo = 0

    def __init__(self):
        self.available = True
        self.semaforo = threading.Semaphore()


    def getBus(self):
        self.semaforo.acquire()
        obtenido = False
        if(self.available):
            self.available = False
            obtenido = True
        self.semaforo.release()
        return obtenido

    def releaseBus(self):
        self.available = True





