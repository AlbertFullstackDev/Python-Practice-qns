class BookLibrary:
    def __init__(self):
        self.books = {}

    # Add Book Method
    def add_book(self, book):
        self.books[book.lower()] = self.books.get(book.lower(), 0) + 1

    # remove Book
    def remove_book(self, book):
        self.books[book.lower()] = self.books.get(book.lower(), 0) - 1

    # Get book quantity
    # def get_quantity(self, book):
    #     # print(self.books.get(book.lower(), 0))
    #     # print(self.books[book.lower()])

    # Get item magic method
    def __getitem__(self, book):
        return book.lower() + " Qty: " + str(self.books.get(book.lower(), 0))

    # Set item magic method
    def __setitem__(self, book, qty):
        self.books[book.lower()] = self.books.get(book.lower(), 0) + qty

    # Len magic method
    def __len__(self):
        return len(self.books)

    # Iter magic method
    def __iter__(self):
        return iter(self.books)


# INSTANTIATE OBJ
moro_library = BookLibrary()
# ADD BOOK
moro_library.add_book("python")
moro_library.add_book("Python")
moro_library.add_book("Python")

# REMOVE BOOK
moro_library.remove_book("PYTHON")

# SET QTY
moro_library["python"] = 10
moro_library["laravel"] = 5

# GET QTY
# moro_library.get_quantity("python")
print(moro_library["python"])
print(moro_library["laravel"])

# GET TOTAL BOOKS
print(f"Total Book types in Library: {len(moro_library)}")

# ITERATE BOOKS
for book, qty in moro_library.books.items():
    print(f"BOOK NAME {book} : QTY {qty}")
