import turtle as t

x = -80
y = 320
l = 30
day = ["Su", "Mo", "Tu", "We", "Th", "Fr", "Sa"]
current_month = 0
starting_day = 0  # Sunday

month_end = [31, 28, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31]
month_start = [0, 3, 3, 6, 1, 4, 6, 2, 5, 0, 3, 5]

wn = t.Screen()
wn.tracer(0)
screen = t.Screen()
screen.screensize(2000, 10000)

while current_month < 12:
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
                            t.write(f" {day[j]}", font=("Arial", 12), align="left")
                        t.fd(l)

                x += l
            t.penup()
            x = -80
            y -= l
        else:
            current_day = 1

            for j in range(0, 7):  # column
                t.goto(x, y)
                t.pendown()

                for k in range(4):
                    t.pendown()
                    t.rt(90)

                    if k == 3 and (month_start[current_month] <= j <= 7):
                        t.write(f" {current_day}", font=("Arial", 12), align="left")
                        current_day += 1

                    t.fd(l)

                x += l

            t.penup()
            x = -80
            y -= l

            while current_day <= month_end[current_month]:
                if starting_day == 7:
                    starting_day = 0
                starting_day += 1
                current_day += 1

    x = -80
    y -= l
    t.setheading(0)

wn.mainloop()
t.done()

