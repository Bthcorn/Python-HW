import turtle
import math
x1,y1 = eval(input("Enter the first point: "))
x2,y2 = eval(input("Enter the second point: "))
x3,y3 = eval(input("Enter the third point: "))
p1 = x1, y1
p2 = x2, y2
p3 = x3, y3
distance1 = ((x1-x2)**2 +(y1-y2)**2)**0.5
distance2 = ((x2-x3)**2 +(y2-y3)**2)**0.5
distance3 = ((x3-x1)**2 +(y3-y1)**2)**0.5
# calculate area
s = (distance1 + distance2 + distance3)/2
area = math.sqrt(s*(s-distance1)*(s-distance2)*(s-distance3))

turtle.penup()
turtle.goto(x1, y1)
turtle.write(f"p1 {p1}")
turtle.pendown()
turtle.goto(x2, y2)
turtle.write(f"p2 {p2}")
turtle.goto(x3,y3)
turtle.write(f"p3 {p3}")
turtle.goto(x1,y1)
turtle.penup()
turtle.goto((x1+x2)/2, (y1+y2)/2 - 40)
turtle.write(f"The area of the triangle: {area}", align="center")

turtle.done()