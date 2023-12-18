# Question 1
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
# =====================================================
# Question 2
import turtle

def rectangle (x, y, w, h):
    turtle.penup()
    turtle.goto(x,y)
    turtle.write(f"{x,y}", align="center")
    turtle.right(180)
    turtle.goto(x,y-(h/2))
    turtle.pendown()
    turtle.forward(w/2)
    turtle.right(90)
    turtle.forward(h)
    turtle.right(90)
    turtle.forward(w)
    turtle.right(90)
    turtle.forward(h)
    turtle.right(90)
    turtle.forward(w/2)
    turtle.left(180)

x1, y1, w1, h1 = eval(input("Enter the center of first rectangle, width, and height: "))
x2, y2, w2, h2 = eval(input("Enter the center of second rectangle, width, and height: "))

x1_left = x1 - w1 / 2
x1_right = x1 + w1 / 2
y1_top = y1 + h1 / 2
y1_bottom = y1 - h1 / 2

x2_left = x2 - w2 / 2
x2_right = x2 + w2 / 2
y2_top = y2 + h2 / 2
y2_bottom = y2 - h2 / 2

turtle.speed(4)
rectangle(x1, y1, w1, h1)
rectangle(x2, y2, w2, h2)
turtle.penup()
turtle.goto(x2, y2-50)

# Check for overlap
if x1_left <= x2_right and x1_right >= x2_left and y1_bottom <= y2_top and y1_top >= y2_bottom:
    if x1_left > x2_left and x1_right < x2_right and y1_bottom > y2_bottom and y1_top < y2_top:
        turtle.write("The first rectangle is inside the second one.")
    elif x1_left < x2_left and x1_right > x2_right and y1_bottom < y2_bottom and y1_top > y2_top:
        turtle.write("The second rectangle is inside the first one.")
    else:
        turtle.write("The two rectangles overlap.")
else:
    turtle.write("The two rectangles do not overlap.")

turtle.done()