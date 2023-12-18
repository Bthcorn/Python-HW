from tkinter import *

class Playcircle:
    def __init__(self):
        window = Tk()
        window.title("Circle")
        self.canvas = Canvas(window, width= 500, height= 300, bg ="white" )
        self.canvas.pack(fill=BOTH, expand=True)
        self.canvas.bind("<Button-1>", self.draw)
        self.canvas.bind("<Button-3>", self.delete)
        window.mainloop()
        
    def delete(self, event):
        x, y = event.x, event.y
        closest_circle = self.canvas.find_closest(x, y)
        if closest_circle:
            self.canvas.delete(closest_circle)
        
    def draw(self, event):
        x1, y1 = event.x, event.y
        self.canvas.create_oval(x1- 25, y1 + 25, x1 + 25, y1 - 25)     
        
Playcircle()