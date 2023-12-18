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