from relationship_app.models import Author, Book, Library, Librarian
from relationship_app.query_samples import get_books_by_author, list_books_in_library, get_librarian_for_library

print(get_books_by_author('Author Name'))
print(list_books_in_library('Library Name'))
print(get_librarian_for_library('Library Name'))


# Query all books by a specific author
def get_books_by_author(author_name):
    author = Author.objects.get(name=author_name)
    return Book.objects.filter(author=author)

# List all books in a library
def list_books_in_library(library_name):
    library = Library.objects.get(name=library_name)
    return library.books.all()

# Retrieve the librarian for a library
def get_librarian_for_library(library_name):
    library = Library.objects.get(name=library_name)
    return Librarian.objects.get(library=library)
#