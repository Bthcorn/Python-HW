def print_btree(node, depth= 0):     
    if isinstance(node, list):
        if depth > 0:
            print("." * depth + str(node[0]))
        else:
            print(node[0])
        for child in node[:][1]:
            print_btree(child, depth + 1)
    else:
        print("." * depth + str(node))
        
list1 = [1, [[11,[111, 112]], [12, [121, [122, [1221, 1222]]]]]]
print_btree(list1, 0)