def squares(number: int):
    current_number = 1
    while current_number <= number:
        yield current_number ** 2
        current_number += 1


print(list(squares(5)))
