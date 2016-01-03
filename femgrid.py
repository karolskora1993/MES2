class FemGrid(object):
    def __init__(self, elements, nodes):
        self.__elements=elements
        self.__nodes=nodes
    def getElement(self, i):
        return self.__elements[i]
    def getNode(self, i):
        return self.__nodes[i]