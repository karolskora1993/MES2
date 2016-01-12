class Element(object):
    def __init__(self, firstNode, secondNode, c, ro, k):
        self.__firstNode=firstNode
        self.__secondNode=secondNode
        self.__c=c
        self.__ro=ro
        self.__k=k
        self.__ke=[[0,0], [0,0]]
        self.__fe=[0, 0]


    def getFirstNode(self):
        return self.__firstNode

    def getSecondNode(self):
        return self.__secondNode

    def getKe(self):
        return self.__ke
    def getFe(self):
        return self.__fe

    def setLocalMatrixAndVector(self, globalData, dTau):
        self.__ke = [[0,0], [0,0]]
        self.__fe = [0, 0]

        dR = self.__secondNode.getR()-self.__firstNode.getR()

        w=[1, 1]

        for i in range(0,2):
            rp = globalData.getN(i,0) * self.__firstNode.getR() + globalData.getN(i,1) * self.__secondNode.getR()
            tauP = globalData.getN(i,0) * self.__firstNode.getTemp() + globalData.getN(i,1) * self.__secondNode.getTemp()

            self.__ke[0][0] += self.__k * rp * w[i] / dR + self.__c * self.__ro * dR * rp * w[i] * globalData.getN(i,0)**2 / dTau
            self.__ke[0][1] += (-1)*self.__k * rp * w[i] / dR + self.__c * self.__ro * dR * rp * w[i] * globalData.getN(i,0) * globalData.getN(i,1) / dTau
            self.__ke[1][0] += (-1)*self.__k * rp * w[i] / dR + self.__c * self.__ro * dR * rp * w[i] * globalData.getN(i,0) * globalData.getN(i,1) / dTau
            self.__ke[1][1] += self.__k * rp * w[i] / dR + self.__c * self.__ro * dR * rp * w[i] * globalData.getN(i,1)**2 / dTau

            self.__fe[0] += (-1)*self.__c * self.__ro * dR * tauP * rp * w[i] * globalData.getN(i,0) / dTau
            self.__fe[1] += (-1)*self.__c * self.__ro * dR * tauP * rp * w[i] * globalData.getN(i,1) / dTau

        if globalData.getRMax() == self.__secondNode.getR():
            self.__ke[1][1] += 2 * globalData.getAlfaAir() * globalData.getRMax()
            self.__fe[1] -= 2 * globalData.getAlfaAir() * globalData.getRMax() * globalData.getTempAir()

        if globalData.getRMin() > 0:
            if globalData.getRMin() == self.__firstNode.getR():
                self.__ke[0][0] += 2 * globalData.getAlfaAir() * globalData.getRMin()
                self.__fe[0] -= 2 * globalData.getAlfaAir() * globalData.getRMin() * globalData.getTempAir()

    def printLocalMatrixAndVector(self):
        print("\n element")
        for x in self.__ke:
            print(x)

        print()
        for x in self.__fe:
            print(x)
