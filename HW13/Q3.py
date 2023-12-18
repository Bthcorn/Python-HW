def perm2(t, start=0):
    if start >= len(t):
        return

    for i in t:
        if t[start] != i:
            print((t[start], i))

    perm2(t, start + 1)

t = (1, 2, 3)
perm2(t)


def perm3(t, current=None):
    if current is None:
        current = []

    if len(current) == 3:
        print(tuple(current))
        return

    for num in t:
        if num not in current:
            current.append(num)
            perm3(t, current)
            current.pop()
t = (1, 2, 3, 4)
perm3(t)

def perm(t, n, current=None):
    if current is None:
        current = []

    if len(current) == n:
        print(tuple(current))
        return

    for num in t:
        if num not in current:
            current.append(num)
            perm3(t, current)
            current.pop()
            
perm((1, 2, 3), 3)