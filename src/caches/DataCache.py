from src.parentClases.Cache import *

class DataCache(Cache):

    memory = []
    memoryMapping = []
    available = []

    def __init__(self):
        self.memory = [0] * 16 #Aquí entran 4 bloques, cada 4 campos hay una palabra
        self.memoryMapping = [0] * 4 #Cada bloque se representa en este vector
        self.available = [False] * 4 #Acá encontramos si bloque está o no inválido
