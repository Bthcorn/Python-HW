# Question 1
from tkinter import *
from tkinter import messagebox

class Phone:
    def __init__(self):
        window = Tk()
        window.title("KMITL phone")
        window.grid_columnconfigure(0, weight= 1)
        window.grid_rowconfigure(0, weight=1)
        self.phone_number = StringVar()
        frame1 = Frame(window, padx= 5, pady=5)
        frame1.grid(row = 0, column= 0)
        # frame1.grid_columnconfigure([0, 1, 2, 3, 4, 5, 6], weight=1)
        # frame1.grid_rowconfigure([0, 1, 2, 3, 4, 5], weight=1)
        
        ent = Entry(frame1, width= 30, textvariable=self.phone_number, justify= RIGHT)
        ent.grid(row =0 , column= 0, columnspan= 6)
        
        
        buttons = [
            "1", "2", "3",
            "4", "5", "6",
            "7", "8", "9",
            "*", "0", "#"
        ]

        row, col = 1, 0
        for button_text in buttons:
            button = Button(frame1, text=button_text, command=lambda b=button_text: self.button_click(b))
            button.grid(row=row, column=col, columnspan=2, ipadx=5, ipady=5, sticky="EWNS")
            col += 2
            if col > 4:
                col = 0
                row += 1
                
        btt = Button(frame1, text= "Talk", command=self.talk)
        btt.grid(row= 5, column= 0, columnspan= 3, ipadx=5, ipady=5, sticky="EWNS")
        btd = Button(frame1, text= "<", command=self.delete)
        btd.grid(row= 5, column= 3, columnspan= 3, ipadx=5, ipady=5, sticky="EWNS")
        
        window.mainloop()
    
    def button_click(self, number):
        current_number = self.phone_number.get()
        self.phone_number.set(current_number + str(number))
    
    def talk(self):
        number = self.phone_number.get()
        messagebox.showinfo("Dialling", f"Dialling<<{number}>>")
        
    def delete(self):
        current_number = self.phone_number.get()
        self.phone_number.set(current_number[0:len(current_number)-1])
        
Phone()

#==============================================
# Question 2
from tkinter import *
from tkinter import filedialog, messagebox, ttk
from datetime import timedelta, datetime

class Todolist:
    def __init__(self, mainwindow):
        self.mainwindow = mainwindow
        mainwindow = Tk()
        mainwindow.geometry('600x400')
        mainwindow.title("Todo Lits")
        font1 =('Arial', 12)
        frame0 = Frame(mainwindow)
        frame0.pack()
        frame1 = Frame(mainwindow)
        frame1.pack()
        frame2 = Frame(mainwindow)
        frame2.pack()
        frame3 = Frame(mainwindow)
        frame3.pack()
        
        #menu -> save load and another for Focus time
        menubar = Menu(frame0)
        menu_file = Menu(menubar, tearoff=0)
        menu_edit = Menu(menubar, tearoff=0)
        
        menubar.add_cascade(label="File", menu= menu_file)
        menubar.add_cascade(label="Edit", menu= menu_edit)
        menu_file.add_command(label='New')
        menu_file.add_command(label='Open')
        menu_file.add_command(label='Save')
        menu_file.add_command(label='Exit')
        mainwindow.config(menu=menubar)
        
        #list of day
        
        day = Label(frame1, text="Select Day", font=font1)
        day.grid(row = 1, column= 1, sticky="ENWS")
        days = ['Monday', 'Tuesday', 'Wendesday', 'Thursday', 'Friday', 'Saturday', 'Sunday']
        cb1 = ttk.Combobox(frame1, values= days, width= 10,)
        cb1.grid(row= 1, column= 2, padx = 10, pady= 10, sticky="ENWS")
        
        #Board view -> Todo list, Doing list, Done list
        
        view = Label(frame2, text="Board View", font=font1)
        view.grid(row= 1, column= 1, sticky="W")
        todo_l = Label(frame2, text="To Do", font=font1)
        todo_l.grid(row= 2, column= 1, sticky="W")
        doin_l = Label(frame2, text="Doing", font=font1)
        doin_l.grid(row= 2, column= 2, sticky="W")
        done_l = Label(frame2, text="Done", font=font1)
        done_l.grid(row= 2, column= 3, sticky="W")
        todo = ttk.Treeview(frame2, columns=('Task','Tag'), show="headings")
        todo.heading("Task", text="Task")
        todo.heading("Tag", text="Tag")
        todo.column("Task", width= 100)
        todo.column("Tag", width= 100)
        todo.grid(row = 3, column= 1)
        doing = ttk.Treeview(frame2, columns=('Task','Tag'), show="headings")
        doing.heading("Task", text="Task")
        doing.heading("Tag", text="Tag")
        doing.column("Task", width= 100)
        doing.column("Tag", width= 100)
        doing.grid(row = 3, column= 2)
        done = ttk.Treeview(frame2, columns=('Task','Tag'), show="headings")
        done.heading("Task", text="Task")
        done.heading("Tag", text="Tag")
        done.column("Task", width= 100)
        done.column("Tag", width= 100)
        done.grid(row = 3, column= 3)
        
        #add task, delete task, move task (same as)
        task_l = Label(frame3, text="Enter Task")
        task_l.grid(row= 1, column=1)
        task_entry = Entry(frame3, width=30)
        task_entry.grid(row= 1, column=2, columnspan= 3)
        date_l = Label(frame3, text="Tag")
        date_l.grid(row= 1, column=5)
        date_entry = Entry(frame3, width=30)
        date_entry.grid(row= 1, column=6)
        add_bt = Button(frame3, text="Add Task")
        add_bt.grid(row= 1, column= 7, )
        del_bt = Button(frame3, text="Delete Task")
        del_bt.grid(row= 2, column= 1, )
        doin_bt = Button(frame3, text="Doing Task")
        doin_bt.grid(row= 2, column= 2, )
        doin_bt = Button(frame3, text="Done Task")
        doin_bt.grid(row= 2, column= 3,)
        
        #edit -> priority hightlight due date

        mainwindow.mainloop()
        

if __name__ == "__main__":
    mainwindow = Tk()
    Label(mainwindow, text="Welcome to Todo LITS!!").grid(row=0, column=0)
    app = Todolist(mainwindow)
    mainwindow.mainloop()
    

#==============================================
# Question 3
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