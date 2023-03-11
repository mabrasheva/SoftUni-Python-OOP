class custom_range:
    def __init__(self, start: int, end: int):
        self.start = start
        self.end = end

    def __iter__(self):
        return self

    def __next__(self):
        while self.start <= self.end:
            temp = self.start
            self.start += 1
            return temp
        raise StopIteration


one_to_ten = custom_range(1, 10)
for num in one_to_ten:
    print(num)
