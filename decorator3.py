import functools


def repeat_decorator(num_times):
    def decorator_r(func):
        @functools.wraps(func)
        def wrapper(*args, **kwargs):
            for _ in range(num_times):
                result = func(*args, **kwargs)
            return result

        return wrapper

    return decorator_r


@repeat_decorator(num_times=4)
def greet(name):
    print(f"Hello my name is {name}")


greet("Rohan")
