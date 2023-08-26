from FlyweightFactory import *
from VCard import *


class FlyweightTest():
   def initialize(self):
        v = []
        v.append("Antonia Ruiz,Ingeniero,North")
        v.append("Pedro Park,Contador,South")
        v.append("Jorge G.,Operario,North")
        v.append("Luis Q.,Secretario,East")
        v.append("Carlos G.,Secretario,East")
        v.append("Pablo L.,Contador,East")
        v.append("Marcos P.,Ingeniero,West")
        v.append("Ana Luisa P.,Secretaria,West")
        v.append("Irene Liz,Ingeniera,West")
        v.append("Mariana U.,Abogada,South")
        v.append("Julia P.,Ingeniera,North")
        v.append("Carla M.,Gerente,North")
        return v

def main():
    ft = FlyweightTest()
    empList = ft.initialize()
    factory = FlyweightFactory()
    for i in empList:
        name = i.split(",")[0]
        title = i.split(",")[1]
        division = i.split(",")[2]
        flyweight = factory.getFlyweight(division)
        card = VCard(name, title, flyweight)
        print("---------------------")
        card.print()

if __name__=="__main__":
    main()
            
            
