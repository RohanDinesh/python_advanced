from timeit import default_timer as ti

my_list = ['abc'] * 10

start = ti()
my_string = ''.join(my_list)

stop = ti()
print(stop - start)
print(my_string)
