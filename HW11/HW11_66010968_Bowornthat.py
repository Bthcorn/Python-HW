# Question 1 
from time import sleep
class Clock:
    def __init__(self, hh, mm, ss):
        self.hh = hh
        self.mm = mm
        self.ss = ss
        
    def run(self):
        while True:
            self.ss += 1
            if self.ss == 60:
                self.ss = 0
                self.mm += 1
            if self.mm == 60:
                self.mm = 0
                self.hh += 1
            if self.hh == 24:
                self.hh = 0
            print(f"{self.hh:02d}:{self.mm:02d}:{self.ss:02d}")
            sleep(1)
        
        
    def setTime(self, h, m, s):
        self.hh = h
        self.mm = m 
        self.ss = s
        
        
class AlarmClock(Clock):
    def __init__(self, hh, mm, ss, alarm_on_off):
        super().__init__(hh, mm, ss)
        self.alarm_hh = hh
        self.alarm_mm = mm
        self.alarm_ss = ss
        self.alarm_on_off =  alarm_on_off
        
    def setAlarmTime(self, h, m, s):
        self.alarm_hh = h
        self.alarm_mm = m
        self.alarm_ss = s
        
    def alarm_on(self):
        self.alarm_on_off = True
    
    def alarm_off(self): 
        self.alarm_on_off = False
    
    def run(self):
        while self.alarm_on_off == True:
            self.ss += 1
            if self.ss == 60:
                self.ss = 0
                self.mm += 1
            if self.mm == 60:
                self.mm = 0
                self.hh += 1
            if self.hh == 24:
                self.hh = 0
            print(f"{self.hh:02d}:{self.mm:02d}:{self.ss:02d}")
            
            if self.hh == self.alarm_hh and self.mm == self.alarm_mm and self.ss == self.alarm_ss:
                print("Time's up!")
                self.alarm_off()

            sleep(1)
            
# x = Clock(20,50,49)
# x.setTime(20,59,49)
# x.run()
x = AlarmClock(20,50,49, True)
x.setTime(20,59,49)
x.setAlarmTime(21,0,0)
# x.alarm_off()
x.alarm_on()
x.run()
        
# =====================================================
# Question 2
import turtle
turtle.speed(0)

def RobotBattle():
    #robotList stores the list of robots in the battle
    robotList = []
    
    while True:
        # Clear the screen and draw the robots
        turtle.clear()
        for robot in robotList:
            robot.draw()
            
        # Display the status of each robot
        print("==== Robots ====")
        
        i = 0
        for robot in robotList:
            print(i, " : ")
            robot.displayStatus()
            i += 1
        print("===============")
        
        #Ask user which robot to command or to create a new robot
        choice = input("Enter which robot to order, 'c' to create new robot, 'q' to quit: ")
        if choice == 'q':
            break
        elif choice == 'c':
            print("Enter which type of robots to create")
            robotType = input("'r' for Robot, 'm' for MedicBot, 's' for StrikerBot: ")
            if robotType == 'r':
                newRobot = Robot()
            if robotType == 'm':
                newRobot = MedicBot()
            if robotType == 's':
                newRobot = StrikerBot()
            robotList = robotList + [newRobot]
        else:
            n = int(choice)
            robotList[n].command(robotList)
        
        #Delete all the robots with health <= 0 from the list
        i = 0 
        for robot in robotList:
            if (robot.health <= 0):
                del robotList[i]
            i += 1
            
class Robot(object):
    def __init__(self, x= 100, y= 100, health= 100, energy= 100):
        self.x = x
        self.y = y
        self.health = health
        self.energy = energy
        
    def move(self, x, y):
        if self.energy > 0:
            self.x = x
            self.y = y
            self.energy -= 10
        
    def draw(self):
        turtle.penup()
        turtle.goto(self.x, self.y - 26)
        turtle.pendown()
        turtle.circle(26)
        turtle.penup()
        
        
    def displayStatus(self):
        print("x=", self.x, "y", self.y, "health=", self.health, "energy=", self.energy)
        
    def command(self, robotList):
        print("Possible action: move")
        newX = int(input("Enter new x-coordinate: "))
        newY = int(input("Enter new y-coordinate: "))
        self.move(newX, newY)
    
    
