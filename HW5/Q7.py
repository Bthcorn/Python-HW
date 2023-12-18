import turtle as t
x = -80
y = 320
l = 30
day = ["Su", "Mo", "Tu", "We", "Th", "Fr", "Sa"]
current_month = 0  # can be following according to while loop
# while loop run month by month
wn = t.Screen()
wn.tracer(0)
screen = t.Screen()
screen.screensize(2000 ,10000)
current_day = 1  # Initialize the current day number
current_day_of_week = 0
month_start = [0, 3, 3, 6, 2, 4, 6, 2, 5, 0, 3, 5] #column
month_end = [31, 28, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31]
# loop for building table
while current_month < 13:
    # current_month = 0
    t.speed(0)
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
    for i in range(0, 6): # row
        t.penup()
        t.goto(x, y)
        t.pendown()
        for j in range(0, 7): # column
            t.goto(x, y)
            t.pendown()
            for k in range(4): # each square
                if i == 0:
                    t.pendown()
                    t.rt(90)
                    if k == 3:
                        t.write(f" {day[j]}", font=("Arial", 12),
                                align="left")  # create days
                    t.fd(l)
                else:
                    t.pendown()
                    t.rt(90)
                    if k == 3 and i >= 1:
                        # if current_day <= month_end[current_month] :
                        t.write(f" {current_day}", font=("Arial", 12), align="left")
                        current_day += 1
                        if current_day == month_end[current_month] + 1:
                            current_day = 1
                            current_month += 1
                    t.fd(l)
            x += l
        t.penup()
        x = -80
        y -= l
    x = -80
    y -= 2*l
    # current_month +=1
    t.setheading(0) # To set new start
    




t.done()
# loop for running day

# loop for month with creating next month with a gap