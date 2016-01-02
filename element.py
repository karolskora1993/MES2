class Element(object):
    def __init__(self, firstNode, secondNode, c, ro, k):
        self.__firstNode=firstNode
        self.__secondNode=secondNode
        self.__c=c
        self.__ro=ro
        self.__k=k
        self.__ke=[[]]
        self.__fe=[]
    def getFirstNode(self):
        return self.__firstNode
    def getSecondNode(self):
        return self.__secondNode
    def getKe(self):
        return self.__ke
    def getFe(self):
        return self.__fe
    def setLocalMatrixAndVector(self):
        pass
