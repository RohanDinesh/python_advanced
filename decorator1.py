def print_name_decorator(func):
    def wrapper():
        print('start')
        func()
        print('stop')

    return wrapper


@print_name_decorator
def print_name():
    print("Hello Rohan")


# print_name = print_name_decorator(print_name)

print_name()
