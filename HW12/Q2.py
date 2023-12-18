dict1 = {'a':'p', 'b':'r', 'c':'q', 'd':'p', 'e':'s'}
dict2 = {'p':'1', 'q':'2', 'r':'3'}

def composite(dict1, dict2):
    new_dict = {}
    for key1, value1 in dict1.items():
        for key2, value2 in dict2.items():
            if value1 == key2:
                new_dict[key1] = value2
    return new_dict

print(composite(dict1, dict2))