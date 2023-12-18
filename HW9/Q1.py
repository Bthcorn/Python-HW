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