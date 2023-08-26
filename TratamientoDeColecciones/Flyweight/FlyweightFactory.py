from FlyweightIntr import *

class FlyweightFactory(object):

    __instance = None
    lstFlyweight = {}
    
    def getFlyweight(self, divisionName):
        if self.lstFlyweight.get(divisionName) is None:
            fw = Flyweight(divisionName)
            self.lstFlyweight[divisionName] = fw
            return fw
        else:
            return self.lstFlyweight.get(divisionName)

    #Garantiza una ejemplificacion unica de la clase
    def __new__(cls):
        if FlyweightFactory.__instance is None:
            FlyweightFactory.__instance = object.__new__(cls)
        return FlyweightFactory.__instance

class Flyweight(FlyweightIntr):

    company = None
    address = None
    city = None
    state = None
    zipStr = None

    def setValues(self, cmp, addr, cty, st, zp):
        self.company=cmp
        self.address=addr
        self.city=cty
        self.state=st
        self.zipStr=zp

    def __init__(self, division):
        if(division == "North"):
            self.setValues("CMP Company", "Cl 170 Cra 42", "Bogotá D.C.", "Toberín", "10000")
        if(division == "South"):
            self.setValues("CMP Company", "Cra 73 Sur Cl 64", "Bogotá D.C.", "Bosa", "20000")
        if(division == "East"):
            self.setValues("CMP Company", "Cl 3 Cra 1", "Bogotá D.C.", "Rafael Uribe Uribe", "30000")
        if(division == "West"):
            self.setValues("CMP Company", "Cra 80 Cl 26", "Bogotá D.C.", "Fontibón", "40000")

    def getCompany(self):
        return self.company

    def getAddress(self):
        return self.address
    
    def getCity(self):
        return self.city
    
    def getState(self):
        return self.state
    
    def getZip(self):
        return self.zipStr
