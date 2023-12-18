import abc
from turtle import *

class Char(abc.ABC):
    
    @abc.abstractclassmethod
    def draw(x, y):
        pass
    
    @abc.abstractclassmethod
    def getWidth():
        pass
    
    
class Char0(Char):
    
    def draw(x, y):
        d = 20
        pu()
        goto(x, y)
        pd()
        setheading(0)
        
        point = pos()
        fd(d)
        rt(90)
        fd(d*2)
        rt(90)
        fd(d)
        rt(90)
        fd(d*2)
        pu()
        goto(point)
        pd()
        setheading(0)
    
    def getWidth():
        return 20
    
class Char1(Char):

    def draw(x, y):
        pu()
        goto(x, y)
        pd()
        setheading(0)
        d = 20
        point = pos()
        pu()
        fd(d)
        pd()
        rt(90)
        fd(d*2)
        pu()
        goto(point)
        pd()
        setheading(0)
    
    def getWidth():
        return 1

class Char2(Char):
        
    def draw(x, y):
        pu()
        goto(x, y)
        pd()
        setheading(0)
        
        d = 20
        point = pos()
        fd(d)
        rt(90)
        fd(d)
        lt(90)
        for i in range(2):
            bk(d)
            lt(90)
        bk(d)
        pu()
        goto(point)
        pd()
        setheading(0)
        
    def getWidth():
        return 20

class Char3(Char):
    
    def draw(x, y):
        pu()
        goto(x, y)
        pd()
        setheading(0)
        
        d = 20
        point = pos()
        for i in range(2):
            fd(d)
            rt(90)
        fd(d)
        for i in range(2):
            bk(d)
            rt(90)
        bk(d)
        pu()
        goto(point)
        pd()
        setheading(0)
    
    def getWidth():
        return 20

class Char4(Char):
    
    def draw(x, y):
        pu()
        goto(x, y)
        pd()
        setheading(0)
        
        d = 20
        point = pos()
        rt(90)
        fd(d)
        for i in range(2):
            lt(90)
            fd(d)
        bk(d * 2)
        pu()
        goto(point)
        pd()
        setheading(0)
    
    def getWidth():
        return 20


class Char5(Char):   
    def draw(x, y):
        pu()
        goto(x, y)
        pd()
        setheading(0)
        
        d = 20
        point = pos()
        fd(d)
        bk(d)
        rt(90)
        fd(d)
        lt(90)
        fd(d)
        for i in range(2):
            rt(90)
            fd(d)
        pu()
        goto(point)
        pd()
        setheading(0)
        
    def getWidth():
        return 20

class Char6(Char):
    def draw(x, y):
        pu()
        goto(x, y)
        pd()
        setheading(0)
        
        d = 20
        point = pos()
        fd(d)
        bk(d)
        rt(90)
        fd(d*2)
        for i in range(3):
            lt(90)
            fd(d)
        rt(90)
        fd(d)
        pu()
        goto(point)
        pd()
        setheading(0)
    
    def getWidth():
        return 20

class Char7(Char):
    def draw(x, y):
        pu()
        goto(x, y)
        pd()
        setheading(0)
        
        d = 20
        point = pos()
        fd(d)
        rt(90)
        fd(d*2)
        bk(d*2)
        lt(90)
        bk(d)
        pu()
        goto(point)
        pd()
        setheading(0)
    
    def getWidth():
        return 20
        
class Char8(Char):
        
    def draw(x, y):
        pu()
        goto(x, y)
        pd()
        setheading(0)
        
        d = 20
        point = pos()
        fd(d)
        rt(90)
        fd(d*2)
        for i in range(3):
            rt(90)
            fd(d)
        bk(d)
        lt(90)
        fd(d)
        pu()
        goto(point)
        pd()
        setheading(0)
    
    def getWidth():
        return 20
    
class Char9(Char):
        
    def draw(x, y):
        pu()
        goto(x, y) 
        pd()
        setheading(0)
        
        d = 20
        point = pos()
        fd(d)
        rt(90)
        fd(d*2)
        bk(d)
        rt(90)
        fd(d)
        rt(90)
        fd(d)
        pu()
        goto(point)
        pd()
        setheading(0)
    
    def getWidth():
        return 20
    
def drawNum(x):
    
    dic = { 0: Char0, 1: Char1, 2: Char2, 3: Char3, 4: Char4, 5: Char5, 6: Char6, 7: Char7, 8: Char8, 9: Char9}
    draw = dic[x]
    draw.draw(0 + 10*x, 0)
    print("Width: ", draw.getWidth())
    
drawNum(1)
drawNum(8)
drawNum(5)

done()

# dic = { 0: Char0, 1: Char1, 2: Char2, 3: Char3, 4: Char4, 5: Char5, 6: Char6, 7: Char7, 8: Char8, 9: Char9}
# dic[9].draw(0,0)