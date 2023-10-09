def print_table(list1):
    for lt in list1:
        for i in lt:
            print(i, end="\t")
        print()
            
print_table([["X", "Y"], [0, 0], [10, 10], [200, 1000]])
print_table([
    ["ID", "Name", "Surname"],
    ["001", "Guido", "van Rossum"],
    ["002", "Donald", "Knuth"],
    ["003", "Gordon", "Moore"]
])
            