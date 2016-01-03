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

    def setLocalMatrixAndVector(self, tauMax, globalData):
        a = self.__k / (self.__c * self.__ro)
        dR = self.__secondNode.getR()-self.__firstNode.getR()
        dTau = (dR**2)/(0.5*a);
        nTime=(tauMax/dTau) + 1;
        dTau = tauMax / nTime;
        alfa=0
        if globalData.getRMax()==self.__secondNode.getR():
            alfa=globalData.getAlfaAir()
        w=[1,1]
        e=[-0.5773502692,0.5773502692]
        n=[[0.5*(1-e[0]),0.5*(1+e[1])],[0.5*(1-e[0]),0.5*(1+e[1])]]
        rp=[n[0][0]*self.__firstNode.getR() + n[0][1]*self.__secondNode.getR(),
            n[1][0]*self.__firstNode.getR() + n[1][1]*self.__secondNode.getR()]

        self.__ke[0][0]=self.__ke*(rp[0]*w[0]+rp[1]*w[1])/dR + self.__c*self.__ro*dR*(rp[0]*w[0]*n[0][0]**2 +rp[1]*w[1]*n[1][0]**2 )/dTau
        self.__ke[0][1]=self.__ke*(rp[0]*w[0]+rp[1]*w[1])/dR + self.__c*self.__ro*dR*(n[0][0]*n[1][0]*rp[0]*w[0] +n[1][0]*n[1][1]*rp[1]*w[1] )/dTau
        self.__ke[1][0]=self.__ke*(rp[0]*w[0]+rp[1]*w[1])/dR + self.__c*self.__ro*dR*(n[0][0]*n[1][0]*rp[0]*w[0] +n[1][0]*n[1][1]*rp[1]*w[1] )/dTau
        self.__ke[1][1]=self.__ke*(rp[0]*w[0]+rp[1]*w[1])/dR + self.__c*self.__ro*dR*(rp[0]*w[0]*n[0][1]**2 +rp[1]*w[1]*n[1][1]**2 )/dTau +2*alfa*globalData.getRMax()

        self.__fe[0]=-self.__c*self.__ro*dR*(  ( (n[0][0]*globalData.getTempBegin()+n[0][1]*globalData.getTempBegin() )*n[0][0]*rp[0]*w[0])+(n[1][0]*globalData.getTempBegin()+n[1][1]*globalData.getTempBegin() )*n[1][0]*rp[1]*w[1])/dTau
        self.__fe[0]=-self.__c*self.__ro*dR*(  ( (n[0][0]*globalData.getTempBegin()+n[0][1]*globalData.getTempBegin() )*n[0][0]*rp[0]*w[0])+(n[1][0]*globalData.getTempBegin()+n[1][1]*globalData.getTempBegin() )*n[1][0]*rp[1]*w[1])/dTau -2*alfa*globalData.getRMax()*globalData.getTempAir()
