from src.parentClases.Cache import *


class InstructionCache(Cache):

    def __init__(self):
        memory = [0] * 64 #Almacena 4 bloques de 16 bytes cada uno = 64 bytes
        memoryMapping = [0] * 4 #Representa que bloque esta en cache
        available = [False] * 4 #Indica si el bloque es válido o inválido