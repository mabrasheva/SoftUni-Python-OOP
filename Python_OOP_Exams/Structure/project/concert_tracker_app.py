from project.band import Band
from project.concert import Concert
from project.band_members.drummer import Drummer
from project.band_members.guitarist import Guitarist
from project.band_members.singer import Singer


class ConcertTrackerApp:
    VALID_MUSICIAN_TYPES = ["Guitarist", "Drummer", "Singer"]

    def __init__(self):
        self.bands = []
        self.musicians = []
        self.concerts = []

    def create_musician(self, musician_type: str, name: str, age: int):
        if musician_type not in self.VALID_MUSICIAN_TYPES:
            raise ValueError("Invalid musician type!")
        for musician in self.musicians:
            if name == musician.name:
                raise Exception(f"{name} is already a musician!")

        if musician_type == "Singer":
            new_musician = Singer(name, age)
            self.musicians.append(new_musician)

        elif musician_type == "Drummer":
            new_musician = Drummer(name, age)
            self.musicians.append(new_musician)

        elif musician_type == "Guitarist":
            new_musician = Guitarist(name, age)
            self.musicians.append(new_musician)

        return f"{name} is now a {musician_type}."

    def create_band(self, name: str):
        for band in self.bands:
            if name == band.name:
                raise Exception(f"{name} band is already created!")
        new_band = Band(name)
        self.bands.append(new_band)
        return f"{name} was created."

    def create_concert(self, genre: str, audience: int, ticket_price: float, expenses: float, place: str):
        for concert in self.concerts:
            if place == concert.place:
                raise Exception(f"{place} is already registered for {concert.genre} concert!")
        new_concert = Concert(genre, audience, ticket_price, expenses, place)
        self.concerts.append(new_concert)
        return f"{genre} concert in {place} was added."

    def __find_musician_by_name(self, name: str):
        for musician in self.musicians:
            if musician.name == name:
                return musician
        else:
            raise Exception(f"{name} isn't a musician!")

    def __find_band_by_name(self, name: str):
        for band in self.bands:
            if band.name == name:
                return band
        else:
            raise Exception(f"{name} isn't a band!")

    @staticmethod
    def __find_added_to_band_musician_by_name(band, name: str):
        for musician in band.members:
            if musician.name == name:
                return musician
        else:
            raise Exception(f"{name} isn't a member of {band.name}!")

    def add_musician_to_band(self, musician_name: str, band_name: str):
        musician = self.__find_musician_by_name(musician_name)
        band = self.__find_band_by_name(band_name)
        band.add_member(musician)
        return f"{musician_name} was added to {band_name}."

    def remove_musician_from_band(self, musician_name: str, band_name: str):
        band = self.__find_band_by_name(band_name)
        musician = self.__find_added_to_band_musician_by_name(band, musician_name)
        band.remove_member(musician)
        return f"{musician_name} was removed from {band_name}."

    def start_concert(self, concert_place: str, band_name: str):

        concert = None
        for con in self.concerts:
            if concert_place == con.place:
                concert = con
                break

        band = self.__find_band_by_name(band_name)

        band_members_types = {member.__class__.__name__ for member in band.members}
        if band_members_types != set(self.VALID_MUSICIAN_TYPES):
            raise Exception(f"{band_name} can't start the concert because it doesn't have enough members!")

        if concert.genre == "Rock":
            for member in band.members:
                if isinstance(member, Drummer):
                    if "play the drums with drumsticks" not in member.skills:
                        raise Exception(f"The {band_name} band is not ready to play at the concert!")
            for member in band.members:
                if isinstance(member, Singer):
                    if "sing high pitch notes" not in member.skills:
                        raise Exception(f"The {band_name} band is not ready to play at the concert!")
            for member in band.members:
                if isinstance(member, Guitarist):
                    if "play rock" not in member.skills:
                        raise Exception(f"The {band_name} band is not ready to play at the concert!")

        if concert.genre == "Metal":
            for member in band.members:
                if isinstance(member, Drummer):
                    if "play the drums with drumsticks" not in member.skills:
                        raise Exception(f"The {band_name} band is not ready to play at the concert!")
            for member in band.members:
                if isinstance(member, Singer):
                    if "sing low pitch notes" not in member.skills:
                        raise Exception(f"The {band_name} band is not ready to play at the concert!")
            for member in band.members:
                if isinstance(member, Guitarist):
                    if "play metal" not in member.skills:
                        raise Exception(f"The {band_name} band is not ready to play at the concert!")

        if concert.genre == "Jazz":
            for member in band.members:
                if isinstance(member, Drummer):
                    if "play the drums with drum brushes" not in member.skills:
                        raise Exception(f"The {band_name} band is not ready to play at the concert!")
            for member in band.members:
                if isinstance(member, Singer):
                    if "sing high pitch notes" not in member.skills or \
                            "sing low pitch notes" not in member.skills:
                        raise Exception(f"The {band_name} band is not ready to play at the concert!")
            for member in band.members:
                if isinstance(member, Guitarist):
                    if "play jazz" not in member.skills:
                        raise Exception(f"The {band_name} band is not ready to play at the concert!")

        profit = concert.audience * concert.ticket_price - concert.expenses
        return f"{band_name} gained {profit:.2f}$ from the {concert.genre} concert in {concert.place}."
