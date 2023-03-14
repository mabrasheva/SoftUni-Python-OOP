def cache(function_ref):
    def wrapper(number):
        if number not in wrapper.log:
            wrapper.log[number] = function_ref(number)
        return wrapper.log[number]

    wrapper.log = {}

    return wrapper


@cache
def fibonacci(n):
    if n < 2:
        return n
    else:
        return fibonacci(n - 1) + fibonacci(n - 2)


fibonacci(3)
print(fibonacci.log)
fibonacci(4)
print(fibonacci.log)
