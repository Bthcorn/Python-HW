import turtle
from turtle import *

text = input("Enter some text: ")
letter_count = {}

for char in text:
    if char.isalpha():
        if char in letter_count:
            letter_count[char] += 1
        else:
            letter_count[char] = 1
max = 0
for letter, count in letter_count.items():
    if count > max:
        max = count

lt(90)
fd(20*max)
stamp()
bk(20*max)
rt(90)
for letter, count in letter_count.items():
    fd(20)
    lt(90)
    fd(20*count)
    rt(90)
    fd(10)
    rt(90)
    fd(20*count)
    lt(90)
    bk(10)
    pu()
    rt(90)
    fd(20)
    write(f"{letter}")
    bk(20)
    lt(90)
    pd()
    fd(10)
fd(20)
done()

    
