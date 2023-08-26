# CAR hierarchy

import abc

class Car:
    __metaclass__ = abc.ABCMeta

    def __init__(self):
        raise NotImplementedError()

    def getCarName(self):
        raise NotImplementedError()

    def getCarFeatures(self):
        raise NotImplementedError()


# End of interface (Class as interface)

class LuxuryCar(Car):
    def __init__(self, cName):
        self.__name = cName
    def getCarName(self):
        return self.__name
    def getCarFeatures(self):
        return "Luxury Car Features "
#End of class

class NonLuxuryCar(Car):
    def __init__(self, cName):
        self.__name = cName
    def getCarName(self):
        return self.__name
    def getCarFeatures(self):
        return "Non-Luxury Car Features "
#End of class




