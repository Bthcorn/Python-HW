def name_list():
    list = []
    i = 1
    while i >= 1:
        name = input(f"Enter name {i}:")
        if name == "":
            break
        list.append(name)
        i += 1
    return list
    
print(name_list())