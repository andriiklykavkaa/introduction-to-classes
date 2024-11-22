

class Book:
    def __init__(self, title: str, author: str, price: float, quantity: int):
        self.title = title
        self.author = author
        self.price = price
        self.quantity = quantity

    def apply_discount(self, discount_percentage: float):
        self.price = (self.price * (100 - discount_percentage) * 0.01)

    def sell(self, amount):
        if amount < self.price:
            print("Unable to sell this amount")
            return
        self.quantity -= amount

    def __str__(self):
        return (f"Title: '{self.title}'," +
                f"author: '{self.author}'," +
                f"price: ${self.price}," +
                f"quantity: {self.quantity}")

class BookStore:

    def __init__(self, books: list[Book]):
        self.books = books

    def add_book(self, book: Book):
        self.books.append(book)

    def search(self, query):
        filtered_books = []
        for book in self.books:
            if book.title == query or book.author == query:
                filtered_books.append(book)
        return filtered_books

    def calculate_total_value(self) -> float:
        total_value = 0
        for book in self.books:
            total_value += book.price * book.quantity
        return total_value


book1 = Book("Ryan Gosling autobiography", "Ryan Reynolds", 100, 7)
book2 = Book("Gachi remixes collection", "Billy and Van", 85, 10)
book3 = Book("1984", "George Orwell", 79, 100)

print(book1)


bookStore = BookStore([book1, book2, book3])
bookStore.add_book(book1)
bookStore.add_book(book2)
bookStore.add_book(book3)

print(bookStore.calculate_total_value())
print(bookStore.search("Ryan Reynolds"))