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
