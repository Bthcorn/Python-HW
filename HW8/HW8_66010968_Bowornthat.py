# Question 1
number = eval(input("Enter an integer: "))
if number == 0:
    print("It is 0.")
elif number < 0:
    print("It is negative.")
else:
    sum = 0
    string =""
    while number >= 1:
        if number % 2 == 0:
            number = number // 2
            string += "0"
        elif number % 2 != 0:
            number = number // 2
            string += "1"
    
    binary = string[::-1]
    for i in range(len(binary)):
        sum += (2**(len(binary) - (i+1)))*int(binary[i])
    print(binary)
    print(sum)
# ==================================
# Question 2
text = input("Enter some text: ")
letter_count = {}

for char in text:
    if char.isalpha():
        if char in letter_count:
            letter_count[char] += 1
        else:
            letter_count[char] = 1

print("-- Character Frequency Table --\nchar\tpercentage (character count / string length)")       
for letter, count in letter_count.items():
    print(f"{letter}\t{count*100/len(text):.2f} %")
# ==================================
# Question 3
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
# ==================================
# Question 4
digit = input("Enter the first 9 digits of an ISBN-10 as a string: ")
sum = 0

for i in range(len(digit)):
    sum += int(digit[i])*(i+1)
d10 = sum % 11

if d10 == 10:
    digit += "X"
else:
    digit += str(d10)
    
print(f"Your ISBN-10 number is {digit}")
# ==================================

