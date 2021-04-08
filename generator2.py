def count_down(num):
    print('starting')

    while num > 0:
        yield num
        num -= 1


cd = count_down(10)

for i in cd:
    print(i)
