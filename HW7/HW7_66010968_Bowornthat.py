# Question 1
class Clock():
    def __init__(self, h=0, m=0, s=0):
        self.h = h
        self.m = m
        self.s = s
    
    def setTime(self, Newh, Newm, News):
        if News >= 60:
            Newm += News // 60
            self.s = News % 60
        else:
            self.s = News

        if Newm >= 60:
            Newh += Newm // 60
            self.m = Newm % 60
        else:
            self.m = Newm
        
        if Newh >= 24: 
            self.h = Newh % 24
        else:
            self.h = Newh

    def getTime(self):
        return f"{self.h:02d}:{self.m:02d}:{self.s:02d}"
    
    def tick(self):
        self.s += 1
        if self.s >= 60:
            self.s = 0
            self.m += 1
            if self.m >= 60:
                self.m = 0
                self.h += 1
                if self.h >= 24:
                    self.h = 0
        
    def displayTime(self):
        if self.h >= 12:
            print(f"{self.h-12:02d}:{self.m:02d}:{self.s:02d} PM")
        else:
            print(f"{self.h:02d}:{self.m:02d}:{self.s:02d} AM")
            
time = Clock()
time.setTime(25,45,62)
time.getTime()
time.displayTime()
time.tick()
time.displayTime()

# =============================================
# Question 2
class Poly():
    def __init__(self, co = ()):
        self.co = co
        
    def add(self, other):
        result = [0] * max(len(self.co), len(other.co))
        for i in range(len(self.co)):
            result[i] += self.co[i]
        for i in range(len(other.co)):
            result[i] += other.co[i]
        return Poly(tuple(result))
    
    def scalar_multiply(self, n):
        newco = []
        for i in self.co:
            newco.append(i * n)
        return Poly(tuple(newco))
    
    def power(self, n):
        if n == 0:
            return Poly((1,))
        elif n > 0:
            result = Poly(self.co)
            for i in range(n - 1):
                result = result.multiply(self) 
            return Poly(result.co)
        else: 
            raise ValueError("Please enter n >= 0.")

    def multiply(self, other): # multiply one by one
        newco = [0] * (len(self.co) + len(other.co) - 1) 
        for i, a in enumerate(self.co):
            for j, b in enumerate(other.co):
                newco[i + j] += a * b
        return Poly(tuple(newco))
    
    def diff(self):
        newco = []
        for i, a in enumerate(self.co):
            if i != 0:
                newco.append(a * i)
        return Poly(tuple(newco))
        
    def integrate(self):
        newco = [0]
        for i, a in enumerate(self.co):
            if i == 0:
                newco.append(a)
            else:
                newco.append(a / (i+1))
        return Poly(tuple(newco))
    
    def eval(self, n):
        result = 0
        for i, a in enumerate(self.co):
            result += a*n**i
        return result
    
    def print(self):
        result = []
        for i, a in enumerate(self.co):
            if a!= 0:
                if i == 0:
                    result.append(str(a))
                else:
                    if i > 0:
                        if a >= 0:
                            result.append(" + ")
                        else:
                            result.append(" - ")
                    result.append(f"{abs(a)}x^{i}")
        print("".join(result))
    
p = Poly((1, 0, -2))
p.print()
p.eval(3)
q = p.power(2)
q.print()
r = p.add(q)
r.print()
r.diff().print()

# =============================================

# Question 3
class LinearEquation():
    def __init__(self, a=0, b=0, c=0, d=0, e=0, f=0):
        self.__a = a
        self.__b = b
        self.__c = c
        self.__d = d
        self.__e = e
        self.__f = f

    def get_a(self):
        return self.__a
    
    def get_b(self):
        return self.__b
    
    def get_c(self):
        return self.__c
    
    def get_d(self):
        return self.__d
    
    def get_e(self):
        return self.__e
    
    def get_f(self):
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
        else:
            raise ValueError("The equaitons is not solveable.")
            
    def getY(self):
        divider = (self.__a*self.__d) - (self.__b*self.__c)
        if divider != 0:
            y = ((self.__a*self.__f) - (self.__e*self.__c)) / divider
            return y
        else:
            raise ValueError("The equaitons is not solveable.")
    
l = LinearEquation(2, 7, 2, -3, 0, 6)
l.isSolveable()
l.getX()
l.getY()
# =============================================
