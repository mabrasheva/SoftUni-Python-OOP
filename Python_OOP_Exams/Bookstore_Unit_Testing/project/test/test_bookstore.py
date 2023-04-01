from unittest import TestCase, main

from project.bookstore import Bookstore


class BookstoreTests(TestCase):
    BOOK_LIMIT = 5

    def setUp(self) -> None:
        self.bookstore = Bookstore(self.BOOK_LIMIT)

    def test_init(self):
        self.assertEqual(self.BOOK_LIMIT, self.bookstore.books_limit)
        self.assertEqual({}, self.bookstore.availability_in_store_by_book_titles)
        self.assertEqual(0, self.bookstore.total_sold_books)

    def test_book_limit_equal_or_below_zero_raises(self):
        book_limit = 0
        with self.assertRaises(ValueError) as error:
            Bookstore(book_limit)
        self.assertEqual(f"Books limit of {book_limit} is not valid", str(error.exception))

        book_limit = -1
        with self.assertRaises(ValueError) as error:
            Bookstore(book_limit)
        self.assertEqual(f"Books limit of {book_limit} is not valid", str(error.exception))

    def test_len_method(self):
        self.assertEqual(0, self.bookstore.__len__())
        self.bookstore.availability_in_store_by_book_titles = {"A": 1, "B": 2}
        self.assertEqual(3, self.bookstore.__len__())

    def test_receive_book_not_enough_space_in_the_bookstore_raises(self):
        self.assertEqual(0, len(self.bookstore))
        self.bookstore.availability_in_store_by_book_titles = {"A": 1, "B": 2}
        with self.assertRaises(Exception) as ex:
            self.bookstore.receive_book("A", 6)
        self.assertEqual("Books limit is reached. Cannot receive more books!", str(ex.exception))
        self.assertEqual(3, len(self.bookstore))

    def test_receive_book_successfully(self):
        expected_availability_in_store_by_book_titles = {"A": 3}
        expected_returned_string = f"3 copies of A are available in the bookstore."
        self.assertEqual(expected_returned_string, self.bookstore.receive_book("A", 3))
        self.assertEqual(expected_availability_in_store_by_book_titles,
                         self.bookstore.availability_in_store_by_book_titles)
        self.assertEqual(3, len(self.bookstore))
        self.assertEqual({"A": 3}, self.bookstore.availability_in_store_by_book_titles)

        expected_availability_in_store_by_book_titles = {"A": 4}
        expected_returned_string = f"4 copies of A are available in the bookstore."
        self.assertEqual(expected_returned_string, self.bookstore.receive_book("A", 1))
        self.assertEqual(expected_availability_in_store_by_book_titles,
                         self.bookstore.availability_in_store_by_book_titles)
        self.assertEqual(4, len(self.bookstore))
        self.assertEqual({"A": 4}, self.bookstore.availability_in_store_by_book_titles)

    def test_sell_book_book_is_not_available_in_bookstore_raises(self):
        book_title = "A"
        number_of_books = 2
        with self.assertRaises(Exception) as ex:
            self.bookstore.sell_book(book_title, number_of_books)
        self.assertEqual(f"Book {book_title} doesn't exist!", str(ex.exception))

    def test_sell_book_book_not_enough_book_copies_in_bookstore_raises(self):
        book_title = "A"
        wanted_number_of_books = 2
        available_books_number = 1
        self.bookstore.availability_in_store_by_book_titles = {book_title: available_books_number}
        expected_string = f"{book_title} has not enough copies to sell. Left: {available_books_number}"
        with self.assertRaises(Exception) as ex:
            self.bookstore.sell_book(book_title, wanted_number_of_books)
        self.assertEqual(expected_string, str(ex.exception))
        self.assertEqual(1, self.bookstore.availability_in_store_by_book_titles[book_title])

    def test_sell_book_successfully(self):
        book_title = "A"
        wanted_number_of_books = 1
        available_books_number = 3
        expected_string = f"Sold {wanted_number_of_books} copies of {book_title}"

        self.bookstore.availability_in_store_by_book_titles = {book_title: available_books_number}
        total_sold = self.bookstore.total_sold_books + wanted_number_of_books
        self.assertEqual(expected_string, self.bookstore.sell_book(book_title, wanted_number_of_books))
        self.assertEqual(total_sold, self.bookstore.total_sold_books)
        self.assertEqual(2, len(self.bookstore))

        available_books_number -= wanted_number_of_books
        self.assertEqual(available_books_number, self.bookstore.availability_in_store_by_book_titles[book_title])

        self.bookstore.sell_book(book_title, wanted_number_of_books)
        total_sold = self.bookstore.total_sold_books + wanted_number_of_books
        self.assertEqual(expected_string, self.bookstore.sell_book(book_title, wanted_number_of_books))
        self.assertEqual(total_sold, self.bookstore.total_sold_books)
        self.assertEqual(0, len(self.bookstore))

    def test_str_method(self):
        self.bookstore.availability_in_store_by_book_titles = {"A": 1, "B": 2}
        self.bookstore.receive_book("A", 1)
        self.bookstore.sell_book("B", 2)

        expected_string = f"Total sold books: 2\n"
        expected_string += f"Current availability: 2\n"
        expected_string += " - A: 2 copies\n"
        expected_string += " - B: 0 copies"

        self.assertEqual(expected_string, self.bookstore.__str__())


if __name__ == "__main__":
    main()
