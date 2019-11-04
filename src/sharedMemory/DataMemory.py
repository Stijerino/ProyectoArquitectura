from src.parentClases.SharedComponent import *

class DataMemory (SharedComponent):

    memory = [i for i in range(0, 380)]
    blockSize = 4
    bus = True