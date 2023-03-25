from unittest import TestCase, main

from project.band import Band
from project.band_members.drummer import Drummer
from project.band_members.guitarist import Guitarist
from project.band_members.singer import Singer
from project.concert import Concert
from project.concert_tracker_app import ConcertTrackerApp


class MusicianTests(TestCase):
    MUSICIAN_NAME = "TEST NAME"
    MUSICIAN_AGE = 16
    DRUMMER_SKILL = "read sheet music"
    GUITARIST_SKILL = "play metal"
    SINGER_SKILL = "sing high pitch notes"

    def setUp(self) -> None:
        self.guitarist = Guitarist(self.MUSICIAN_NAME, self.MUSICIAN_AGE)
        self.drummer = Drummer(self.MUSICIAN_NAME, self.MUSICIAN_AGE)
        self.singer = Singer(self.MUSICIAN_NAME, self.MUSICIAN_AGE)

    def test_musician_empty_name_raises(self):
        with self.assertRaises(ValueError) as error:
            Guitarist("", 20)
        self.assertEqual("Musician name cannot be empty!", str(error.exception))

    def test_musician_age_less_than_16_raises(self):
        with self.assertRaises(ValueError) as error:
            Guitarist("TestName", 15)
        self.assertEqual("Musicians should be at least 16 years old!", str(error.exception))

    def test_musician_age_initialize_properly_at_least_age_16(self):
        self.assertEqual(16, self.guitarist.age)

        guitarist = Guitarist("TestName", 17)
        self.assertEqual(17, guitarist.age)





    def test_musician_learn_new_skill_successfully(self):
        self.assertEqual(f"{self.MUSICIAN_NAME} learned to {self.DRUMMER_SKILL}.",
                         self.drummer.learn_new_skill(self.DRUMMER_SKILL))
        self.assertEqual([self.DRUMMER_SKILL], self.drummer.skills)

        self.assertEqual(f"{self.MUSICIAN_NAME} learned to {self.GUITARIST_SKILL}.",
                         self.guitarist.learn_new_skill(self.GUITARIST_SKILL))
        self.assertEqual([self.GUITARIST_SKILL], self.guitarist.skills)

        self.assertEqual(f"{self.MUSICIAN_NAME} learned to {self.SINGER_SKILL}.",
                         self.singer.learn_new_skill(self.SINGER_SKILL))
        self.assertEqual([self.SINGER_SKILL], self.singer.skills)

    def test_musician_learn_new_skill_not_needed_skill_raises(self):
        new_skill = "Not needed skill"
        with self.assertRaises(Exception) as ex:
            self.drummer.learn_new_skill(new_skill)
        self.assertEqual(f"{new_skill} is not a needed skill!", str(ex.exception))

        with self.assertRaises(Exception) as ex:
            self.guitarist.learn_new_skill(new_skill)
        self.assertEqual(f"{new_skill} is not a needed skill!", str(ex.exception))

        with self.assertRaises(Exception) as ex:
            self.singer.learn_new_skill(new_skill)
        self.assertEqual(f"{new_skill} is not a needed skill!", str(ex.exception))

    def test_musician_learn_new_skill_already_learned_raises(self):
        self.drummer.learn_new_skill(self.DRUMMER_SKILL)
        with self.assertRaises(Exception) as ex:
            self.drummer.learn_new_skill(self.DRUMMER_SKILL)
        self.assertEqual(f"{self.DRUMMER_SKILL} is already learned!", str(ex.exception))

        self.guitarist.learn_new_skill(self.GUITARIST_SKILL)
        with self.assertRaises(Exception) as ex:
            self.guitarist.learn_new_skill(self.GUITARIST_SKILL)
        self.assertEqual(f"{self.GUITARIST_SKILL} is already learned!", str(ex.exception))

        self.singer.learn_new_skill(self.SINGER_SKILL)
        with self.assertRaises(Exception) as ex:
            self.singer.learn_new_skill(self.SINGER_SKILL)
        self.assertEqual(f"{self.SINGER_SKILL} is already learned!", str(ex.exception))


