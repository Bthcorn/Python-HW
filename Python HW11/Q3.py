import turtle
turtle.speed(1)

class Point(object):
    def __init__(self):
        self.pt_list = []
    
    def getPoints(self, points):
        for i in range(0, len(points), 2):
            tuple1 = (points[i], points[i+1])
            self.pt_list.append(tuple1)
        return self.pt_list

    def draw(self):
        for (x, y) in self.pt_list:
            turtle.penup()
            turtle.goto(x * 20, y * 20)
            turtle.pendown()
            turtle.dot(5, 'black')
            turtle.penup()
    
        
class Rectangle2D(object):  
        
    def getRectangle(self, points):
        pt_x = []
        pt_y = []
        for (x, y) in points:
            pt_x.append(x)
            pt_y.append(y)
            
        x_max = max(pt_x)
        x_min = min(pt_x)
        y_max = max(pt_y)
        y_min = min(pt_y)
        height = abs(y_max-y_min)
        width = abs(x_max-x_min)
        xc = (x_max + x_min)/2
        yc = (y_max + y_min)/2
        
        turtle.penup()
        turtle.goto(xc * 20, yc * 20 - height / 2 * 20 )
        turtle.pendown()
        turtle.forward(width/2 * 20)
        turtle.left(90)
        turtle.forward(height * 20)
        turtle.left(90)
        turtle.forward(width * 20)
        turtle.left(90)
        turtle.forward(height * 20)
        turtle.left(90)
        turtle.forward(width/2 * 20)
        turtle.penup()
        print(f"The bounding rectangle is centered at ({xc}, {yc}) with width {width} and height {height}")
        
        
class Run():
    pt_list = []
    point = input("Enter the points: ")
    points = [float(x) for x in point.split()]
    
    x = Point()
    pt_list = x.getPoints(points)
    x.draw()
    y = Rectangle2D()
    y.getRectangle(pt_list)
    turtle.done()

Run()
