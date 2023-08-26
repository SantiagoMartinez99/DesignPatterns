# Main program
# This example was elaborated from Partha Kuchana's example of his book "Software Architecture Design Patterns in Java" by Daniel Hernández Olis
# and adapted by Henry Alberto Diosa with pedagogical purposes.

from tkinter import ttk
from tkinter import *
from ButtonHandler import *
import SUV
import CAR
import Motorcycle

class AutoSearchUI(Toplevel):
    SEARCH = "Show"
    EXIT = "Exit"
    CAR = "Car"
    SUV = "SUV"
    MOTORCYCLE="Motorcycle"

    def __init__(self, master):
        Toplevel.__init__(self, master)

        self.__cmbVehicleCategory = ttk.Combobox(self, state="readonly")
        self.__cmbVehicleCategory["values"] = [VehicleFactory.LUXURY_VEHICLE,
                                               VehicleFactory.NON_LUXURY_VEHICLE]
        self.__cmbVehicleCategory.current(0)

        self.__cmbVehicleType = ttk.Combobox(self, state="readonly")
        self.__cmbVehicleType["values"] = [self.CAR, self.SUV, self.MOTORCYCLE]
        self.__cmbVehicleType.current(0)

        self.__lblVehicleCategory = Label(self, text="Vehicle Category:")
        self.__lblVehicleType = Label(self, text="Vehicle Type:")
        self.__lblCarName = Label(self, text="Search Result:")
        self.__lblCarNameValue = Label(self, text=" Please click on Show button")

        self.__openButton = Button(self, text=self.SEARCH)
        self.__exitButton = Button(self, text=self.EXIT)
        # ******************************************************************************************************#
        self.__lblVehicleCategory.grid(row=1, column=1, padx=10, pady=10)
        self.__cmbVehicleCategory.grid(row=1, column=2, padx=10, pady=10)
        self.__lblVehicleType.grid(row=2, column=1, padx=10, pady=10)
        self.__cmbVehicleType.grid(row=2, column=2, padx=10, pady=10)
        self.__lblCarName.grid(row=3, column=1, padx=10, pady=10)
        self.__lblCarNameValue.grid(row=3, column=2, padx=10, pady=10)
        self.__openButton.grid(row=4, column=1, padx=10, pady=10)
        self.__exitButton.grid(row=4, column=2, padx=10, pady=10)

    def getExitButton(self):
        return self.__exitButton

    def getOpenButton(self):
        return self.__openButton

    def getCmbVehicleCategory(self):
        return self.__cmbVehicleCategory

    def getCmbVehicleType(self):
        return self.__cmbVehicleType

    def getLblCarNameValue(self):
        return self.__lblCarNameValue

    def setText(self, s):
        self.__lblCarNameValue.config(text=s)

# End of class
# Main method
def main():
    root = Tk()
    root.withdraw()
    root.title("Abstract Factory Example")
    app = ButtonHandler(root)
    root.mainloop()

# Executing the main method
if __name__ == "__main__":
    main()
