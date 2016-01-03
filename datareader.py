import xml.etree.cElementTree as et
from element import Element
from node import Node

class DataReader(object):

    @staticmethod
    def readGlobalData(fileName):
        rmin=0
        alfaAir=0
        tempBegin=0
        tempAir=0
        tauMax=0
        tree=et.parse(fileName+".xml")
        root=tree.getroot()
        for child in root:
            rMin=int(child.find('promień_minimalny_wsadu').text)
            alfaAir=int(child.find('współczynnik_konwekcyjnej_wymiany_ciepła').text)
            tempBegin=int(child.find('temperatura_początkowa').text)
            tempAir=int(child.find('temperatura_otoczenia').text)
            tauMax=int(child.find('czas_procesu').text)
        return rMin, alfaAir, tempBegin, tempAir, tauMax

    @staticmethod
    def readElementsData(fileName, rMin):
        ne=0
        nh=0
        globalR=0
        elements=[]
        nodes=[]
        tree=et.parse(fileName+".xml")
        root=tree.getroot()
        for child in root:
            ne+=1
        nh=ne+1
        for i in range(0,ne-1):
            globalR+=int(child.find('dlugosc').text)
            c=int(child.find('cieplo_wlasciwe').text)
            ro=int(child.find('gestosc_materialu').text)
            k=int(child.find('wspolczynnik_przewodzenia_ciepla').text)
            if i==0:
                nodes.append(Node(0))
                nodes.append(globalR+rMin)
            else :
                nodes.append(globalR)
            elements.append(Element(nodes[i], nodes[i+1], c, ro, k))
        return ne, nh, globalR, elements, nodes

