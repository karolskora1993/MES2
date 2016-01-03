from datareader import DataReader
from femgrid import FemGrid
from globaldata import GlobalData

rMin, alfaAir, tempBegin, tempAir, tauMax = DataReader.readGlobalData("global_data")
ne, nh, rMax, elements, nodes = DataReader.readElementsData("elements_data", rMin)
globalData = GlobalData(ne, nh, rMin,rMax, alfaAir, tempBegin, tempAir, tauMax)
femGrid = FemGrid(elements, nodes)