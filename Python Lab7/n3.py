import turtle as t
    
def intersect(self, rec):
    if (rec.__x < self.__x + self.__width and
        rec.__x + rec.__width > self.__x and
        rec.__y - rec.__height < self.__y and
        rec.__y > self.__y - self.__height):
        
        intersection_x = max(self.__x, rec.__x)
        intersection_y = min(self.__y, rec.__y)
        intersection_width = min(self.__x + self.__width, rec.__x + rec.__width) - intersection_x
        intersection_height = abs(max(self.__y - self.__height, rec.__y - rec.__height) - intersection_y)
        
        t.penup()
        t.goto(intersection_x, intersection_y)
        t.pendown()
        t.fd(intersection_width)
        t.rt(90)
        t.fd(intersection_height)
        t.rt(90)
        t.fd(intersection_width)
        t.rt(90)
        t.fd(intersection_height)
    else:
        return None

# Create a Turtle object
t.speed(1)
rectangle1 = Rectangle(100, 100, 150, 100)
rectangle2 = Rectangle(150, 150, 100, 150)


rectangle1.intersect(rectangle2)

t.done()



