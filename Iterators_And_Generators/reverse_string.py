def reverse_text(text: str):
    current_index = len(text) - 1
    end_index = 0
    while current_index >= end_index:
        yield text[current_index]
        current_index -= 1


for char in reverse_text("step"):
    print(char, end='')
