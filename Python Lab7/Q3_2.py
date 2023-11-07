import turtle as t
class Circle:
    def __init__(self, x=0, y=0, r=0):
        self.x = x
        self.y = y 
        self.r = r
    
    def getArea(self):
        return 3.14*self.r**2
    
    def getPerimater(self):
        return 2*3.14*self.r
    
    def move(self, newX, newY):
        self.x = newX
        self.y = newY
    
    def draw(self):
        t.penup()
        t.goto(self.x, self.y - self.r)
        t.pendown()
        t.circle(self.r)
        
cir = Circle(10, 20, 50)
print(cir.getArea())
print(cir.getPerimater())

cir.draw()
cir.move(40,50)
cir.draw()
t.done()

