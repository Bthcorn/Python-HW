# n = 5

# for i in range(1, 2 * n):
#     if i <= n:
#         for j in range(i):
#             print('*', end='')
#         print()
#     else:
#         for j in range(2 * n - i):
#             print('*', end='')
#         print()

n = 5
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
