class FemGrid(object):

    def __init__(self, elements, nodes):
        self.__elements=elements
        self.__nodes=nodes
        self.__kg=[[]]
        self.__fg=[]

    def getElement(self, i):
        return self.__elements[i]
    def getNode(self, i):
        return self.__nodes[i]

    def setLocalMatrixAndVectors(self, globalData):
        for element in self.__elements:
            element.setLocalMatrixAndVector(globalData)

    def printLocalMatrixAndVectors(self):
        for element in self.__elements:
            element.printLocalMatrixAndVector()

    def setGlobalMatrixAndVector(self, nh):
        self.__kg=[[0]*nh]*nh
        self.__fg=[0]*nh
        for i in range(0, nh-1):
            ke=self.__elements[i].getKe()
            self.__kg[i][i]+=ke[0][0]
            self.__kg[i][i+1]+=ke[0][1]
            self.__kg[i+1][i]+=ke[1][0]
            self.__kg[i+1][i+1]+=ke[1][1]

            fe=self.__elements[i].getFe()
            self.__fg[i]+=fe[0]
            self.__fg[i+1]+=fe[1]

    def printGlobalMatrixAndVector(self):
        print("Macierz globalna [K]: \n")
        for x in self.__kg:
            print(x)

        print("wektor globalny [F]: \n")

        for x in self.__fg:
            print(x)

