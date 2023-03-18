from project.computer_types.computer import Computer


class Laptop(Computer):
    AVAILABLE_PROCESSORS = {
        "AMD Ryzen 9 5950X": 900,
        "Intel Core i9-11900H": 1050,
        "Apple M1 Pro": 1200
    }
    POSSIBLE_RAM = [2, 4, 8, 16, 32, 64]

    def configure_computer(self, processor: str, ram: int):

        if processor not in Laptop.AVAILABLE_PROCESSORS:
            raise ValueError(f'{processor} is not compatible with laptop {self.manufacturer} {self.model}!')
        if ram not in Laptop.POSSIBLE_RAM:
            raise ValueError(f'{ram}GB RAM is not compatible with laptop {self.manufacturer} {self.model}!')
        self.processor = processor
        self.ram = ram
        self.price += Laptop.AVAILABLE_PROCESSORS[processor] + self.find_power_of_two(ram) * 100
        return f'Created {self.manufacturer} {self.model} with {self.processor} and {self.ram}GB RAM for {self.price}$.'
