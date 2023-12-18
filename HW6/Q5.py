def reverse(input):
    num = list(str(input))
    num.reverse()
    new_num = int("".join(num))
    print(new_num)

reverse(3456)
