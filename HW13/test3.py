def perm2(tup):
    if len(tup) == 0:
        return ([()], 1)
    else:
        ntup = []
        total_permutations = 0
        for i in range(len(tup)):
            rest_permutations, count = perm2(tup[:i] + tup[i + 1:])
            total_permutations += count
            for p in rest_permutations:
                ntup.append((tup[i],) + p)
        return (ntup, total_permutations)

result, count = perm2((1, 2, 3))
print("Permutations:", result)
print("Total Permutations Count:", count)
