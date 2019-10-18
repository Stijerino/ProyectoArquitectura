class Bus:
    available = True

    def __init__(self):
        pass

    def getBus(self):
        self.available = False

    def releaseBus(self):
        self.available = True

    def isAvailable(self):
        return self.available
