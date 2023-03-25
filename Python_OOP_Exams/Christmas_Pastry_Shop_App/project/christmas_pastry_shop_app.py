from project.booths.open_booth import OpenBooth
from project.booths.private_booth import PrivateBooth
from project.delicacies.gingerbread import Gingerbread
from project.delicacies.stolen import Stolen


class ChristmasPastryShopApp:
    VALID_DELICACY_TYPES = ["Gingerbread", "Stolen"]
    VALID_BOOTH_TYPES = ["Open Booth", "Private Booth"]

    def __init__(self):
        self.booths = []  # will contain all booths (objects) that are created.
        self.delicacies = []  # will contain all delicacies (objects) that are created.
        self.income = 0.0  # the total income of the pastry shop

    @staticmethod
    def __get_object_by_name(name, collection):
        for obj in collection:
            if obj.name == name:
                return obj

    def add_delicacy(self, type_delicacy: str, name: str, price: float):
        if self.__get_object_by_name(name, self.delicacies):
            raise Exception(f"{name} already exists!")
        if type_delicacy not in ChristmasPastryShopApp.VALID_DELICACY_TYPES:
            raise Exception(f"{type_delicacy} is not on our delicacy menu!")

        if type_delicacy == "Gingerbread":
            new_delicacy = Gingerbread(name, price)
            self.delicacies.append(new_delicacy)
        elif type_delicacy == "Stolen":
            new_delicacy = Stolen(name, price)
            self.delicacies.append(new_delicacy)

        return f"Added delicacy {name} - {type_delicacy} to the pastry shop."

    def add_booth(self, type_booth: str, booth_number: int, capacity: int):
        for booth in self.booths:
            if booth.booth_number == booth_number:
                raise Exception(f"Booth number {booth_number} already exists!")
        if type_booth not in ChristmasPastryShopApp.VALID_BOOTH_TYPES:
            raise Exception(f"{type_booth} is not a valid booth!")

        if type_booth == "Open Booth":
            new_booth = OpenBooth(booth_number, capacity)
            self.booths.append(new_booth)
        elif type_booth == "Private Booth":
            new_booth = PrivateBooth(booth_number, capacity)
            self.booths.append(new_booth)

        return f"Added booth number {booth_number} in the pastry shop."

    def reserve_booth(self, number_of_people: int):
        for booth in self.booths:
            if not booth.is_reserved and booth.capacity >= number_of_people:
                booth.reserve(number_of_people)
                return f"Booth {booth.booth_number} has been reserved for {number_of_people} people."
        raise Exception(f"No available booth for {number_of_people} people!")

    def order_delicacy(self, booth_number: int, delicacy_name: str):
        delicacy_to_order = self.__get_object_by_name(delicacy_name, self.delicacies)
        if not delicacy_to_order:
            raise Exception(f"No {delicacy_name} in the pastry shop!")

        for booth in self.booths:
            if booth.booth_number == booth_number:
                booth.delicacy_orders.append(delicacy_to_order)
                return f"Booth {booth_number} ordered {delicacy_name}."

        raise Exception(f"Could not find booth {booth_number}!")

    def leave_booth(self, booth_number: int):
        # Finds the booth with the same booth's number (the booth's number will always be valid).
        booth = [booth for booth in self.booths if booth.booth_number == booth_number][0]

        # Calculates the bill for that booth taking the price for reservation and all the price of all orders.
        # The bill is added to the pastry shop's total income.
        price_of_all_orders = 0
        for delicacy in booth.delicacy_orders:
            price_of_all_orders += delicacy.price
        booth_bill = booth.price_for_reservation + price_of_all_orders
        self.income += booth_bill

        # Removes all the ordered delicacies, frees the booth, and sets the price for reservation to 0.
        booth.delicacy_orders = []
        booth.is_reserved = False
        booth.price_for_reservation = 0

        result = f"Booth {booth_number}:\n"
        result += f"Bill: {booth_bill:.2f}lv."
        return result

    def get_income(self):
        return f"Income: {self.income:.2f}lv."
