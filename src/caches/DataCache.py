from src.parentClases.Cache import *

class DataCache(Cache):

    def __init__(self):
        memory = [0] * 16 #Aquí entran 4 bloques, cada 4 campos hay una palabra
        memoryMapping = [0] * 4 #Cada bloque se representa en este vector
        available = [False] * 4 #Acá encontramos si bloque está o no inválido
