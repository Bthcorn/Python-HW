d = ((x1-x2)*(x1-x2)+(y1-y2)*(y1-y2))**0.5 # calculate the distance between 2 centers of rectangles
r1 = (w1*w1 + l1*l1)**0.5 /2 # diagonal of rectangle devided by 2
r2 = (w2*w2 + l2*l2)**0.5 /2
turtle.penup()
turtle.goto(x2, y2-50)
if d <= r1+r2 :
    # if d <= (w1+w2)/2 or d <= (l1+l2)/2: 
    #     turtle.write("The two rectangles overlap.")
    if  (x1 + l1/2) < (x2 + l2/2) and (y1 + w1/2) < (y2 + w2/2): 
        turtle.write("The first rectangle is inside the second one.")
    elif (x1 + l1/2) > (x2 + l2/2) and (y1 + w1/2) > (y2 + w2/2):
        turtle.write("The second rectangle is inside the first one.")
    else:
        turtle.write("The two rectangles overlap.")
elif d > r1+r2:
    turtle.write("The two rectangles do not overlap.")
        
x1_left = x1 - w1 / 2
x1_right = x1 + w1 / 2
y1_top = y1 + h1 / 2
y1_bottom = y1 - h1 / 2

x2_left = x2 - w2 / 2
x2_right = x2 + w2 / 2
y2_top = y2 + h2 / 2
y2_bottom = y2 - h2 / 2

# Check for overlap or containment
if x1_left <= x2_right and x1_right >= x2_left and y1_bottom <= y2_top and y1_top >= y2_bottom:
    if w1 < w2 and h1 < h2:
        turtle.write("The first rectangle is inside the second one.")
    elif w1 > w2 and h1 > h2:
        turtle.write("The second rectangle is inside the first one.")
    else:
        turtle.write("The two rectangles overlap.")
else:
    turtle.write("The two rectangles do not overlap.")
    
def rectangles_overlap(x1, y1, w1, h1, x2, y2, w2, h2):
    # Calculate the coordinates of the four corners of each rectangle
    x1_left = x1 - w1 / 2
    x1_right = x1 + w1 / 2
    y1_top = y1 + h1 / 2
    y1_bottom = y1 - h1 / 2

    x2_left = x2 - w2 / 2
    x2_right = x2 + w2 / 2
    y2_top = y2 + h2 / 2
    y2_bottom = y2 - h2 / 2

    # Check for overlap or containment
    if x1_left <= x2_right and x1_right >= x2_left and y1_bottom <= y2_top and y1_top >= y2_bottom:
        if w1 <= w2 and h1 <= h2:
            return "The first rectangle is inside the second one."
        elif w1 >= w2 and h1 >= h2:
            return "The second rectangle is inside the first one."
        else:
            return "The two rectangles overlap."
    else:
        return "The two rectangles do not overlap."