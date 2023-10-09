# Question1
name = input("Enter employee's name: ")
hour = float(input("Enter number of hours worked in a week: "))
payrate = float(input("Enter hourly pay rate: "))
ftax = float(input("Enter federal tax withholding rate: "))
stax = float(input("enter state tax withholding rate: "))
grosspay= hour*payrate
federal= ftax*grosspay
state= stax*grosspay
deduct =federal+state
print("Employee Name: ", name)
print("Hourly Worked: ", hour)
print("Pay Rate: " + "$" +str(payrate))
print("Gross Pay: " +"$"+ str(grosspay))
print("Deduction: ")
print("  Federal Withholding " + "("+ str(ftax*100) +"%"+ ") : " + "$" + str(format(federal, ".1f")))
print("  State Withholding " + "("+ str(stax*100) +"%" +") : " + "$" + str(format(state, ".2f")))
print("  Total Deduction : " + "$" + str(format(deduct, ".2f")))
print("Net Pay : " +"$"+ str(format(grosspay-deduct, ".2f")))
#=========================================================

# Question2
number = input("Enter a four digit integer: ")
print(str(number[::-1]))
#=========================================================

# Question3
length = eval(input("Enter the length pf the star: "))

import turtle

turtle.lt(36)
turtle.fd(length)
for i in range(4) :
    turtle.lt(144)
    turtle.fd(length)

turtle.done() 
#=========================================================

# Question4
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
#=========================================================

# Question 5
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
#=========================================================