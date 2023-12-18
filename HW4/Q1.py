import turtle

def equation(x0, y0, x1, y1, x2, y2) :
    turtle.goto(x2, y2-60)
    try:
        m = float(((y1-y0)/(x1-x0)))
        if m > 0:
            if float(y0) > float(m*(x0-x2)) + float(y2):
                turtle.write("p2 is on right side of the line", align="center")
            elif float(y0) < float(m*(x0-x2)) + float(y2):
                turtle.write("p2 is on left side of the line", align="center")
            elif float(y0) == float(m*(x0-x2)) + float(y2):
                turtle.write("p2 is on the line between p0 and p1")
        elif m < 0:
            if float(y0) < float(m*(x0-x2)) + float(y2):
                turtle.write("p2 is on right side of the line", align="center")
            elif float(y0) > float(m*(x0-x2)) + float(y2):
                turtle.write("p2 is on left side of the line", align="center")
            elif float(y0) == float(m*(x0-x2)) + float(y2):
                turtle.write("p2 is on the line between p0 and p1")
        elif m == 0:
            if y2 < y0:
                turtle.write("p2 is below the line", align="center")
            elif y2 > y0:
                turtle.write("p2 is above the line", align="center")
            elif y2 == y0:
                turtle.write("p2 is on the line between p0 and p1")
    except ZeroDivisionError:
        if x2 > x0:
            turtle.write("p2 is on right side of the line", align="center")
        elif x2 < x0:
            turtle.write("p2 is on left side of the line", align="center")
        elif x2 == x0:
            turtle.write("p2 is on the line between p0 and p1")

x0, y0= eval(input("Enter point0(p0): "))
x1, y1= eval(input("Enter point1(p1): "))
x2, y2= eval(input("enter point2(p2): "))
p0 = float(x0), float(y0)
p1 = float(x1), float(y1)
p2 = float(x2), float(y2)
# distance = ((x1-x0)*(x1-x0) + (y1-y0)*(y1-y0))**0.5
# space = distance/2
turtle.penup()
turtle.goto(x0, y0)
turtle.write(f"p0", align="center")
turtle.pendown()
turtle.goto(x1, y1)
turtle.write(f"p1")
turtle.penup()
turtle.goto(x2, y2)
turtle.write(f"p2", align="center")
equation(x0, y0, x1, y1, x2, y2)

turtle.done()