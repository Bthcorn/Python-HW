# Question 1
import turtle as t


def time24To12hour(time):
    time_list = time.split(":")
    con_to_num = []
    con_to_str = []
    for i in time_list:
        con_to_num.append(int(i))
    con_to_num

    if con_to_num[0] > 12:
        con_to_num[0] -= 12
        for j in con_to_num:
            con_to_str.append(str(j))
        new_time = ":".join(con_to_str)
    else:
        con_to_num = time_list
    print(f"\"{new_time} PM\"")


time24To12hour("23:24")
time24To12hour("20:30")
# ===========================================
# Question 2
x = -80
y = 80
l = 30
day = ["Mo", "Tu", "We", "Th", "Fr", "Sa", "Su"]
wn = t.Screen()
wn.tracer(0)
screen = t.Screen()
screen.screensize(2000, 10000)
current_day = 1  # Initialize the current day number
month_end = [31, 28, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31]
month_start = [6, 2, 2, 5, 0, 3, 5, 1, 4, 6, 2, 4]
month = ["January", "Febuary", "March", "April", "May", "June",
         "July", "August", "September", "October", "November", "December"]


def calendar_of_2023(n):
    global x, y, l, current_day
    t.speed(0.5)
    t.penup()
    t.goto(x, y)
    t.pendown()
    t.fd(210)
    t.rt(90)
    t.fd(l)
    t.rt(90)
    t.fd(105)
    t.write(f" {month[n-1]} 2023", font=("Arial", 12), align="center")
    t.fd(105)
    t.rt(90)
    t.fd(l)
    t.rt(90)
    t.lt(90)
    y -= l
    for i in range(0, 7):  # row
        t.penup()
        t.goto(x, y)
        t.pendown()
        if i == 0:
            for j in range(0, 7):  # column
                t.goto(x, y)
                t.pendown()
                for k in range(4):  # each square
                    if i == 0:
                        t.pendown()
                        t.rt(90)
                        if k == 3:
                            t.write(f" {day[j]}", font=("Arial", 12),
                                    align="left")  # create days
                        t.fd(l)
                x += l
            t.penup()
            x = -80
            y -= l
        elif i == 1:
            current_day = 1
            for j in range(0, 7):  # column
                t.goto(x, y)
                t.pendown()
                for k in range(4):
                    t.pendown()
                    t.rt(90)
                    # if current_month == 12:
                    #     break
                    if k == 3 and (month_start[n-1] <= j <= 7):
                        t.write(f" {current_day}", font=(
                            "Arial", 12), align="left")
                        current_day += 1
                    t.fd(l)
                x += l
            t.penup()
            x = -80
            y -= l
        elif i > 1:
            for j in range(0, 7):  # column
                t.penup()
                t.goto(x, y)
                t.pendown()
                for k in range(4):
                    t.pendown()
                    t.rt(90)
                    if k == 3:
                        if current_day == 1:
                            t.fd(l)
                            break
                        if current_day <= month_end[n-1]:
                            t.write(f" {current_day}", font=(
                                "Arial", 12), align="left")
                            current_day += 1
                            if current_day > month_end[n-1]:
                                current_day = 1
                    t.fd(l)
                x += l
            t.penup()
            x = -80
            y -= l
    t.done()


calendar_of_2023(8)
# ===========================================
# Question 3
num = int(input("Enter a number: "))

one_to_10 = ["zero", "one", "two", "three", "four", "five",
             "six", "seven", "eight", "nine"]
ten_to_19 = ["ten", "eleven", "twelve", "thirteen", "fourteen",
             "fifteen", "sixteen", "seventeen", "eighteen", "nineteen"]
more_or_20 = ["twenty", "thirty", "forty", "fifty",
              "sixty", "seventy", "eighty", "ninety"]

ten = ""
word = []
if num < 0 or num > 999:
    raise ValueError("Please input a number in range 1-999")

if 0 <= num < 10:
    ten += one_to_10[num]
    word.append(ten)
elif 10 <= num <= 19:
    ten += ten_to_19[num % 10]
    word.append(ten)
elif 19 < num < 100:
    ten += more_or_20[num % 100 // 10 - 2]
    ten += "-"
    ten += one_to_10[num % 10]
    word.append(ten)
elif num >= 100 and num <= 999:
    word.append(one_to_10[num // 100])
    word.append("hundred")
    if 0 < num % 100 < 10:
        ten += "and "
        ten += one_to_10[num % 10]
    elif 10 <= num % 100 < 20:
        ten += "and "
        ten += ten_to_19[num % 10]
    elif num % 100 >= 20:
        ten += "and "
        ten += more_or_20[num % 100 // 10 - 2]
        if num % 10 >= 1:
            ten += "-"
            ten += one_to_10[num % 10]
    word.append(ten)
else:
    word.append("I don't know")

print(" ".join(word))
# ===========================================
# Question 4
money = int(input("Input your amount of money: "))

notes_coins = [1000, 500, 100, 50, 20, 10, 5, 2, 1]
if money < 0:
    raise ValueError("Please input the correct value.")

for value in notes_coins:
    count = money // value
    money %= value
    if count != 0:
        if value >= 20:
            print(f"{value}-Baht notes: {count}")
        else:
            print(f"{value}-Baht coins: {count}")
# ===========================================
# Question 5


def reverse(input):
    num = list(str(input))
    num.reverse()
    new_num = int("".join(num))
    print(new_num)


reverse(3456)
# ===========================================
