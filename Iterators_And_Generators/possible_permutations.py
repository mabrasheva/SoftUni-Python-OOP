from itertools import permutations


def possible_permutations(integers_list: list):
    result = permutations(integers_list)
    for perm in result:
        yield list(perm)


[print(n) for n in possible_permutations([1, 2, 3])]
print()
[print(n) for n in possible_permutations([1])]
