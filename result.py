import numpy as np
class Result(object):
    def __init__(self):
        self.__temp = []

    def getTemperatures(self):
        return self.__temp

    def solveSystemOfEquation(self, kg, fg):
        a=np.array(kg)

        localF=[]
        for x in fg:
            localF.append(x*(-1))
        b=np.array(localF)

        temperatures = np.linalg.solve(a, b).tolist()
        self.__temp.append(temperatures)
        return temperatures

    def printTemperatures(self):
        print("wektor temperatur w poszczególnych węzłach:")
        print(self.__temp)

