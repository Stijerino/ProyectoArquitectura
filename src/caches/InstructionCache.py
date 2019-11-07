from src.parentClases.Cache import *


class InstructionCache(Cache):
    memory = []
    memoryMapping = []
    available = []


    def __init__(self):
        self.memory = [0] * 64 #Almacena 4 bloques de 16 bytes cada uno = 64 bytes
        self.memoryMapping = [-1] * 4 #Representa que bloque esta en cache.
        self.available = [False] * 4 #Indica si el bloque es válido o inválido