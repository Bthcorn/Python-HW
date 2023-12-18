def product(*args):
    new_set = []
    for i in args[0]:
        new_set.append((i,))
        
    for k in args[1:]:
        another_set = [] 
        for j in new_set:
            for m in k:
                another_set.append(j + (m,))
        new_set = another_set
    return new_set

s1 = set([1, 2, 3])
s2 = set(['p', 'q'])
s3 = set(['a', 'b', 'c'])

set(product(s1, s2, s3))
set(product(s1, s2))
set(product(s1))

