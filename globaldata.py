class GlobalData(object):
    def __init__(self, ne, nh, rMin, alfaAir, tempBegin, tempAir, tauMax):
        self.__ne=ne
        self.__nh=nh
        self.__rMin=rMin
        self.__alfaAir=alfaAir
        self.__tempBegin=tempBegin
        self.__tempAir=tempAir
        self.__tauMax=tauMax
    def setNumberOfElements(self, ne):
        self.__ne=ne
        self.__nh=ne+1