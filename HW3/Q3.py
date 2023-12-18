length = eval(input("Enter the length pf the star: "))

import turtle

turtle.lt(36)
turtle.fd(length)
for i in range(4) :
    turtle.lt(144)
    turtle.fd(length)

turtle.done() 