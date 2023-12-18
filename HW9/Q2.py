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
    