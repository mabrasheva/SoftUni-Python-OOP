def fibonacci():
    first = 0
    yield first
    second = 1
    yield second
    while True:
        result = first + second
        yield result
        first, second = second, result


generator = fibonacci()
for i in range(5):
    print(next(generator))

print()

generator = fibonacci()
for i in range(1):
    print(next(generator))
