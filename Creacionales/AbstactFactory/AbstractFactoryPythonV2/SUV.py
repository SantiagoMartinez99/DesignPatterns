# SUV hierarchy

import abc
class SUV:
    __metaclass__ = abc.ABCMeta

    def __init__(self):
        raise NotImplementedError()

    def getSUVName(self):
        raise NotImplementedError()

    def getSUVFeatures(self):
        raise NotImplementedError()
# End of interface (Class as interface)

class LuxurySUV(SUV):
    def __init__(self, sName):
        self.__name = sName
    def getSUVName(self):
        return self.__name;
    def getSUVFeatures(self):
        return "Luxury SUV Features ";
#End of class

class NonLuxurySUV(SUV):
    def __init__(self, sName):
        self.__name = sName
    def getSUVName(self):
        return self.__name
    def getSUVFeatures(self):
        return "Non-Luxury SUV Features "
#End of class
