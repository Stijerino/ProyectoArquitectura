from src.parentClases.Cache import *

class DataCache(Cache):

    memory = []
    memoryMapping = []
    available = []
    bloques = 0

    def __init__(self):
        self.memory = [0] * 16 #Aquí entran 4 bloques, cada 4 campos hay una palabra
        self.memoryMapping = [0] * 4 #Cada bloque se representa en este vector
        self.available = [False] * 4 #Acá encontramos si bloque está o no inválido
        self.bloques = 4 #La cantidad de bloques que tiene la caches

    def contieneBloque(self,numeroBloque):
        '''
        Indica si el bloque se encuentra o no en la cache de datos.
        Utiliza el algoritmo de mapeo directo, en el cual realiza un modulo entre el tamaño de la cache para encontrar
        la posición del bloque, con un vector de tags que indique cual es el número de bloque que se encuentra en dicha
        posición de memoria
        :param numeroBloque: El numero de bloque a comprobar si esta o no en la cache
        :return: True si el bloque esta en la cache de datos, de lo contario False
        '''

        encontrado = False

        posicion = numeroBloque % self.bloques

        if self.available[posicion] == True and self.memoryMapping[posicion] == numeroBloque:
            encontrado = True

        return encontrado

    def cargarBloque(self,numeroBloque,memoriaDatos):
        '''
        Función intermediaria. Solicita a la memoria de datos el bloque
        :param numeroBloque: El bloque a traer
        :param memoriaDatos: Referencia a la memoria de datos
        :return:
        '''
        bloque = memoriaDatos.traerBloque(numeroBloque)
        posicion = numeroBloque % self.bloques

        #Mete las palabras en el bloque de la cache, una por una
        for p in range(0,4):
            self.memory[posicion * 4 + p] = bloque[p]

        #Indica el tag y la validez del bloque
        self.memoryMapping[posicion] = numeroBloque
        self.available[posicion] = True

        print(self.memory)

    def invalidarBloque(self,numeroBloque):
        '''
        Invalida el bloque si se encuentra en la cache.
        Utiliza el algoritmo de Mapeo Directo para encontrar la posición del bloque en la cache. Para invalidarlo
        comprueba que en esa posición del bloque en verdad se encuentre el bloque con ese número y no otro.
        :param numeroBloque: El bloque a invalidar
        '''

        posicion = numeroBloque % self.bloques

        if self.memoryMapping[posicion] == numeroBloque:
            self.available[posicion] = False



    def escribirPalabra(self,numeroBloque,indicePalabra,palabra):
        '''
        Actualiza el valor de  una palabra que se encuentra en un bloque valido

        Utiliza el algoritmo de mapeo directo, en el cual realiza un modulo entre el tamaño de la cache para encontrar
        la posición del bloque, con un vector de tags que indique cual es el número de bloque que se encuentra en dicha
        posición de memoria.

        :param numeroBloque: El numero de bloque a comprobar si esta o no en la cache
        :param indicePalabra: El indice del dato a traer
        :return: [] si el bloque esta invalido o no esta en la cache, de lo contrario la palabra
        '''

        posicion = numeroBloque % self.bloques

        if self.available[posicion] == True and self.memoryMapping[posicion] == numeroBloque:
            self.memory[posicion * 4 + indicePalabra] = palabra


    def obtenerDato(self,numeroBloque,indicePalabra):
        '''
        Devuelve una palabra que se encuentra en un bloque valido

        Utiliza el algoritmo de mapeo directo, en el cual realiza un modulo entre el tamaño de la cache para encontrar
        la posición del bloque, con un vector de tags que indique cual es el número de bloque que se encuentra en dicha
        posición de memoria.

        :param numeroBloque: El numero de bloque a comprobar si esta o no en la cache
        :param indicePalabra: El indice del dato a traer
        :return: [] si el bloque esta invalido o no esta en la cache, de lo contrario la palabra
        '''

        palabra = []

        posicion = numeroBloque % self.bloques



        if self.available[posicion] == True and self.memoryMapping[posicion] == numeroBloque:
            palabra = self.memory[posicion * 4 + indicePalabra]


        return palabra



