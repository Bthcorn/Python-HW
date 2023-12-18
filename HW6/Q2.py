# def calendar_of_2023():

import turtle as t
x = -80
y = 80
l = 30
day = ["Mo", "Tu", "We", "Th", "Fr", "Sa", "Su"]
wn = t.Screen()
wn.tracer(0)
screen = t.Screen()
screen.screensize(2000, 10000)
current_day = 1  # Initialize the current day number
month_end = [31, 28, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31]
month_start = [6, 2, 2, 5, 0, 3, 5, 1, 4, 6, 2, 4]
month = ["January", "Febuary", "March", "April", "May", "June",
         "July", "August", "September", "October", "November", "December"]

def calendar_of_2023(n):
    global x,y,l,current_day
    t.speed(0.5)
    t.penup()
    t.goto(x, y)
    t.pendown()
    t.fd(210)
    t.rt(90)
    t.fd(l)
    t.rt(90)
    t.fd(105)
    t.write(f" {month[n-1]} 2023", font=("Arial", 12), align="center")
    t.fd(105)
    t.rt(90)
    t.fd(l)
    t.rt(90)
    t.lt(90)
    y -= l
    for i in range(0, 7):  # row
        t.penup()
        t.goto(x, y)
        t.pendown()
        if i == 0:
            for j in range(0, 7):  # column
                t.goto(x, y)
                t.pendown()
                for k in range(4):  # each square
                    if i == 0:
                        t.pendown()
                        t.rt(90)
                        if k == 3:
                            t.write(f" {day[j]}", font=("Arial", 12),
                                    align="left")  # create days
                        t.fd(l)
                x += l
            t.penup()
            x = -80
            y -= l
        elif i == 1:
            current_day = 1
            for j in range(0, 7):  # column
                t.goto(x, y)
                t.pendown()
                for k in range(4):
                    t.pendown()
                    t.rt(90)
                    # if current_month == 12:
                    #     break
                    if k == 3 and (month_start[n-1] <= j <= 7):
                        t.write(f" {current_day}", font=(
                            "Arial", 12), align="left")
                        current_day += 1
                    t.fd(l)
                x += l
            t.penup()
            x = -80
            y -= l
        elif i > 1:
            for j in range(0, 7):  # column
                t.penup()
                t.goto(x, y)
                t.pendown()
                for k in range(4):
                    t.pendown()
                    t.rt(90)
                    if k == 3:
                        if current_day == 1:
                            t.fd(l)
                            break
                        if current_day <= month_end[n-1]:
                            t.write(f" {current_day}", font=(
                                "Arial", 12), align="left")
                            current_day += 1
                            if current_day > month_end[n-1]:
                                current_day = 1
                    t.fd(l)
                x += l
            t.penup()
            x = -80
            y -= l
    # x = -80
    # y -= l
    # t.setheading(0)  # To set new start
    t.done()

calendar_of_2023(10)