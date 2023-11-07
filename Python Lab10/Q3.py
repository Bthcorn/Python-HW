def get_the_difference(list1, list2):
    list = []
    for i in list1:
        if not i in list2:
            list.append(i)
    
    for j in list2:
        if not j in list1:
            list.append(j)
    
    return list

print(get_the_difference([3,1,1,1,2,7], [4,1,1,2,2,5]))