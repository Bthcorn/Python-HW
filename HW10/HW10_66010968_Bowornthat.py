# Question 1
import numpy as np
import matplotlib.pyplot as plt

def pie_chart(list1):
    dic = {}
    for i in list1:
        if i in dic:
            dic[i] += i
        else:
            dic[i] = 1
    labels1 = list(dic.keys())
    values = list(dic.values())
    y = np.array(values)
    plt.pie(y, labels=labels1)
    plt.show()

pie_chart([3, 1, 3, 3, 2, 3, 3, 2, 3, 2, 4, 3, 3, 3, 3, 4, 3, 4, 3, 3, 3, 4, 3])

# ======================================
# Question 2
def bubble_sort(list1):
    for i in range(len(list1)):
        swapped = False
        for j in range(len(list1)-1):
            if list1[j] > list1[j+1]:
                list1[j], list1[j+1] = list1[j+1], list1[j]
            swapped = True
        if swapped == False:
            break    
    return list1

print(bubble_sort([3, 2, 9, 7, 8]))
# ======================================
# Question 3
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

# ======================================
# Question 4
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
            
# ======================================
# Question 5
def isAnagram(text1, text2):
    if len(text1) != len(text2):
        return False
    
    for i in text1:
        anagram = False
        if i in text2:
            anagram = True
        if anagram == False:
            return anagram
    return anagram

print(isAnagram("silent", "listen"))
print(isAnagram("recital", "article"))
print(isAnagram("note", "notice"))
print(isAnagram("letter", "better"))
print(isAnagram("flower", "flour"))
# ======================================