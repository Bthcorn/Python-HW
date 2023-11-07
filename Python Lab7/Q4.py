class QuadraticEquation:
    def __init__(self, a=1, b=4, c=2):
        self.a = a
        self.b = b
        self.c = c
    
    def geta(self):
        return self.a
    
    def getb(self):
        return self.b
    
    def getc(self):
        return self.c
    
    def getDiscriminant(self):
        return (self.b**2 - 4*self.a*self.c)**0.5
    
    def getRoot1(self):
        if  self.b**2 - 4*self.a*self.c >= 0:
            return (-1*self.b + (self.b**2 - 4*self.a*self.c)**0.5) / 2*self.a
        else:
            return 0

    def getRoot2(self):
        if self.b**2 - 4*self.a*self.c >= 0:
            return (-1*self.b - (self.b**2 - 4*self.a*self.c)**0.5) / 2*self.a
        else:
            return 0
            
q = QuadraticEquation(1,4,4)
q.geta()
q.getb()
q.getc()

print(q.getDiscriminant())
print(q.getRoot1())
print(q.getRoot2())