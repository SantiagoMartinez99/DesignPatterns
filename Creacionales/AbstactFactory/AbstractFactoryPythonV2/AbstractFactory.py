# VehicleFactory hierarchy

import abc
from SUV import *
from CAR import *
from Motorcycle import *

class VehicleFactory:
    __metaclass__ = abc.ABCMeta
    LUXURY_VEHICLE="Luxury"
    NON_LUXURY_VEHICLE="Non-Luxury"
    def __init__(self):
        raise NotImplementedError()
    def getCar(self):
        raise NotImplementedError()
    def getSUV(self):
        raise NotImplementedError()
    def getMotorcycle(self):
        raise NotImplementedError()
    def getVehicleFactory(tipo):
        if tipo==VehicleFactory.LUXURY_VEHICLE:
            return LuxuryVehicleFactory()
        if tipo==VehicleFactory.NON_LUXURY_VEHICLE:
            return NonLuxuryVehicleFactory()
        return LuxuryVehicleFactory()
    getVehicleFactory = staticmethod(getVehicleFactory)
#End of class

class LuxuryVehicleFactory(VehicleFactory):
    def __init__(self):
        pass
    def getCar(self):
        return LuxuryCar("Luxury-Car")
    def getSUV(self):
        return LuxurySUV("Luxury-SUV")
    def getMotorcycle(self):
        return LuxuryMotorcycle("Luxury-Motorcycle")
#End of class

class NonLuxuryVehicleFactory(VehicleFactory):
    def __init__(self):
        pass
    def getCar(self):
        return NonLuxuryCar("Non Luxury-Car")
    def getSUV(self):
        return NonLuxurySUV("Non Luxury-SUV")
    def getMotorcycle(self):
        return NonLuxuryMotorcycle("Non Luxury-Motorcycle")
#End of class

