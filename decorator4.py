import functools


def start_end_decorator(func):
    @functools.wraps(func)
    def wrapper(*args, **kwargs):
        print('start')
        result = func(*args, **kwargs)
        print('end')

    return wrapper


def debuggg(func): 
    @functools.wraps(func)
    def wrapper(*args, **kwargs):
        print(f"calling function: {func.__name__}")
        result = func(*args, **kwargs)
        print(f"it returned a result: {result}")
        return result

    return wrapper


@debuggg
@start_end_decorator
def say_hello(name):
    print(f"Hello {name}")


abc = say_hello("Rohan")
print(f"abc is {abc}")
