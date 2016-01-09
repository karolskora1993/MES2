from result import Result

class FemGrid(object):

    def __init__(self, elements, nodes):
        self.__elements=elements
        self.__nodes=nodes
        self.__kg=[[]]
        self.__fg=[]
        self.__Result=None
        self.__dTau=0
        self.__tauArray=[]

    def getElement(self, i):
        return self.__elements[i]
    def getNode(self, i):
        return self.__nodes[i]

    def getKg(self):
        return self.__kg

    def getFg(self):
        return self.__fg

    def getNodesR(self):
        r=[]
        for node in self.__nodes:
            r.append(node.getR())
        return r

    def setTemperatures(self, temperatures):
        for n in self.__nodes:
            n.setTemp(temperatures.pop(0))

    def getTauArray(self):
        return self.__tauArray

    def setLocalMatrixAndVectors(self, globalData):
        for element in self.__elements:
            element.setLocalMatrixAndVector(globalData, self.__dTau)

    def printLocalMatrixAndVectors(self):
        for element in self.__elements:
            element.printLocalMatrixAndVector()

    def setGlobalMatrixAndVector(self, nh):
        self.__kg=[[0]* nh for i in range(0,nh)]
        self.__fg=[0 for i in range(0,nh)]

        for i in range(0, nh-1):
            ke=self.__elements[i].getKe()
            self.__kg[i][i] += ke[0][0]
            self.__kg[i][i+1] += ke[0][1]
            self.__kg[i+1][i] += ke[1][0]
            self.__kg[i+1][i+1] += ke[1][1]

            fe=self.__elements[i].getFe()
            self.__fg[i] += fe[0]
            self.__fg[i+1] += fe[1]

    def solveSystemOfEquatios(self):
        temperatures = self.__result.solveSystemOfEquation(self.__kg, self.__fg)
        return temperatures

    def simulateProcess(self, globalData):
        self.__dTau = globalData.getTauMax() / globalData.getNTime()
        tau = self.__dTau;

        self.__result=Result()

        while tau <= globalData.getTauMax():
            self.setLocalMatrixAndVectors(globalData)
            self.setGlobalMatrixAndVector(globalData.getNh())
            temperatures = self.solveSystemOfEquatios()
            self.setTemperatures(temperatures)
            self.__tauArray.append(tau)
            tau += self.__dTau

        return self.__result


    def printGlobalMatrixAndVector(self):
        print("Macierz globalna [K]: \n")
        for x in self.__kg:
            print(x)

        print("wektor globalny [F]: \n")

        for x in self.__fg:
            print(x)

