import functools


def my_decorator(func):

    @functools.wraps(func)
    def wrapper(*args, **kwargs):
        print('start')
        result = func(*args, **kwargs)
        print('end')
        return result
    return wrapper


@my_decorator
def add_five(x):
    return x + 5


summm = add_five(10)
print(summm)
