# def merge(list1, list2):
#     merged = [i for i in list1]
#     for i in list2:
#         for m in merged: 
#             if i < m: 
#                 merged.insert(merged.index(m), i)
#                 break
#             elif i > m and merged.index(m) == len(merged) - 1:
#                 merged.append(i)
#                 break
        

#     for i in merged:
#         print(i, end=" ")

# merge(list1, list2)
# try using while loop instedad comqpared each index 

list1 = [1,3,5,7,9]
list2 = [2,4,6,8,10]
list3 = [1,1,1,1,8,8,9,9,15,15,15]

def merge(list1, list2):
    i = 0
    j = 0
    nlist = []
    while i < len(list1) and j < len(list2):
        if list1[i] < list2[j]:
            nlist.append(list1[i])
            i += 1
        else:
            nlist.append(list2[j])
            j += 1
    
    while i < len(list1):
        nlist.append(list1[i])
        i += 1

    while j < len(list2):
        nlist.append(list2[j])
        j += 1
        
    return nlist

print(merge(list1, list2))