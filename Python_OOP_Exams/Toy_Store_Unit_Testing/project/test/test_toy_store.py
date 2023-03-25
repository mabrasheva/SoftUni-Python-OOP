from unittest import TestCase, main

from project.toy_store import ToyStore


class ToyStoreTests(TestCase):
    SHELF = "A"
    TOY_NAME = "Toy Name"

    def setUp(self) -> None:
        self.shelf_dict = ToyStore()

    def test_init(self):
        expected_result = {
            "A": None,
            "B": None,
            "C": None,
            "D": None,
            "E": None,
            "F": None,
            "G": None,
        }
        self.assertEqual(expected_result, self.shelf_dict.toy_shelf)

    def test_add_toy_not_existing_shelf_raises(self):
        shelf = "H"
        with self.assertRaises(Exception) as ex:
            self.shelf_dict.add_toy(shelf, self.TOY_NAME)
        self.assertEqual("Shelf doesn't exist!", str(ex.exception))

    def test_add_toy_already_in_shelf_raises(self):
        self.shelf_dict.add_toy(self.SHELF, self.TOY_NAME)
        with self.assertRaises(Exception) as ex:
            self.shelf_dict.add_toy(self.SHELF, self.TOY_NAME)
        self.assertEqual("Toy is already in shelf!", str(ex.exception))

    def test_add_toy_is_already_taken_raises(self):
        self.shelf_dict.add_toy(self.SHELF, "AnotherToy")
        with self.assertRaises(Exception) as ex:
            self.shelf_dict.add_toy(self.SHELF, self.TOY_NAME)
        self.assertEqual("Shelf is already taken!", str(ex.exception))

    def test_add_toy_successfully(self):
        self.assertEqual(f"Toy:{self.TOY_NAME} placed successfully!",
                         self.shelf_dict.add_toy(self.SHELF, self.TOY_NAME))
        expected_result = {
            "A": self.TOY_NAME,
            "B": None,
            "C": None,
            "D": None,
            "E": None,
            "F": None,
            "G": None,
        }
        self.assertEqual(expected_result, self.shelf_dict.toy_shelf)

    def test_remove_toy_from_not_existing_shelf(self):
        shelf = "H"
        with self.assertRaises(Exception) as ex:
            self.shelf_dict.remove_toy(shelf, self.TOY_NAME)
        self.assertEqual("Shelf doesn't exist!", str(ex.exception))

    def test_remove_not_existing_toy(self):
        with self.assertRaises(Exception) as ex:
            self.shelf_dict.remove_toy(self.SHELF, self.TOY_NAME)
        self.assertEqual("Toy in that shelf doesn't exists!", str(ex.exception))

        self.shelf_dict.add_toy(self.SHELF, "AnotherToy")
        with self.assertRaises(Exception) as ex:
            self.shelf_dict.remove_toy(self.SHELF, self.TOY_NAME)
        self.assertEqual("Toy in that shelf doesn't exists!", str(ex.exception))

    def test_remove_toy_successfully(self):
        self.shelf_dict.add_toy(self.SHELF, self.TOY_NAME)
        expected_string = f"Remove toy:{self.TOY_NAME} successfully!"
        self.assertEqual(expected_string, self.shelf_dict.remove_toy(self.SHELF, self.TOY_NAME))
        expected_result = {
            "A": None,
            "B": None,
            "C": None,
            "D": None,
            "E": None,
            "F": None,
            "G": None,
        }
        self.assertEqual(expected_result, self.shelf_dict.toy_shelf)


if __name__ == "__main__":
    main()
