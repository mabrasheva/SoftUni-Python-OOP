from project.car.muscle_car import MuscleCar
from project.car.sports_car import SportsCar
from project.driver import Driver
from project.race import Race


class Controller:
    def __init__(self):
        self.cars = []  # will contain all cars (objects)
        self.drivers = []  # will contain all drivers (objects)
        self.races = []  # will contain all races (objects)

    def __find_driver_by_name(self, name):
        for driver in self.drivers:
            if driver.name == name:
                return driver

    def __find_race_by_name(self, name):
        for race in self.races:
            if race.name == name:
                return race

    def __find_driver_by_car(self, car):
        for driver in self.drivers:
            if driver.car == car:
                return driver

    def create_car(self, car_type: str, model: str, speed_limit: int):
        for car in self.cars:
            if car.model == model:
                return f"Car {model} is already created!"
        if car_type == "MuscleCar":
            new_car = MuscleCar(model, speed_limit)
            self.cars.append(new_car)
            return f"{car_type} {model} is created."
        elif car_type == "SportsCar":
            new_car = SportsCar(model, speed_limit)
            self.cars.append(new_car)
            return f"{car_type} {model} is created."

    def create_driver(self, driver_name: str):
        driver = self.__find_driver_by_name(driver_name)
        if driver:
            raise Exception(f"Driver {driver_name} is already created!")
        self.drivers.append(Driver(driver_name))
        return f"Driver {driver_name} is created."

    def create_race(self, race_name: str):
        race = self.__find_race_by_name(race_name)
        if race:
            raise Exception(f"Race {race_name} is already created!")
        self.races.append(Race(race_name))
        return f"Race {race_name} is created."

    def add_car_to_driver(self, driver_name: str, car_type: str):
        driver = self.__find_driver_by_name(driver_name)
        if driver is None:
            raise Exception(f"Driver {driver_name} could not be found!")

        for car in reversed(self.cars):
            if car.__class__.__name__ == car_type and not car.is_taken:
                if driver.car:
                    old_car_model = driver.car.model
                    driver.car.is_taken = False
                    driver.car = car
                    car.is_taken = True
                    return f"Driver {driver_name} changed his car from {old_car_model} to {car.model}."
                driver.car = car
                car.is_taken = True
                return f"Driver {driver_name} chose the car {car.model}."
        raise Exception(f"Car {car_type} could not be found!")

    def add_driver_to_race(self, race_name: str, driver_name: str):
        race = self.__find_race_by_name(race_name)
        if race is None:
            raise Exception(f"Race {race_name} could not be found!")
        driver = self.__find_driver_by_name(driver_name)
        if driver is None:
            raise Exception(f"Driver {driver_name} could not be found!")
        if driver.car is None:
            raise Exception(f"Driver {driver_name} could not participate in the race!")
        if driver in race.drivers:
            return f"Driver {driver_name} is already added in {race_name} race."
        race.drivers.append(driver)
        return f"Driver {driver_name} added in {race_name} race."

    def start_race(self, race_name: str):
        race = self.__find_race_by_name(race_name)
        if race is None:
            raise Exception(f"Race {race_name} could not be found!")
        if len(race.drivers) < 3:
            raise Exception(f"Race {race_name} cannot start with less than 3 participants!")

        sorted_cars = sorted(self.cars, key=lambda x: -x.speed_limit)
        result = []
        for car in sorted_cars[0:3]:
            driver = self.__find_driver_by_car(car)
            driver.number_of_wins += 1
            result.append(f"Driver {driver.name} wins the {race_name} race with a speed of {car.speed_limit}.")
        return "\n".join(result)
