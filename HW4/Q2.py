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