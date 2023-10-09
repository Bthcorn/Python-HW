radius = eval(input("Enter the radius of the ring: "))

import turtle
turtle.width(7)
turtle.color("blue")
turtle.penup()
turtle.goto(-11,-2.5)
turtle.pendown()
turtle.circle(radius)

turtle.color("black")
turtle.penup()
turtle.goto(0 + (radius+1.2*radius), -2.5)
turtle.pendown()
turtle.circle(radius)

turtle.color("red")
turtle.penup()
turtle.goto(11 + 2*(radius+1.2*radius),  -2.5)
turtle.pendown()
turtle.circle(radius)

turtle.color("yellow")
turtle.penup()
turtle.goto(-5.5 + 1.1*radius , -7.5 - 1.1*radius)
turtle.pendown()
turtle.circle(radius)

turtle.color("green")
turtle.penup()
turtle.goto(5.5+ 1.5*(radius+1.2*radius) , -7.5 -1.1*radius)
turtle.pendown()
turtle.circle(radius)

turtle.done()
