class Integer:
    def __init__(self, value: int):
        self.value = value

    @classmethod
    def from_float(cls, float_value):
        if not isinstance(float_value, float):
            return "value is not a float"
        return cls(int(float_value))

    @classmethod
    def from_roman(cls, value):
        roman_value = {'I': 1, 'V': 5, 'X': 10, 'L': 50, 'C': 100, 'D': 500, 'M': 1000}
        int_value = 0
        for i in range(len(value)):
            if i > 0 and roman_value[value[i]] > roman_value[value[i - 1]]:
                int_value += roman_value[value[i]] - 2 * roman_value[value[i - 1]]
            else:
                int_value += roman_value[value[i]]
        return cls(int_value)

    @classmethod
    def from_string(cls, value):
        if isinstance(value, str) and isinstance(int(value), int):
            return cls(int(value))
        else:
            return "wrong type"


first_num = Integer(10)
print(first_num.value)

second_num = Integer.from_roman("IV")
print(second_num.value)

print(Integer.from_float("2.6"))
print(Integer.from_string(2.6))
