a = input("enter value of a")


def check(b):
    if int(b) in range(1, 10):
        print('a is between 1-9')
    else:
        print('a is outside specified range')



check(a)
