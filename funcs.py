def foo(a, b, *args, **kwargs):
    print(a, b)
    for i in args:
        print(i)

    for i in kwargs:
        print(i, kwargs[i])


foo('abc', 42, 2, 1, 9, 5, 0, age=20, bro_age=15)