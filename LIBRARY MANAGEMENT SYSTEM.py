class Book:
    def __init__(self, book_id, title, author, year):
        self.book_id = book_id
        self.title = title
        self.author = author
        self.year = year

    def __str__(self):
        return f"ID: {self.book_id}, Title: {self.title}, Author: {self.author}, Year: {self.year}"


class Library:
    def __init__(self):
        self.books = []

    def add_book(self, book):
        self.books.append(book)
        print("Book added successfully!")

    def view_books(self):
        if not self.books:
            print("No books found.")
        else:
            for book in self.books:
                print(book)

    def update_book(self, book_id):
        for book in self.books:
            if book.book_id == book_id:
                print("1. Update Title")
                print("2. Update Author")
                print("3. Update Year")
                update_choice = input("Enter choice: ")

                if update_choice == '1':
                    book.title = input("Enter new Title: ")
                elif update_choice == '2':
                    book.author = input("Enter new Author: ")
                elif update_choice == '3':
                    book.year = input("Enter new Year: ")
                else:
                    print("Invalid choice.")

                print("Book information updated successfully!")
                return
        print("Book not found.")

    def delete_book(self, book_id):
        for i in range(len(self.books)):
            if self.books[i].book_id == book_id:
                del self.books[i]
                print("Book deleted successfully!")
                return
        print("Book not found.")


# Main loop
def main():
    library = Library()

    while True:
        print("\nLibrary Management System")
        print("1. Add Book")
        print("2. View Books")
        print("3. Update Book")
        print("4. Delete Book")
        print("5. Exit")

        choice = input("Enter your choice: ")

        if choice == '1':
            book_id = input("Enter Book ID: ")
            title = input("Enter Book Title: ")
            author = input("Enter Book Author: ")
            year = input("Enter Year of Publication: ")

            book = Book(book_id, title, author, year)
            library.add_book(book)

        elif choice == '2':
            library.view_books()

        elif choice == '3':
            book_id = input("Enter Book ID to update: ")
            library.update_book(book_id)

        elif choice == '4':
            book_id = input("Enter Book ID to delete: ")
            library.delete_book(book_id)

        elif choice == '5':
            print("Exiting...")
            break

        else:
            print("Invalid choice. Please try again.")


if __name__ == "__main__":
    main()