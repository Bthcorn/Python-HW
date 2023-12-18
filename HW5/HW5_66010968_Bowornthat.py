# Question 1
n = int(input("Enter a number to find its square root: "))
if n < 0:
    raise ValueError("Please input number greater than or equal to 0!")  
guess = n/2
time = 5
while time < 8: 
    for i in range(time):
        temp = float(n/guess)
        guess = (guess + temp)/2
    print(time, "times approximation:",  format(guess, ".3f"))
    time += 1
    guess = n/2
# ====================================================

# Question 2
import turtle as t
x = -80
y = 320
l = 30
day = ["Su", "Mo", "Tu", "We", "Th", "Fr", "Sa"]
current_month = 0
wn = t.Screen()
wn.tracer(0)
screen = t.Screen()
screen.screensize(2000, 10000)
current_day = 1  # Initialize the current day number
month_end = [31, 28, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31]
month_start = [0, 3, 3, 6, 1, 4, 6, 2, 5, 0, 3, 5]

# loop for building table
while current_month < 12:
    # current_month = 0
    t.speed(0.5)
    t.penup()
    t.goto(x, y)
    t.pendown()
    t.fd(210)
    t.rt(90)
    t.fd(l)
    t.rt(90)
    t.fd(210)
    t.write(f" Month#{current_month + 1}", font=("Arial", 12), align="left")
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
                    if current_month == 12:
                        break
                    if k == 3 and (month_start[current_month] <= j <= 7):
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
                        if current_month == 12 or current_day == 1:
                            t.fd(l)
                            break
                        if current_day <= month_end[current_month]:
                            t.write(f" {current_day}", font=(
                                "Arial", 12), align="left")
                            current_day += 1
                            if current_day > month_end[current_month]:
                                current_day = 1
                                current_month += 1
                    t.fd(l)
                x += l
            t.penup()
            x = -80
            y -= l
    x = -80
    y -= l
    t.setheading(0)  # To set new start
t.done()
# ====================================================

# Question 3
n = int(input("Enter a integer: "))
if n <= 0:
    raise ValueError("Please input integer greater than or equal to 1!")  

while n > 0:
    print('*')
    for i in range(1, n):
        for j in range(0, i + 1):
            print('*', end='')
        print()
    for i in range(n, 1, -1):
        if i < 2*n-1:
            for j in range(i, 1, -1):
                print('*', end='')
            print()
        elif i >= 2*n-1 :
            for j in range(i, 1, -1):
                print('*', end='')
            print(end='')
    n -= 1
# ====================================================
