class Zoo:
    def __init__(self, name: str, budget: int, animal_capacity: int, worker_capacity: int):
        self.name = name
        self.__budget = budget
        self.__animal_capacity = animal_capacity
        self.__workers_capacity = worker_capacity
        self.animals = []
        self.workers = []

    def add_animal(self, animal, price):
        if len(self.animals) < self.__animal_capacity:
            if self.__budget >= price:
                self.animals.append(animal)
                self.__budget -= price
                return f"{animal.name} the {animal.__class__.__name__} added to the zoo"
            return "Not enough budget"
        return "Not enough space for animal"

    def hire_worker(self, worker):
        if len(self.workers) < self.__workers_capacity:
            self.workers.append(worker)
            return f"{worker.name} the {worker.__class__.__name__} hired successfully"
        return "Not enough space for worker"

    def fire_worker(self, worker_name):
        for worker in self.workers:
            if worker.name == worker_name:
                self.workers.remove(worker)
                return f"{worker_name} fired successfully"
        return f"There is no {worker_name} in the zoo"

    def pay_workers(self):
        sum_salaries = sum([worker.salary for worker in self.workers])
        if self.__budget >= sum_salaries:
            self.__budget -= sum_salaries
            return f"You payed your workers. They are happy. Budget left: {self.__budget}"
        return "You have no budget to pay your workers. They are unhappy"

    def tend_animals(self):
        total_sum_for_care = sum([animal.money_for_care for animal in self.animals])
        if self.__budget >= total_sum_for_care:
            self.__budget -= total_sum_for_care
            return f"You tended all the animals. They are happy. Budget left: {self.__budget}"
        return "You have no budget to tend the animals. They are unhappy."

    def profit(self, amount):
        self.__budget += amount

    def animals_status(self):
        result = f"You have {len(self.animals)} animals\n"
        amount_of_lions = len(list(filter(lambda animal: animal.__class__.__name__ == "Lion", self.animals)))
        amount_of_tigers = len(list(filter(lambda animal: animal.__class__.__name__ == "Tiger", self.animals)))
        amount_of_cheetahs = len(list(filter(lambda animal: animal.__class__.__name__ == "Cheetah", self.animals)))
        result += f"----- {amount_of_lions} Lions:\n"
        for animal in self.animals:
            if animal.__class__.__name__ == "Lion":
                result += f"{animal.__repr__()}\n"
        result += f"----- {amount_of_tigers} Tigers:\n"
        for animal in self.animals:
            if animal.__class__.__name__ == "Tiger":
                result += f"{animal.__repr__()}\n"
        result += f"----- {amount_of_cheetahs} Cheetahs:\n"
        for animal in self.animals:
            if animal.__class__.__name__ == "Cheetah":
                result += f"{animal.__repr__()}\n"
        return result.strip()

    def workers_status(self):
        result = f"You have {len(self.workers)} workers\n"
        amount_of_keepers = len(list(filter(lambda worker: worker.__class__.__name__ == "Keeper", self.workers)))
        amount_of_caretakers = len(list(filter(lambda worker: worker.__class__.__name__ == "Caretaker", self.workers)))
        amount_of_vets = len(list(filter(lambda worker: worker.__class__.__name__ == "Vet", self.workers)))
        result += f"----- {amount_of_keepers} Keepers:\n"
        for worker in self.workers:
            if worker.__class__.__name__ == "Keeper":
                result += f"{worker.__repr__()}\n"
        result += f"----- {amount_of_caretakers} Caretakers:\n"
        for worker in self.workers:
            if worker.__class__.__name__ == "Caretaker":
                result += f"{worker.__repr__()}\n"
        result += f"----- {amount_of_vets} Vets:\n"
        for worker in self.workers:
            if worker.__class__.__name__ == "Vet":
                result += f"{worker.__repr__()}\n"
        return result.strip()
