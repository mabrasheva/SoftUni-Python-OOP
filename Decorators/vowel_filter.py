def vowel_filter(function):
    def wrapper():
        vowels = "aeoui"
        return [letter for letter in function() if letter.lower() in vowels]

    return wrapper


@vowel_filter
def get_letters():
    return ["a", "b", "c", "d", "e"]


print(get_letters())
