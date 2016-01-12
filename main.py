from datareader import DataReader
from datawriter import DataWriter
from femgrid import FemGrid
from globaldata import GlobalData
from result import Result
from plotter import Plotter

rMin, alfaAir, tempBegin, tempAir, tauMax, nTime = DataReader.readGlobalData("global_data")
ne, nh, rMax, elements, nodes = DataReader.readElementsData("elements_data", rMin, tempBegin)

globalData = GlobalData(ne, nh, rMin, rMax, alfaAir, tempBegin, tempAir, tauMax, nTime)
globalData.printGlobalData()

femGrid = FemGrid(elements, nodes)
result = femGrid.simulateProcess(globalData)

result.printTemperatures()

DataWriter.writeData("result.txt", result.getTemperatures())
Plotter.plot("czas", "temperatura", femGrid.getTauArray(), result.getTemperatures())


