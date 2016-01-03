class GlobalData(object):
    def __init__(self, ne, nh, rMin, rMax, alfaAir, tempBegin, tempAir, tauMax):
        self.__ne=ne
        self.__nh=nh
        self.__rMin=rMin
        self.__rMax=rMax
        self.__alfaAir=alfaAir
        self.__tempBegin=tempBegin
        self.__tempAir=tempAir
        self.__tauMax=tauMax

    def getRMax(self):
        return self.__rMax
    def getAlfaAir(self):
        return self.__alfaAir
    def getTempBegin(self):
        return self.__tempBegin
    def getTempAir(self):
        return self.__tempAir
