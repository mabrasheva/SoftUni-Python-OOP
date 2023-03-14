from functools import wraps


def logged(function):
    @wraps(function)
    def wrapper(*args, **kwargs):
        return f"you called {function.__name__}{args}\nit returned {function(*args, **kwargs)}"

    return wrapper


@logged
def func(*args):
    return 3 + len(args)


print(func(4, 4, 4))

print()


@logged
def sum_func(a, b):
    return a + b


print(sum_func(1, 4))
