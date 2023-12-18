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

# money = int(input("Input your amount 0f your money: "))

# num_of_1000_note = money // 1000
# remaining = money % 1000
# if num_of_1000_note != 0:
#     print("1000-Baht notes: ", num_of_1000_note)

# num_of_500_note = remaining // 500
# remaining = remaining % 500
# if num_of_500_note != 0:
#     print("500-Bath notes: ", num_of_500_note)

# num_of_100_note = remaining // 100
# remaining = remaining % 100
# if num_of_100_note != 0:
#     print("100-Bath notes: ", num_of_100_note)

# num_of_50_note = remaining // 50
# remaining = remaining % 50
# if num_of_50_note != 0:
#     print("50-Bath notes: ", num_of_50_note)

# num_of_20_note = remaining // 20
# remaining = remaining % 20
# if num_of_20_note != 0:
#     print("20-Bath notes: ", num_of_20_note)

# num_of_10_coin = remaining // 10
# remaining = remaining % 10
# if num_of_10_coin != 0:
#     print("10-Bath coins: ", num_of_10_coin)

# num_of_5_coin = remaining // 5 
# remaining = remaining % 5
# if num_of_5_coin != 0:
#     print("5-Bath coins: ", num_of_5_coin)

# num_of_2_coin = remaining // 2 
# remaining = remaining % 2
# if num_of_2_coin != 0:
#     print("2-Bath coins: ", num_of_2_coin)

# if remaining != 0:
#     print("1-Bath coins: ", remaining)