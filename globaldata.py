class GlobalData(object):
    def __init__(self, ne, nh, rMin, rMax, alfaAir, tempBegin, tempAir, tauMax, nTime):
        self.__ne=ne
        self.__nh=nh
        self.__rMin=rMin
        self.__rMax=rMax
        self.__alfaAir=alfaAir
        self.__tempBegin=tempBegin
        self.__tempAir=tempAir
        self.__tauMax=tauMax
        self.__nTime=nTime

    def getRMax(self):
        return self.__rMax

    def getRMin(self):
        return self.__rMin

    def getAlfaAir(self):
        return self.__alfaAir

    def getTempBegin(self):
        return self.__tempBegin

    def getTempAir(self):
        return self.__tempAir

    def getTauMax(self):
        return self.__tauMax

    def getNTime(self):
        return self.__nTime

    def getNh(self):
        return self.__nh

    def printGlobalData(self):
        print("dane globalne: \n")
        print("ne= {} rMin={} rMax={}  alfaAir={} tempBegin={} tempAir={} tauMax={} \n".format(self.__ne, self.__rMin, self.__rMax, self.__alfaAir,
                                                                                               self.__tempBegin, self.__tempAir, self.__tauMax))