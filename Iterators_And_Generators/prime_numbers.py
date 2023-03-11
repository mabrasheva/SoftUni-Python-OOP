def get_primes(integers_list: list):
    def is_prime(number):
        if number <= 1:
            return False
        for i in range(2, number):
            if number % i == 0:
                return False
        return True

    for number in integers_list:
        if is_prime(number):
            yield number


print(list(get_primes([2, 4, 3, 5, 6, 9, 1, 0])))
print()
print(list(get_primes([-2, 0, 0, 1, 1, 0])))
