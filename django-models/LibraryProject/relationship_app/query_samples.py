from relationship_app.models import Author, Book, Library, Librarian

# Query all books by a specific author
author = Author.objects.get(name="George Orwell")
books_by_author = Book.objects.filter(author=author)
print(books_by_author)

# List all books in a library
library = Library.objects.get(name="Central Library")
all_books = library.books.all()
print(all_books)

# Retrieve librarian for a library
librarian = Librarian.objects.get(library=library)
print(librarian)
