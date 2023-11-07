import turtle as t

class Rectangle:
    def __init__(self, x=0, y=0, width=0, height=0):
        self.x = x
        self.y = y
        self.width = width
        self.height = height

    def getArea(self):
        print(self.width*self.height)
        
    def getPerimeter(self):
        print(2*self.width + 2*self.height)
    
    def move(self, NewX, NewY):
        self.x = NewX
        self.y = NewY
            
    def intersect(self, rec):
        if (rec.x < self.x + self.width and
            rec.x + rec.width > self.x and
            rec.y - rec.height < self.y and
            rec.y > self.y - self.height):
            
            intersection_x = max(self.x, rec.x)
            intersection_y = min(self.y, rec.y)
            intersection_width = min(self.x + self.width, rec.x + rec.width) - intersection_x
            intersection_height = abs(max(self.y - self.height, rec.y - rec.height) - intersection_y)
        
            t.penup()
            t.goto(intersection_x, intersection_y)
            t.pendown()
            t.fd(intersection_width)
            t.rt(90)
            t.fd(intersection_height)
            t.rt(90)
            t.fd(intersection_width)
            t.rt(90)
            t.fd(intersection_height)
        else:
            return None


    def draw(self):
        t.penup()
        t.goto(self.x, self.y)
        t.pendown()
        t.fd(self.width)
        t.rt(90)
        t.fd(self.height)
        t.rt(90)
        t.fd(self.width)
        t.rt(90)
        t.fd(self.height)
        t.setheading(0)
        
        
a = Rectangle(0, 0, 100, 200)
b = Rectangle(-200, 0, 100, 10)
d = Rectangle(-200, -50, 250, 50)
a.draw()
# b.draw()
d.draw()
e = a.intersect(d)
# e1 = a.intersect(b)



t.done()


        
        