class MedicBot(Robot):
    def __init__(self, x=100, y=100, health=100, energy=100):
        super().__init__(x, y, health, energy)
        
    def heal(self, robot):
        r = ((self.x - robot.x)**2 + (self.y - robot.y)**2) ** 0.5
        if self.health >= 20 and r <= 10:
            self.energy -= 20
            robot.health += 10
    
    def draw(self):
        turtle.penup()
        turtle.goto(self.x, self.y)
        turtle.goto(self.x, self.y - 15)
        turtle.fd(5)
        for i in range(4):
            turtle.pendown()
            turtle.lt(90)
            turtle.fd(10)
            turtle.rt(90)
            turtle.fd(10)
            turtle.lt(90)
            turtle.fd(10)
        turtle.penup()
        turtle.goto(self.x, self.y - 26)
        turtle.pendown()
        turtle.circle(26)
        turtle.penup()
        
    def command(self, robotList):
        print("Possible action: move 'm' or heal other robot 'h'")
        command = input("Choose the command: ")
        if command == 'm':
            newX = int(input("Enter new x-coordinate: "))
            newY = int(input("Enter new y-coordinate: "))
            self.move(newX, newY)
        elif command == 'h':
            n = int(input("Which robot to heal (number in list): "))
            self.heal(robotList[n])
            print("Successful healing")
       
class StrikerBot(Robot):
    def __init__(self, x=100, y=100, health=100, energy=100, missle= 5):
        super().__init__(x, y, health, energy)
        self.missle = missle
        
    def draw(self):
        turtle.penup()
        turtle.rt(90)
        turtle.goto(self.x, self.y)
        turtle.goto(self.x, self.y - 15)
        turtle.pendown()
        turtle.lt(45)
        for i in range(4):
            turtle.lt(90)
            turtle.fd(21.2132)
        turtle.rt(-45)
        turtle.penup()
        turtle.goto(self.x, self.y - 26)
        turtle.pendown()
        turtle.circle(26)
        turtle.penup()
    
    def strike(self, robot):
        r = ((self.x - robot.x)**2 + (self.y - robot.y)**2) ** 0.5
        if self.energy >= 20 and self.missle > 0 and r <= 10:
            self.energy -= 20
            self.missle -= 1
            robot.health -= 50
            
    def displayStatus(self):
        print("x=", self.x, "y", self.y, "health=", self.health, "energy=", self.energy, "missile=", self.missle)
        
    def command(self, robotList):
        print("Possible action: move 'm' or strike other robot 's'")
        command = input("Choose the command: ")
        if command == 'm':
            newX = int(input("Enter new x-coordinate: "))
            newY = int(input("Enter new y-coordinate: "))
            self.move(newX, newY)
        elif command == 's':
            n = int(input("Which robot to strike (number in list): "))
            self.strike(robotList[n])
            print("Strike!")
            
RobotBattle()

# =====================================================
# Question 3
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

# =====================================================
# Question 4
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
    draw.draw(0, 0)
    print("Width: ", draw.getWidth())
    
drawNum(1)
drawNum(8)
drawNum(9)

done()
# =====================================================
# Question 5

class StationaryGood():
    def __init__(self, name, price, quantity):
        self.name = name
        self.price = price
        self.quantity = quantity
    
    def getCost(self):
        pass
    
class Magazine(StationaryGood):
    def __init__(self, name, price, quantity):
        super().__init__(name, price, quantity)
        
    def getCost(self):
        return self.price * self.quantity
    
class Book(StationaryGood):
    def __init__(self, name, price, quantity):
        super().__init__(name, price, quantity)
    
    def getCost(self):
        return self.price * self.quantity * 0.9

class Ribbon(StationaryGood):
    def __init__(self, name, price, quantity):
        super().__init__(name, price, quantity)
    
    def getCost(self):
        return self.price * self.quantity
    
basket = [ Magazine("Computer World", 70, 3), Book("Window 7 for Beginners", 200, 2), Ribbon("Blue ribbon", 5, 10)]

def getTotalCost(basket):
    totalcost = 0
    for com in basket:
        price = com.getCost()
        print(f"Name: {com.name} q:{com.quantity} -> price: {price}")
        totalcost += price
    print(f"Total cost: {totalcost} Bahts")
    
getTotalCost(basket)

# =====================================================
