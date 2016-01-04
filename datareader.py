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
            rMin=float(child.find('promień_minimalny_wsadu').text)
            alfaAir=float(child.find('współczynnik_konwekcyjnej_wymiany_ciepła').text)
            tempBegin=float(child.find('temperatura_początkowa').text)
            tempAir=float(child.find('temperatura_otoczenia').text)
            tauMax=float(child.find('czas_procesu').text)
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
        print("Wczytuje dane elementow z pliku:\n")
        for i in range(0,ne):
            print("Element numer {}: \n".format(i))
            globalR += float(child.find('dlugosc').text)
            print("dlugosc: {} \n".format(globalR))

            c=float(child.find('cieplo_wlasciwe').text)
            print("cieplo wlasciwe: {} \n".format(c))

            ro=float(child.find('gestosc_materialu').text)
            print("gestosc materialu: {} \n".format(ro))

            k=float(child.find('wspolczynnik_przewodzenia_ciepla').text)
            print("wspolczynnik przewodzenia ciepla: {} \n".format(k))

            if i==0:
                node1=Node(0)
                node2=Node(globalR+rMin)
                nodes.append(node1)
                nodes.append(node2)
            else :
                node=Node(globalR+rMin)
                nodes.append(node)

            element=Element(nodes[i], nodes[i+1], c, ro, k)
            elements.append(element)

        return ne, nh, globalR, elements, nodes

