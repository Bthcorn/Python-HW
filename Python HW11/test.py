# pt_list = []
# pt_x = []
# pt_y = []
# point = input("Enter the points: ")
# # points = point.split()
# points = [float(x) for x in point.split()]

# for i in range(0, len(points), 2):
#     tuple = (points[i], points[i+1])
#     pt_list.append(tuple)
#     pt_x.append(points[i])
#     pt_y.append(points[i+1])

# x_max = max(pt_x)
# x_min = min(pt_x)
# y_max = max(pt_y)
# y_min = min(pt_y)
# height = abs(y_max-y_min)
# width = abs(x_max-x_min)
# print("x_max: ", x_max)
# print("x_min: ", x_min)
# print("y_max: ", y_max)
# print("y_min: ", y_min)
# print("height: ", height)
# print("width: ", width)
# print(pt_list)
# print(pt_x)
# print(pt_y)

# import turtle

# # Create a Turtle screen and set up the Turtle
# screen = turtle.Screen()
# t = turtle.Turtle()

# # Set the text to be drawn
# text_to_draw = "A"

# # Move the Turtle to the desired position
# x = 100
# y = 100
# t.penup()
# t.goto(x, y)

# # Set the font and size (optional)
# font = ("Arial", 24, "normal")
# t.write(text_to_draw, font=font, align="center")

# # Close the Turtle graphics window when clicked
# screen.exitonclick()

from turtle import *

def moveto(x,y):
    pu()
    goto(x,y)
    pd()
    setheading(0)

#x and y let the user place their numbers down, d is length of sides.
def nine(d):
    point = pos()
    fd(d)
    rt(90)
    fd(d*2)
    bk(d)
    rt(90)
    fd(d)
    rt(90)
    fd(d)
    pu()
    goto(point)
    pd()
    setheading(0)

def eight(d):
        point = pos()
        fd(d)
        rt(90)
        fd(d*2)
        for i in range(3):
            rt(90)
            fd(d)
        bk(d)
        lt(90)
        fd(d)
        pu()
        goto(point)
        pd()
        setheading(0)

def seven(d):
    point = pos()
    fd(d)
    rt(90)
    fd(d*2)
    bk(d*2)
    lt(90)
    bk(d)
    pu()
    goto(point)
    pd()
    setheading(0)

def six(d):
        point = pos()
        fd(d)
        bk(d)
        rt(90)
        fd(d*2)
        for i in range(3):
            lt(90)
            fd(d)
        rt(90)
        fd(d)
        pu()
        goto(point)
        pd()
        setheading(0)

def five(d):
    point = pos()
    fd(d)
    bk(d)
    rt(90)
    fd(d)
    lt(90)
    fd(d)
    for i in range(2):
        rt(90)
        fd(d)
    pu()
    goto(point)
    pd()
    setheading(0)

def four(d):
        point = pos()
        rt(90)
        fd(d)
        for i in range(2):
            lt(90)
            fd(d)
        bk(d * 2)
        pu()
        goto(point)
        pd()
        setheading(0)

def three(d):
        point = pos()
        for i in range(2):
            fd(d)
            rt(90)
        fd(d)
        for i in range(2):
            bk(d)
            rt(90)
        bk(d)
        pu()
        goto(point)
        pd()
        setheading(0)

def two(d):
    point = pos()
    fd(d)
    rt(90)
    fd(d)
    lt(90)
    for i in range(2):
        bk(d)
        lt(90)
    bk(d)
    pu()
    goto(point)
    pd()
    setheading(0)

def one(d):
    point = pos()
    pu()
    fd(d)
    pd()
    rt(90)
    fd(d*2)
    pu()
    goto(point)
    pd()
    setheading(0)

def zero(d):
    point = pos()
    fd(d)
    rt(90)
    fd(d*2)
    rt(90)
    fd(d)
    rt(90)
    fd(d*2)
    pu()
    goto(point)
    pd()
    setheading(0)

def drawnum(n):
    d=50
    if (n == 1):
        one(d)
    if (n ==2):
        two(d)
    if (n==3):
        three(d)
    if (n==4):
       four(d)
    if (n==5):
        five(d)
    if (n==6):
        six(d)
    if (n==7):
        seven(d)
    if (n==8):
        eight(d)
    if (n==9):
        nine(d)
    if (n==0):
        zero(d)
    pu()
    fd(1.5*d)
    pd()
drawnum(1)
drawnum(2)
drawnum(3)
drawnum(0)
done()
