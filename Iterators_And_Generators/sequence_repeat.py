class sequence_repeat:
    def __init__(self, sequence: str, number: int):
        self.sequence = sequence
        self.number = number
        self.iterations = 0

    def __iter__(self):
        return self

    def __next__(self):
        while self.iterations < self.number:
            current_index = self.iterations % len(self.sequence)
            self.iterations += 1
            return self.sequence[current_index]
        raise StopIteration


result = sequence_repeat('abc', 5)
for item in result:
    print(item, end='')

print()

result = sequence_repeat('I Love Python', 3)
for item in result:
    print(item, end='')
