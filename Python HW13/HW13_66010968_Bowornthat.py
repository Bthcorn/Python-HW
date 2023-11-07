# Question 1
def print_btree(node, depth= 0):     
    if isinstance(node, list):
        if depth > 0:
            print("." * depth + str(node[0]))
        else:
            print(node[0])
        for child in node[:][1]:
            print_btree(child, depth + 1)
    else:
        print("." * depth + str(node))
        
list1 = [1, [[11,[111, 112]], [12, [121, [122, [1221, 1222]]]]]]
print_btree(list1, 0)

# ====================================================
# Question 2
def display_f(n):
    if n == 0:
        print(0)
        return 0
    if n > 0 and n % 2 == 0:
        print(2 * display_f(n/2) + 1)
        return 2 * display_f(n/2) + 1
    else:
        print(0)
        return 0
    
display_f(0)
display_f(7)
display_f(14)
display_f(24)

# ====================================================
# Question 3.1
def perm2(t, start=0):
    if start >= len(t):
        return

    for i in t:
        if t[start] != i:
            print((t[start], i))

    perm2(t, start + 1)

perm2((1, 2, 3))

# Question 3.2
def perm3(t, current=None):
    if current is None:
        current = []

    if len(current) == 3:
        print(tuple(current))
        return

    for num in t:
        if num not in current:
            current.append(num)
            perm3(t, current)
            current.pop()

perm3((1, 2, 3, 4))

# Question 3.3
def perm(t, n, current=None):
    if current is None:
        current = []

    if len(current) == n:
        print(tuple(current))
        return

    for num in t:
        if num not in current:
            current.append(num)
            perm3(t, current)
            current.pop()
            
perm((1, 2, 3), 3)

# ====================================================
# Question 5
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
        self.entry_depth = Entry(frame1, textvariable=self.depth, justify=RIGHT)
        self.entry_depth.pack(side=LEFT)
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
# ====================================================
