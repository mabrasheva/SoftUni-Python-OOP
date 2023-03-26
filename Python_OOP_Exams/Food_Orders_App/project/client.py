class Client:
    def __init__(self, phone_number: str):
        self.phone_number = phone_number
        self.shopping_cart = []  # Will contain all meals (objects) added by the client.
        self.bill = 0.0  # Represents the total amount of money for all meals that the client has added to his shopping cart
        self.ordered_meals = {}

    @property
    def phone_number(self):
        return self.__phone_number

    @staticmethod
    def is_valid_phone_number(number: str):
        return number.startswith("0") and \
            len(number) == 10 and \
            all([True if char.isdigit() else False for char in number])

    @phone_number.setter
    def phone_number(self, value):
        if not self.is_valid_phone_number(value):
            raise ValueError("Invalid phone number!")
        self.__phone_number = value
