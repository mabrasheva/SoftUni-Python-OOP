from project.client import Client
from project.meals.meal import Meal


class FoodOrdersApp:
    POSSIBLE_MEALS = ["Starter", "MainDish", "Dessert"]

    def __init__(self):
        self.menu = []  # will contain all the meals (objects)
        self.clients_list = []  # will contain all the clients (objects)
        self.receipt_id = 0

    def __find_client_by_phone_number(self, number):
        for client in self.clients_list:
            if client.phone_number == number:
                return client

    def register_client(self, client_phone_number: str):
        if self.__find_client_by_phone_number(client_phone_number):
            raise Exception("The client has already been registered!")
        new_client = Client(client_phone_number)
        self.clients_list.append(new_client)
        return f"Client {client_phone_number} registered successfully."

    def add_meals_to_menu(self, *meals: Meal):
        for meal in meals:
            if meal.__class__.__name__ in FoodOrdersApp.POSSIBLE_MEALS:
                self.menu.append(meal)

    def __menu_is_ready(self):
        if len(self.menu) < 5:
            raise Exception("The menu is not ready!")

    def show_menu(self):
        self.__menu_is_ready()
        result = ""
        for meal in self.menu:
            result += meal.details() + "\n"
        return result.strip()

    def add_meals_to_shopping_cart(self, client_phone_number: str, **meal_names_and_quantity):
        self.__menu_is_ready()
        client = self.__find_client_by_phone_number(client_phone_number)
        if not client:
            self.register_client(client_phone_number)
            client = self.__find_client_by_phone_number(client_phone_number)
        meals_to_order = []
        current_bill = 0

        for meal_name, meal_quantity in meal_names_and_quantity.items():
            for meal in self.menu:
                if meal.name == meal_name:
                    if meal.quantity >= meal_quantity:
                        meals_to_order.append(meal)
                        current_bill += meal.price * meal_quantity
                        break
                    else:
                        raise Exception(f"Not enough quantity of {type(meal).__name__}: {meal_name}!")
            else:
                raise Exception(f"{meal_name} is not on the menu!")

        client.shopping_cart.extend(meals_to_order)
        client.bill += current_bill

        for meal_name, meal_quantity in meal_names_and_quantity.items():
            if meal_name not in client.ordered_meals:
                client.ordered_meals[meal_name] = 0
            client.ordered_meals[meal_name] += meal_quantity
            for meal in self.menu:
                if meal.name == meal_name:
                    meal.quantity -= meal_quantity

        return f"Client {client_phone_number} " \
               f"successfully ordered {', '.join(meal.name for meal in client.shopping_cart)} " \
               f"for {client.bill:.2f}lv."

    @staticmethod
    def __shopping_cart_is_not_empty(client):
        if len(client.shopping_cart) == 0:
            raise Exception("There are no ordered meals!")
        return True

    def cancel_order(self, client_phone_number: str):

        client = self.__find_client_by_phone_number(client_phone_number)

        if self.__shopping_cart_is_not_empty(client):

            for meal_name, meal_quantity in client.ordered_meals.items():
                for meal in self.menu:
                    if meal.name == meal_name:
                        meal.quantity += meal_quantity

            client.shopping_cart = []
            client.bill = 0
            client.ordered_meals = {}

            return f"Client {client_phone_number} successfully canceled his order."

    def finish_order(self, client_phone_number: str):
        client = self.__find_client_by_phone_number(client_phone_number)
        if self.__shopping_cart_is_not_empty(client):
            client.shopping_cart = []
            paid_bill = client.bill
            client.bill = 0
            self.receipt_id += 1
            client.ordered_meals = {}
            return f"Receipt #{self.receipt_id} with total amount of {paid_bill:.2f} was successfully paid for {client_phone_number}."

    def __str__(self):
        return f"Food Orders App has {len(self.menu)} meals on the menu and {len(self.clients_list)} clients."
