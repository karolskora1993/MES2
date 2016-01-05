from datareader import DataReader
from datawriter import DataWriter
from femgrid import FemGrid
from globaldata import GlobalData
from result import Result

rMin, alfaAir, tempBegin, tempAir, tauMax = DataReader.readGlobalData("global_data")
ne, nh, rMax, elements, nodes = DataReader.readElementsData("elements_data", rMin)

globalData = GlobalData(ne, nh, rMin, rMax, alfaAir, tempBegin, tempAir, tauMax)
globalData.printGlobalData()

femGrid = FemGrid(elements, nodes)
femGrid.setLocalMatrixAndVectors(globalData)
femGrid.printLocalMatrixAndVectors()

femGrid.setGlobalMatrixAndVector(nh)
femGrid.printGlobalMatrixAndVector()

result=Result()
result.solveSystemOfEquation(femGrid.getFg(), femGrid.getKg())
result.printTemperatures()

DataWriter("result.text", result.getTemperatures())


