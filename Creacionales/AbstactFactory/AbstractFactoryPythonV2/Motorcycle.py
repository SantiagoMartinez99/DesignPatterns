# Motorcycle hierarchy

import abc

class Motorcycle:
    __metaclass__ = abc.ABCMeta

    def __init__(self):
        raise NotImplementedError()

    def getMotorcycleName(self):
        raise NotImplementedError()

    def getMotorcycleFeatures(self):
        raise NotImplementedError()


# End of interface (Class as interface)

class LuxuryMotorcycle(Motorcycle):
    def __init__(self, cName):
        self.__name = mName
    def getMotorcycleName(self):
        return self.__name
    def getMotorcycleFeatures(self):
        return "Luxury Motorcycle Features "
#End of class

class NonLuxuryMotorcycle(Motorcycle):
    def __init__(self, cName):
        self.__name = mName
    def getMotorcycleName(self):
        return self.__name
    def getMotorcycleFeatures(self):
        return "Non-Luxury Motorcycle Features "
#End of class

