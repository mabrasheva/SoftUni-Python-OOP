from unittest import TestCase, main

from project.movie import Movie


class MovieTests(TestCase):
    NAME = "Test Name"
    YEAR = 1988
    RATING = 9

    def setUp(self) -> None:
        self.movie = Movie(self.NAME, self.YEAR, self.RATING)

    def test_init(self):
        self.assertEqual(self.NAME, self.movie.name)
        self.assertEqual(self.YEAR, self.movie.year)
        self.assertEqual(self.RATING, self.movie.rating)
        self.assertEqual([], self.movie.actors)

    def test_empty_string_name_raises(self):
        with self.assertRaises(ValueError) as error:
            Movie("", self.YEAR, self.RATING)
        self.assertEqual("Name cannot be an empty string!", str(error.exception))

    def test_invalid_year_raises(self):
        with self.assertRaises(ValueError) as error:
            Movie(self.NAME, 1880, self.RATING)
        self.assertEqual("Year is not valid!", str(error.exception))

    def test_add_actor_successfully(self):
        actor1 = "Actor1"
        actor2 = "Actor2"
        self.assertEqual([], self.movie.actors)
        self.movie.add_actor(actor1)
        self.assertEqual([actor1], self.movie.actors)
        self.movie.add_actor(actor2)
        self.assertEqual([actor1, actor2], self.movie.actors)

    def test_add_actor_twice_raises(self):
        actor1 = "Actor1"
        self.assertEqual([], self.movie.actors)
        self.movie.add_actor(actor1)
        self.assertEqual([actor1], self.movie.actors)
        expected_string = f"{actor1} is already added in the list of actors!"
        self.assertEqual(expected_string, self.movie.add_actor(actor1))
        self.assertEqual([actor1], self.movie.actors)

    def test_gt(self):
        movie2 = Movie("Name", 1990, 1)
        self.assertEqual(f'"{self.NAME}" is better than "Name"', self.movie.__gt__(movie2))

        movie2.rating = 10
        self.assertEqual(f'"{movie2.name}" is better than "{self.NAME}"', self.movie.__gt__(movie2))

    def test_repr_method(self):
        actor1 = "Actor1"
        actor2 = "Actor2"
        self.assertEqual([], self.movie.actors)
        self.movie.add_actor(actor1)
        self.assertEqual([actor1], self.movie.actors)
        self.movie.add_actor(actor2)
        self.assertEqual([actor1, actor2], self.movie.actors)

        expected_string = f"Name: {self.NAME}\n"
        expected_string += f"Year of Release: {self.YEAR}\n"
        expected_string += f"Rating: {self.RATING:.2f}\n"
        expected_string += f"Cast: {', '.join(self.movie.actors)}"

        self.assertEqual(expected_string, self.movie.__repr__())


if __name__ == "__main__":
    main()
