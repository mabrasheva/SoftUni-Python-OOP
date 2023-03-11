class vowels:
    def __init__(self, text: str):
        possible_vowels = 'AEIOUYaeiouy'
        self.text = text
        self.vowels_list = [char for char in text if char in possible_vowels]
        self.start = 0
        self.end = len(self.vowels_list) - 1

    def __iter__(self):
        return self

    def __next__(self):
        while self.start <= self.end:
            index = self.start
            self.start += 1
            return self.vowels_list[index]
        raise StopIteration


my_string = vowels('Abcedifuty0o')
for char in my_string:
    print(char)