class BandTests(TestCase):
    BAND_NAME = "Test band name"
    MEMBER_1 = Guitarist("Guitarist name", 16)
    MEMBER_2 = Singer("Singer name", 17)

    def setUp(self) -> None:
        self.band = Band(self.BAND_NAME)

    def test_empty_band_name_raises(self):
        with self.assertRaises(ValueError) as error:
            Band("")
        self.assertEqual("Band name should contain at least one character!", str(error.exception))

    def test_band_initialized_properly(self):
        self.assertEqual(self.BAND_NAME, self.band.name)
        self.assertEqual([], self.band.members)

    def test_band_add_member(self):
        self.band.add_member(self.MEMBER_1)
        self.assertEqual([self.MEMBER_1], self.band.members)
        self.band.add_member(self.MEMBER_2)
        self.assertEqual([self.MEMBER_1, self.MEMBER_2], self.band.members)

    def test_band_remove_member(self):
        self.band.add_member(self.MEMBER_1)
        self.assertEqual([self.MEMBER_1], self.band.members)
        self.band.remove_member(self.MEMBER_1)
        self.assertEqual([], self.band.members)

    def test_band_str(self):
        self.assertEqual(f"{self.BAND_NAME} with 0 members.", str(self.band))
        self.band.add_member(self.MEMBER_1)
        self.assertEqual(f"{self.BAND_NAME} with 1 members.", str(self.band))


class ConcertTests(TestCase):
    GENRE = "Rock"
    AUDIENCE = 5
    TICKET_PRICE = 10.0
    EXPENSES = 6.00
    PLACE = "Sofia"
    INVALID_GENRE = "Pop"
    INVALID_AUDIENCE = 0
    INVALID_TICKET_PRICE = 0.99
    INVALID_PLACE_EMPTY_STRING = ""
    INVALID_PLACE = "A"
    INVALID_EXPENSES = -1

    def setUp(self) -> None:
        self.concert = Concert(self.GENRE, self.AUDIENCE, self.TICKET_PRICE, self.EXPENSES, self.PLACE)

    def test_concert_initialisation_properly(self):
        self.assertEqual(self.GENRE, self.concert.genre)
        self.assertEqual(self.AUDIENCE, self.concert.audience)
        self.assertEqual(self.TICKET_PRICE, self.concert.ticket_price)
        self.assertEqual(self.EXPENSES, self.concert.expenses)
        self.assertEqual(self.PLACE, self.concert.place)

        concert = Concert(self.GENRE, 1, self.TICKET_PRICE, self.EXPENSES, self.PLACE)
        self.assertEqual(1, concert.audience)

        concert = Concert(self.GENRE, self.AUDIENCE, 1, self.EXPENSES, self.PLACE)
        self.assertEqual(1, concert.ticket_price)

        concert = Concert(self.GENRE, self.AUDIENCE, self.TICKET_PRICE, 0, self.PLACE)
        self.assertEqual(0, concert.expenses)

    def test_concert_invalid_genre(self):
        with self.assertRaises(ValueError) as error:
            Concert(self.INVALID_GENRE, self.AUDIENCE, self.TICKET_PRICE, self.EXPENSES, self.PLACE)
        self.assertEqual(f"Our group doesn't play {self.INVALID_GENRE}!", str(error.exception))

    def test_concert_no_audience_raises(self):
        with self.assertRaises(ValueError) as error:
            Concert(self.GENRE, self.INVALID_AUDIENCE, self.TICKET_PRICE, self.EXPENSES, self.PLACE)
        self.assertEqual("At least one person should attend the concert!", str(error.exception))

    def test_concert_invalid_ticket_price_raises(self):
        with self.assertRaises(ValueError) as error:
            Concert(self.GENRE, self.AUDIENCE, self.INVALID_TICKET_PRICE, self.EXPENSES, self.PLACE)
        self.assertEqual("Ticket price must be at least 1.00$!", str(error.exception))

    def test_concert_invalid_expenses_raises(self):
        with self.assertRaises(ValueError) as error:
            Concert(self.GENRE, self.AUDIENCE, self.TICKET_PRICE, self.INVALID_EXPENSES, self.PLACE)
        self.assertEqual("Expenses cannot be a negative number!", str(error.exception))

    def test_concert_invalid_place_raises(self):
        with self.assertRaises(ValueError) as error:
            Concert(self.GENRE, self.AUDIENCE, self.TICKET_PRICE, self.EXPENSES, self.INVALID_PLACE_EMPTY_STRING)
        self.assertEqual("Place must contain at least 2 chars. It cannot be empty!", str(error.exception))

        with self.assertRaises(ValueError) as error:
            Concert(self.GENRE, self.AUDIENCE, self.TICKET_PRICE, self.EXPENSES, self.INVALID_PLACE)
        self.assertEqual("Place must contain at least 2 chars. It cannot be empty!", str(error.exception))

    def test_concert_str(self):
        self.assertEqual(f"{self.GENRE} concert at {self.PLACE}.", str(self.concert))


