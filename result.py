import numpy as np
class Result(object):
    def __init__(self):
        self.__temp=[]

    def getTemperatures(self):
        return self.__temp

    def solveSystemOfEquation(self, ke, fe):
        a=np.array(ke)

        localFe=[]
        for x in fe:
            localFe.append(x*(-1))
        b=np.array(localFe)

        self.__temp=np.linalg.solve(a, b)

    def printTemperatures(self):
        print("wektor temperatur w poszczególnych węzłach:")
        for x in self.__temp:
            print(x)
