n = int(input("Enter a number to find its square root: "))
if n < 0:
    raise ValueError("Please input number greater than or equal to 0!")  
guess = n/2
time = 5
while time < 8: 
    for i in range(time):
        temp = float(n/guess)
        guess = (guess + temp)/2
    print(time, "times approximation:",  format(guess, ".3f"))
    time += 1
    guess = n/2


