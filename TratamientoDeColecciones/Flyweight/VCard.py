class VCard():

    name = None
    title = None
    objFW = None

    def __init__(self, n, t, fw):
        self.name=n
        self.title=t
        self.objFW=fw

    def print(self):
        print(self.name)
        print(self.title)
        print(self.objFW.getCompany())
        print(self.objFW.getAddress() + " , " + self.objFW.getCity() + " , " + self.objFW.getState() + " , " + self.objFW.getZip())