class ConcertTrackerAppTests(TestCase):
    MUSICIAN_TYPE = "Singer"
    MUSICIAN_NAME = "Test Name"
    MUSICIAN_AGE = 17
    INVALID_MUSICIAN_TYPE = "Test Invalid Type"
    BAND_NAME = "Test Band Name"
    GENRE = "Rock"
    AUDIENCE = 5
    TICKET_PRICE = 10.0
    EXPENSES = 6.00
    PLACE = "Sofia"

    def setUp(self) -> None:
        self.concert_tracker_app = ConcertTrackerApp()

    def test_init_properly(self):
        self.assertEqual([], self.concert_tracker_app.bands)
        self.assertEqual([], self.concert_tracker_app.musicians)
        self.assertEqual([], self.concert_tracker_app.concerts)

    def test_create_musician_properly(self):
        self.assertEqual(f"{self.MUSICIAN_NAME} is now a {self.MUSICIAN_TYPE}.",
                         self.concert_tracker_app.create_musician(self.MUSICIAN_TYPE, self.MUSICIAN_NAME,
                                                                  self.MUSICIAN_AGE))

    def test_create_invalid_musician_type_raises(self):
        with self.assertRaises(ValueError) as error:
            self.concert_tracker_app.create_musician(self.INVALID_MUSICIAN_TYPE, self.MUSICIAN_NAME, self.MUSICIAN_AGE)
        self.assertEqual("Invalid musician type!", str(error.exception))

    def test_create_musician_with_same_name_raises(self):
        self.concert_tracker_app.create_musician(self.MUSICIAN_TYPE, self.MUSICIAN_NAME, self.MUSICIAN_AGE)
        with self.assertRaises(Exception) as ex:
            self.concert_tracker_app.create_musician(self.MUSICIAN_TYPE, self.MUSICIAN_NAME, self.MUSICIAN_AGE)
        self.assertEqual(f"{self.MUSICIAN_NAME} is already a musician!", str(ex.exception))

    def test_create_band_successfully(self):
        self.assertEqual(f"{self.BAND_NAME} was created.", self.concert_tracker_app.create_band(self.BAND_NAME))

    def test_create_band_with_same_name_raises(self):
        self.concert_tracker_app.create_band(self.BAND_NAME)
        with self.assertRaises(Exception) as ex:
            self.concert_tracker_app.create_band(self.BAND_NAME)
        self.assertEqual(f"{self.BAND_NAME} band is already created!", str(ex.exception))

    def test_create_concert_successfully(self):
        self.assertEqual(f"{self.GENRE} concert in {self.PLACE} was added.",
                         self.concert_tracker_app.create_concert(self.GENRE, self.AUDIENCE, self.TICKET_PRICE,
                                                                 self.EXPENSES, self.PLACE))

    def test_create_concert_in_the_same_place_raises(self):
        self.concert_tracker_app.create_concert(self.GENRE, self.AUDIENCE, self.TICKET_PRICE, self.EXPENSES, self.PLACE)
        with self.assertRaises(Exception) as ex:
            self.concert_tracker_app.create_concert(self.GENRE, self.AUDIENCE, self.TICKET_PRICE, self.EXPENSES,
                                                    self.PLACE)
        self.assertEqual(f"{self.PLACE} is already registered for {self.GENRE} concert!", str(ex.exception))

    def test_add_musician_to_band_successfully(self):
        self.concert_tracker_app.create_musician(self.MUSICIAN_TYPE, self.MUSICIAN_NAME, self.MUSICIAN_AGE)
        self.concert_tracker_app.create_band(self.BAND_NAME)
        self.assertEqual(f"{self.MUSICIAN_NAME} was added to {self.BAND_NAME}.",
                         self.concert_tracker_app.add_musician_to_band(self.MUSICIAN_NAME, self.BAND_NAME))

    def test_add_non_existing_musician_to_band(self):
        self.concert_tracker_app.create_band(self.BAND_NAME)
        with self.assertRaises(Exception) as ex:
            self.concert_tracker_app.add_musician_to_band(self.MUSICIAN_NAME, self.BAND_NAME)
        self.assertEqual(f"{self.MUSICIAN_NAME} isn't a musician!", str(ex.exception))

    def test_add_musician_to_non_existing_band(self):
        self.concert_tracker_app.create_musician(self.MUSICIAN_TYPE, self.MUSICIAN_NAME, self.MUSICIAN_AGE)
        with self.assertRaises(Exception) as ex:
            self.concert_tracker_app.add_musician_to_band(self.MUSICIAN_NAME, self.BAND_NAME)
        self.assertEqual(f"{self.BAND_NAME} isn't a band!", str(ex.exception))

    def test_remove_musician_from_band_successfully(self):
        self.concert_tracker_app.create_musician(self.MUSICIAN_TYPE, self.MUSICIAN_NAME, self.MUSICIAN_AGE)
        self.concert_tracker_app.create_band(self.BAND_NAME)
        self.concert_tracker_app.add_musician_to_band(self.MUSICIAN_NAME, self.BAND_NAME)
        self.assertEqual(f"{self.MUSICIAN_NAME} was removed from {self.BAND_NAME}.",
                         self.concert_tracker_app.remove_musician_from_band(self.MUSICIAN_NAME, self.BAND_NAME))

    def test_remove_non_existing_musician_from_band(self):
        self.concert_tracker_app.create_band(self.BAND_NAME)
        with self.assertRaises(Exception) as ex:
            self.concert_tracker_app.remove_musician_from_band(self.MUSICIAN_NAME, self.BAND_NAME)
        self.assertEqual(f"{self.MUSICIAN_NAME} isn't a member of {self.BAND_NAME}!", str(ex.exception))

    def test_remove_musician_from_non_existing_band(self):
        self.concert_tracker_app.create_musician(self.MUSICIAN_TYPE, self.MUSICIAN_NAME, self.MUSICIAN_AGE)
        with self.assertRaises(Exception) as ex:
            self.concert_tracker_app.remove_musician_from_band(self.MUSICIAN_NAME, self.BAND_NAME)
        self.assertEqual(f"{self.BAND_NAME} isn't a band!", str(ex.exception))

    def test_start_concert_not_enough_members_raises(self):
        self.concert_tracker_app.create_band(self.BAND_NAME)
        with self.assertRaises(Exception) as ex:
            self.concert_tracker_app.start_concert(self.PLACE, self.BAND_NAME)
        self.assertEqual(f"{self.BAND_NAME} can't start the concert because it doesn't have enough members!",
                         str(ex.exception))

        self.concert_tracker_app.create_musician(self.MUSICIAN_TYPE, self.MUSICIAN_NAME, self.MUSICIAN_AGE)
        self.concert_tracker_app.add_musician_to_band(self.MUSICIAN_NAME, self.BAND_NAME)

        with self.assertRaises(Exception) as ex:
            self.concert_tracker_app.start_concert(self.PLACE, self.BAND_NAME)
        self.assertEqual(f"{self.BAND_NAME} can't start the concert because it doesn't have enough members!",
                         str(ex.exception))

    def test_start_rock_concert_properly(self):
        self.concert_tracker_app.create_band(self.BAND_NAME)
        self.concert_tracker_app.create_musician("Singer", "SingerName", self.MUSICIAN_AGE)
        self.concert_tracker_app.create_musician("Drummer", "DrummerName", self.MUSICIAN_AGE)
        self.concert_tracker_app.create_musician("Guitarist", "GuitaristName", self.MUSICIAN_AGE)
        self.concert_tracker_app.create_musician("Guitarist", "GuitaristName2", self.MUSICIAN_AGE)
        self.concert_tracker_app.add_musician_to_band("SingerName", self.BAND_NAME)
        self.concert_tracker_app.add_musician_to_band("DrummerName", self.BAND_NAME)
        self.concert_tracker_app.add_musician_to_band("GuitaristName", self.BAND_NAME)
        self.concert_tracker_app.add_musician_to_band("GuitaristName2", self.BAND_NAME)
        self.concert_tracker_app.create_concert(self.GENRE, self.AUDIENCE, self.TICKET_PRICE, self.EXPENSES, self.PLACE)

        self.concert_tracker_app.musicians[0].learn_new_skill("sing high pitch notes")
        self.concert_tracker_app.musicians[1].learn_new_skill("play the drums with drumsticks")
        self.concert_tracker_app.musicians[2].learn_new_skill("play rock")
        self.concert_tracker_app.musicians[3].learn_new_skill("play rock")

        profit = self.AUDIENCE * self.TICKET_PRICE - self.EXPENSES
        self.assertEqual(f"{self.BAND_NAME} gained {profit:.2f}$ from the {self.GENRE} concert in {self.PLACE}.",
                         self.concert_tracker_app.start_concert(self.PLACE, self.BAND_NAME))

    def test_start_metal_concert_properly(self):
        self.concert_tracker_app.create_band(self.BAND_NAME)
        self.concert_tracker_app.create_musician("Singer", "SingerName", self.MUSICIAN_AGE)
        self.concert_tracker_app.create_musician("Drummer", "DrummerName", self.MUSICIAN_AGE)
        self.concert_tracker_app.create_musician("Guitarist", "GuitaristName", self.MUSICIAN_AGE)
        self.concert_tracker_app.create_musician("Guitarist", "GuitaristName2", self.MUSICIAN_AGE)
        self.concert_tracker_app.add_musician_to_band("SingerName", self.BAND_NAME)
        self.concert_tracker_app.add_musician_to_band("DrummerName", self.BAND_NAME)
        self.concert_tracker_app.add_musician_to_band("GuitaristName", self.BAND_NAME)
        self.concert_tracker_app.add_musician_to_band("GuitaristName2", self.BAND_NAME)
        self.concert_tracker_app.create_concert("Metal", self.AUDIENCE, self.TICKET_PRICE, self.EXPENSES, self.PLACE)

        self.concert_tracker_app.musicians[0].learn_new_skill("sing low pitch notes")
        self.concert_tracker_app.musicians[1].learn_new_skill("play the drums with drumsticks")
        self.concert_tracker_app.musicians[2].learn_new_skill("play metal")
        self.concert_tracker_app.musicians[3].learn_new_skill("play metal")

        profit = self.AUDIENCE * self.TICKET_PRICE - self.EXPENSES
        self.assertEqual(f"{self.BAND_NAME} gained {profit:.2f}$ from the Metal concert in {self.PLACE}.",
                         self.concert_tracker_app.start_concert(self.PLACE, self.BAND_NAME))

    def test_start_jazz_concert_properly(self):
        self.concert_tracker_app.create_band(self.BAND_NAME)
        self.concert_tracker_app.create_musician("Singer", "SingerName", self.MUSICIAN_AGE)
        self.concert_tracker_app.create_musician("Drummer", "DrummerName", self.MUSICIAN_AGE)
        self.concert_tracker_app.create_musician("Guitarist", "GuitaristName", self.MUSICIAN_AGE)
        self.concert_tracker_app.create_musician("Guitarist", "GuitaristName2", self.MUSICIAN_AGE)
        self.concert_tracker_app.add_musician_to_band("SingerName", self.BAND_NAME)
        self.concert_tracker_app.add_musician_to_band("DrummerName", self.BAND_NAME)
        self.concert_tracker_app.add_musician_to_band("GuitaristName", self.BAND_NAME)
        self.concert_tracker_app.add_musician_to_band("GuitaristName2", self.BAND_NAME)
        self.concert_tracker_app.create_concert("Jazz", self.AUDIENCE, self.TICKET_PRICE, self.EXPENSES, self.PLACE)

        self.concert_tracker_app.musicians[0].learn_new_skill("sing high pitch notes")
        self.concert_tracker_app.musicians[0].learn_new_skill("sing low pitch notes")
        self.concert_tracker_app.musicians[1].learn_new_skill("play the drums with drum brushes")
        self.concert_tracker_app.musicians[2].learn_new_skill("play jazz")
        self.concert_tracker_app.musicians[3].learn_new_skill("play jazz")

        profit = self.AUDIENCE * self.TICKET_PRICE - self.EXPENSES
        self.assertEqual(f"{self.BAND_NAME} gained {profit:.2f}$ from the Jazz concert in {self.PLACE}.",
                         self.concert_tracker_app.start_concert(self.PLACE, self.BAND_NAME))

    def test_start_concert_members_do_not_have_required_skills_raises(self):
        self.concert_tracker_app.create_band(self.BAND_NAME)
        self.concert_tracker_app.create_musician("Singer", "SingerName", self.MUSICIAN_AGE)
        self.concert_tracker_app.create_musician("Drummer", "DrummerName", self.MUSICIAN_AGE)
        self.concert_tracker_app.create_musician("Guitarist", "GuitaristName", self.MUSICIAN_AGE)
        self.concert_tracker_app.create_musician("Guitarist", "GuitaristName2", self.MUSICIAN_AGE)
        self.concert_tracker_app.add_musician_to_band("SingerName", self.BAND_NAME)
        self.concert_tracker_app.add_musician_to_band("DrummerName", self.BAND_NAME)
        self.concert_tracker_app.add_musician_to_band("GuitaristName", self.BAND_NAME)
        self.concert_tracker_app.add_musician_to_band("GuitaristName2", self.BAND_NAME)
        self.concert_tracker_app.create_concert("Jazz", self.AUDIENCE, self.TICKET_PRICE, self.EXPENSES, self.PLACE)

        self.concert_tracker_app.musicians[0].learn_new_skill("sing high pitch notes")
        # self.concert_tracker_app.musicians[0].learn_new_skill("sing low pitch notes")
        self.concert_tracker_app.musicians[1].learn_new_skill("play the drums with drum brushes")
        self.concert_tracker_app.musicians[2].learn_new_skill("play jazz")
        self.concert_tracker_app.musicians[3].learn_new_skill("play jazz")

        with self.assertRaises(Exception) as ex:
            self.concert_tracker_app.start_concert(self.PLACE, self.BAND_NAME)
        self.assertEqual(f"The {self.BAND_NAME} band is not ready to play at the concert!", str(ex.exception))


if __name__ == "__main__":
    main()
