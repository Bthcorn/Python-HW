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