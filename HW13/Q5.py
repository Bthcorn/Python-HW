from tkinter import *
import math

class Tree:
    def __init__(self):
        window = Tk()
        window.title("Recursive Tree")
        
        self.height = 400
        self.width = 400
        self.canvas = Canvas(window, height=self.height, width=self.width, bg="white")
        self.canvas.pack()
        
        frame1 = Frame(window)
        frame1.pack()
        
        Label(frame1, text="Enter the depth: ").pack(side=LEFT)
        
        self.depth = StringVar()
        Entry(frame1, textvariable=self.depth, justify=RIGHT).pack(side=LEFT)
        Button(frame1, text="Display", command=self.display).pack(side=LEFT)
        
        self.angle = math.pi/6
        self.scale = 0.6
        
        window.mainloop()
        
    def drawLine(self, x1, y1, x2, y2):
        self.canvas.create_line(x1, y1, x2, y2, tags="line")
        
    def display(self):
        self.canvas.delete("line")
        depth = int(self.depth.get())
        return self.drawBranch(depth, self.width/2, self.height, self.height/3, math.pi/2)
        
    def drawBranch(self, depth, x1, y1, length, angle):
        if depth >= 0:
            depth -= 1 
            x2 = x1 + int(math.cos(angle) * length)
            y2 = y1 - int(math.sin(angle) * length)
            
            self.drawLine(x1, y1, x2, y2)
            
            self.drawBranch(depth, x2, y2, length * self.scale, angle + self.angle)
            self.drawBranch(depth, x2, y2, length * self.scale, angle - self.angle)
     
Tree()
        