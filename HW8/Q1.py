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