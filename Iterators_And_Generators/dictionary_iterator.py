class dictionary_iter:
    def __init__(self, dictionary_object: dict):
        self.iterable = list(dictionary_object.items())
        self.iterations = len(dictionary_object)
        self.start_index = 0

    def __iter__(self):
        return self

    def __next__(self):
        while self.iterations > 0:
            self.current_index = self.start_index
            self.start_index += 1
            self.iterations -=1
            return self.iterable[self.current_index]
        raise StopIteration


result = dictionary_iter({1: "1", 2: "2"})
for x in result:
    print(x)

print()

result = dictionary_iter({"name": "Peter", "age": 24})
for x in result:
    print(x)
