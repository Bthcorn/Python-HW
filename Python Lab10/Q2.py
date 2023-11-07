list1 = [3, 6, 6, 3, 7, 2, 0, 1, 5, 4]

# def remove_the_thirds(list):
#     count = 2
#     for i in list:
#         count += 1
#         if count % 3 == 0:
#             list.remove(i)
        
#     return list


# print(remove_the_thirds(list1))

def remove_every_third_element(input_list):
    index = 2 

    while index < len(input_list):
        del input_list[index]
        index += 2 

my_list = [3, 6, 6, 3, 7, 2, 0, 1, 5, 4]
remove_every_third_element(my_list)
print(my_list)  