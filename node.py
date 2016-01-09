class Node(object):

    def __init__(self, r, tempBegin):
        self.__r = r
        self.__temp = tempBegin

    def getR(self):
        return self.__r

    def setTemp(self, temp):
        print("poprzednia wartosc temp:{} ".format(self.__temp))
        self.__temp = temp
        print("nowa wartosc temp:{} ".format(self.__temp))

    def getTemp(self):
        return self.__temp
