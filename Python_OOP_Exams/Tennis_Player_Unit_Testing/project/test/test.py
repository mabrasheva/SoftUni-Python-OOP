from unittest import TestCase, main

from project.tennis_player import TennisPlayer


class TennisPlayerTests(TestCase):
    NAME = "TestName"
    AGE = 18
    POINTS = 100

    def setUp(self) -> None:
        self.player = TennisPlayer(self.NAME, self.AGE, self.POINTS)
        self.player2 = TennisPlayer(self.NAME, self.AGE, 200)

    def test_init(self):
        self.assertEqual(self.NAME, self.player.name)
        self.assertEqual(self.AGE, self.player.age)
        self.assertEqual(self.POINTS, self.player.points)
        self.assertEqual([], self.player.wins)

    def test_set_invalid_name(self):
        with self.assertRaises(ValueError) as error:
            self.player.name = "AA"
        self.assertEqual("Name should be more than 2 symbols!", str(error.exception))

    def test_set_valid_name(self):
        self.player.name = "AAA"
        self.assertEqual("AAA", self.player.name)

    def test_set_invalid_age(self):
        with self.assertRaises(ValueError) as error:
            self.player.age = 17
        self.assertEqual("Players must be at least 18 years of age!", str(error.exception))

    def test_set_valid_age(self):
        self.player.age = 19
        self.assertEqual(19, self.player.age)

    def test_add_new_win_successfully(self):
        tournament_name = "Wimbledon"
        tournament_name_2 = "Australia Open"

        self.assertEqual([], self.player.wins)

        self.player.add_new_win(tournament_name)
        self.assertEqual([tournament_name], self.player.wins)

        self.player.add_new_win(tournament_name_2)
        self.assertEqual([tournament_name, tournament_name_2], self.player.wins)

    def test_add_duplicate_win_raises(self):
        tournament_name = "Wimbledon"

        self.player.add_new_win(tournament_name)
        self.assertEqual([tournament_name], self.player.wins)

        expected_string = f"{tournament_name} has been already added to the list of wins!"
        self.assertEqual(expected_string, self.player.add_new_win(tournament_name))
        self.assertEqual([tournament_name], self.player.wins)

    def test_lt_method(self):
        expected_string = f'{self.player2.name} is a top seeded player and he/she is better than {self.player.name}'
        self.assertEqual(expected_string, self.player.__lt__(self.player2))

        expected_string = f'{self.player2.name} is a better player than {self.player.name}'
        self.assertEqual(expected_string, self.player2.__lt__(self.player))

    def test_str_method(self):
        tournament_name = "Wimbledon"
        tournament_name_2 = "Australia Open"
        self.player.add_new_win(tournament_name)
        self.player.add_new_win(tournament_name_2)

        expected_result = f"Tennis Player: {self.player.name}\n" \
                          f"Age: {self.player.age}\n" \
                          f"Points: {self.player.points:.1f}\n" \
                          f"Tournaments won: {', '.join(self.player.wins)}"
        self.assertEqual(expected_result, self.player.__str__())


if __name__ == "__main__":
    main()
