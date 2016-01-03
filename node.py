class Node(object):
    def __init__(self, r):
        self.__r=r
        self.__temp=None
    def getR(self):
        return self.__r
    def setTemp(self, temp):
        self.__temp=temp
