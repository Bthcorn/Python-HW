class LinearEquation():
    def __init__(self, a=0, b=0, c=0, d=0, e=0, f=0):
        self.__a = a
        self.__b = b
        self.__c = c
        self.__d = d
        self.__e = e
        self.__f = f

    def getA(self):
        return self.__a
    
    def getB(self):
        return self.__b
    
    def getC(self):
        return self.__c
    
    def getD(self):
        return self.__d
    
    def getE(self):
        return self.__e
    
    def getF(self):
        return self.__f
    
    def isSolveable(self):
        if (self.__a*self.__d) - (self.__b*self.__c) != 0:
            return True
        else:
            return False
        
    def getX(self):
        divider = (self.__a*self.__d) - (self.__b*self.__c)
        if divider != 0:
            x = ((self.__e*self.__d) - (self.__b*self.__f)) / divider
            return x
            
    def getY(self):
        divider = (self.__a*self.__d) - (self.__b*self.__c)
        if divider != 0:
            y = ((self.__a*self.__f) - (self.__e*self.__c)) / divider
        return y
    
l = LinearEquation(2, 7, 2, -3, 0, 6)
l.isSolveable()
l.getX()
l.getY()
l.getA()
l.getB()
