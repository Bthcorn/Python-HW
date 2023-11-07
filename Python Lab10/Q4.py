import numpy as np
import matplotlib.pyplot as plt

list1 = [1,2,2,1,3,4,6,5,3,4,5,6,4,3,5,4,5,3,4,4,3,3,4,3,3,4,4,4]
def histogram(list1):
    dic= {}
    for i in list1:
        if i in dic:
            dic[i] += 1
        else:
            dic[i] = 1
    
    courses = list(dic.keys())
    values = list(dic.values())
    
    # fig = plt.figure(figsize = (10, 5))
    plt.bar(courses, values, color ='blue',width = 0.4)
    plt.show()
  
histogram(list1)