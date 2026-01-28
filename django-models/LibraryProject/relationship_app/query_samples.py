from relationship_app.models import Author, Book, Library, Librarian

# Query all books by a specific author
author = Author.objects.filter(name="Chinua Achebe").first()
if author:
    books_by_author = Book.objects.filter(author=author)
    print("Books by author:", books_by_author)
else:
    print("Author not found")

# List all books in a library
library = Library.objects.filter(name="Central Library").first()
if library:
    books_in_library = library.books.all()
    print("Books in library:", books_in_library)
else:
    print("Library not found")

# Retrieve the librarian for a library
if library:
    librarian = Librarian.objects.filter(library=library).first()
    print("Librarian:", librarian)
