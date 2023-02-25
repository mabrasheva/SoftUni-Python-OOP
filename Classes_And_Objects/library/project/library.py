from project.user import User


class Library:
    def __init__(self):
        self.user_records = []  # an empty list that will store the users (users objects) of the library
        self.books_available = {}
        self.rented_books = {}

    def get_book(self, author: str, book_name: str, days_to_return: int, user: User):

        for author, books_list in self.books_available.items():
            if book_name in books_list:
                user.books.append(book_name)
                self.books_available[author].remove(book_name)
                if user.username not in self.rented_books:
                    self.rented_books[user.username] = {}
                self.rented_books[user.username][book_name] = days_to_return
                return f"{book_name} successfully rented for the next {days_to_return} days!"

        days_to_return_rented_book = 0
        for book_dict in self.rented_books.values():
            for book, days in book_dict.items():
                if book == book_name:
                    days_to_return_rented_book = days
                    break
        return f'The book "{book_name}" is already rented and will be available in {days_to_return_rented_book} days!'

    def return_book(self, author: str, book_name: str, user: User):
        if book_name in user.books:
            user.books.remove(book_name)
            self.books_available[author].append(book_name)
            del self.rented_books[user.username][book_name]
        return f"{user.username} doesn't have this book in his/her records!"
