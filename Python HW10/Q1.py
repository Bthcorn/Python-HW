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
