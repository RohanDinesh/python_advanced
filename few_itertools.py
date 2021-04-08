from itertools import product, permutations, combinations, combinations_with_replacement, accumulate, groupby, count, \
    cycle, repeat
from timeit import default_timer as ti
a = [1, 2, 3, 4]
b = [4, 5, 6]
x = [7, 8, 9]
c = product(a, b)
print(list(c))
# for key, values in c:
#    print(key, values)
for i in c:
    print(i)

print(list(permutations(a)))
print(list(combinations(b, 2)))
print(list(combinations_with_replacement(c, 4)))
print(list(accumulate(a, func=max)))


def smaller_than_3(x):
    if x < 3:
        return True
    else:
        return False


grp = groupby(a, smaller_than_3)
print("groupby fun:\n")
#print(list(grp))

for key, value in grp:
    print(key, list(value))


count=0
start = ti()
for i in cycle(a):
    print(i)
    count+=1

    if count==10 :
        break
end = ti()
print("time taken for cycle fun: "+str(end-start))


start = ti()
for i in repeat(5, 10):
    print(i)

end = ti()
print("time taken for cycle fun: "+str(end-start))

