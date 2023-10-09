n = int(input("Enter a integer: "))
if n <= 0:
    raise ValueError("Please input integer greater than or equal to 1!")  

while n > 0:
    print('*')
    for i in range(1, n):
        for j in range(0, i + 1):
            print('*', end='')
        print()
    for i in range(n, 1, -1):
        if i < 2*n-1:
            for j in range(i, 1, -1):
                print('*', end='')
            print()
        elif i >= 2*n-1 :
            for j in range(i, 1, -1):
                print('*', end='')
            print(end='')
    n -= 1