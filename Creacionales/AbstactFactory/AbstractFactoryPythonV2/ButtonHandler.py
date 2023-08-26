# This example was elaborated from Partha Kuchana's example of his book "Software Architecture Design Patterns in Java" by Daniel Hernández Olis and adapted by Henry
# Alberto Diosa with padagogical purposes.

from tkinter import *
from tkinter import ttk
from AbstractFactory import *
from AutoSearchUI import *

class ButtonHandler:
    def __init__(self,root):
        self.__root=root
        self.__frame=AutoSearchUI(root)
        self.__frame.getExitButton().config(command=self.eventExitButton)
        self.__frame.getOpenButton().config(command=self.eventOpenButton)
    def eventExitButton(self):
        self.__frame.destroy()
        self.__root.destroy()
    def eventOpenButton(self):
        vhCategory = self.__frame.getCmbVehicleCategory().get()
        vhType = self.__frame.getCmbVehicleType().get()
        vf = VehicleFactory.getVehicleFactory(vhCategory)
        if vhType == self.__frame.CAR:
            c = vf.getCar()
            searchResult = "Name: " + c.getCarName() + " Features: " + c.getCarFeatures()
        if vhType == self.__frame.SUV:
            s = vf.getSUV()
            searchResult = "Name: " + s.getSUVName() + " Features: " + s.getSUVFeatures()
        if vhType == self.__frame.MOTORCYCLE:
            s = vf.getMotorcycle()
            searchResult = "Name: " + s.getMotorcycleName() + " Features: " + s.getMotorcycleFeatures()
        self.__frame.setText(searchResult)
#End of class