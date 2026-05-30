class Book:
    books = []

    def __init__(self, title, price):
        self.title = title
        self.price = price
        Book.books.append(self)

    @classmethod
    def display_all_books(cls):
        if not cls.books:
            print("No books available.")
            return
        for index, book in enumerate(cls.books, start=1):
            print(f"{index}. Title: {book.title}, Price: {book.price}")


# Example usage:
if __name__ == "__main__":
    Book("The Hobbit", 250)
    Book("1984", 180)
    Book.display_all_books()