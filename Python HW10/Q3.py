list1 = [3, 1, 2, 7]
list2 = [4, 1, 2, 5]

def my_union(list1, list2):
    new_list = []
    for i in list1:
        if not i in new_list:
            new_list.append(i)
    
    for j in list2:
        if not j in new_list:
            new_list.append(j)
    
    return new_list

def my_intersection(list1, list2):
    new_list = []
    for i in list1:
        if i in list2 and not i in new_list:
            new_list.append(i)
            
    for j in list2:
        if j in list1 and not j in new_list:
            new_list.append(j)
    
    return new_list

def my_difference(list1, list2):
    new_list = []
    for i in list1:
        if not i in list2 and not i in new_list:
            new_list.append(i)
            
    # for j in list2:
    #     if not j in list1 and not j in new_list:
    #         new_list.append(j)
    return new_list


print(my_union(list1, list2))
print(my_intersection(list1, list2))
print(my_difference(list1, list2))

