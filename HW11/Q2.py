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
