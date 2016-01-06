from datareader import DataReader
from datawriter import DataWriter
from femgrid import FemGrid
from globaldata import GlobalData
from result import Result
from plotter import Plotter

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
result.solveSystemOfEquation(femGrid.getKg(), femGrid.getFg())
result.printTemperatures()

DataWriter.writeData("result.txt", result.getTemperatures())
Plotter.plot("promień", "tepmeratura", femGrid.getNodesR(), result.getTemperatures())


