from project.supply.supply import Supply


class Drink(Supply):
    ENERGY = 15

    def __init__(self, name: str):
        super().__init__(name, Drink.ENERGY)

    def details(self):
        return f"Drink: {self.name}, {self.energy}"
