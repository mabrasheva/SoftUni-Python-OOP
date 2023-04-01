from project.horse_race import HorseRace
from project.horse_specification.appaloosa import Appaloosa
from project.horse_specification.thoroughbred import Thoroughbred
from project.jockey import Jockey


class HorseRaceApp:
    RACE_TYPES_CREATED = {"Winter": 0, "Spring": 0, "Autumn": 0, "Summer": 0}

    def __init__(self):
        self.horses = []  # An empty list that will contain all the horses (objects).
        self.jockeys = []  # An empty list that will contain all the jockeys (objects).
        self.horse_races = []  # An empty list that will contain all the horse races (objects).

    @staticmethod
    def __find_object_by_name(property_value, collection):
        for element in collection:
            if element.name == property_value:
                return element

    def __find_race_by_race_type(self, race_type_value):
        for race in self.horse_races:
            if race.race_type == race_type_value:
                return race

    def __find_horse_by_horse_type(self, horse_type):
        for horse in reversed(self.horses):
            if horse.__class__.__name__ == horse_type:
                return horse

    def add_horse(self, horse_type: str, horse_name: str, horse_speed: int):
        if self.__find_object_by_name(horse_name, self.horses) is not None:
            raise Exception(f"Horse {horse_name} has been already added!")
        if horse_type == "Appaloosa":
            new_horse = Appaloosa(horse_name, horse_speed)
            self.horses.append(new_horse)
        elif horse_type == "Thoroughbred":
            new_horse = Thoroughbred(horse_name, horse_speed)
            self.horses.append(new_horse)
        return f"{horse_type} horse {horse_name} is added."

    def add_jockey(self, jockey_name: str, age: int):
        if self.__find_object_by_name(jockey_name, self.jockeys) is not None:
            raise Exception(f"Jockey {jockey_name} has been already added!")
        new_jockey = Jockey(jockey_name, age)
        self.jockeys.append(new_jockey)
        return f"Jockey {jockey_name} is added."

    def create_horse_race(self, race_type: str):
        if race_type in self.RACE_TYPES_CREATED and self.RACE_TYPES_CREATED[race_type] != 0:
            raise Exception(f"Race {race_type} has been already created!")
        self.RACE_TYPES_CREATED[race_type] = 1
        new_race = HorseRace(race_type)
        self.horse_races.append(new_race)
        return f"Race {race_type} is created."

    def add_horse_to_jockey(self, jockey_name: str, horse_type: str):
        horse = self.__find_horse_by_horse_type(horse_type)
        jockey = self.__find_object_by_name(jockey_name, self.jockeys)

        if jockey is None:
            raise Exception(f"Jockey {jockey_name} could not be found!")
        if horse is None or horse.is_taken:
            raise Exception(f"Horse breed {horse_type} could not be found!")
        if jockey.horse:
            return f"Jockey {jockey_name} already has a horse."
        jockey.horse = horse
        horse.is_taken = True
        return f"Jockey {jockey_name} will ride the horse {horse.name}."

    def add_jockey_to_horse_race(self, race_type: str, jockey_name: str):
        race = self.__find_race_by_race_type(race_type)
        jockey = self.__find_object_by_name(jockey_name, self.jockeys)

        if race is None:
            raise Exception(f"Race {race_type} could not be found!")
        if jockey is None:
            raise Exception(f"Jockey {jockey_name} could not be found!")
        if jockey.horse is None:
            raise Exception(f"Jockey {jockey_name} cannot race without a horse!")
        if jockey in race.jockeys:
            return f"Jockey {jockey_name} has been already added to the {race_type} race."
        race.jockeys.append(jockey)
        return f"Jockey {jockey_name} added to the {race_type} race."

    def start_horse_race(self, race_type: str):
        race = self.__find_race_by_race_type(race_type)

        if race is None:
            raise Exception(f"Race {race_type} could not be found!")
        if len(race.jockeys) < 2:
            raise Exception(f"Horse race {race_type} needs at least two participants!")

        winner_horse_speed = 0
        winner_jockey_name = ""
        winner_horse_name = ""
        for jockey in race.jockeys:
            if jockey.horse.speed > winner_horse_speed:
                winner_horse_speed = jockey.horse.speed
                winner_jockey_name = jockey.name
                winner_horse_name = jockey.horse.name
        return f"The winner of the {race_type} race, with a speed of {winner_horse_speed}km/h is {winner_jockey_name}! Winner's horse: {winner_horse_name}."
