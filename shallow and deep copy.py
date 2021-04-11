import copy

org = [1, 2, 3, 4, 5, 6]
cpy = copy.copy(org)

cpy[2] = 1
print(org, cpy)

org2 = [1, 2, 3, 4, 5, [6, 3, 1, 5, 6, 5]]
cpy2 = copy.deepcopy(org2)

cpy2[2] = 1
cpy2[5][0] = 0
print(org2, cpy2)
