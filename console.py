import pdb
from models.book import Book
from models.author import Author

import repositories.book_repository as book_repository
import repositories.author_repository as author_repository

author_repository.delete_all()
book_repository.delete_all()

author1 = Author("Jack Jarvis")
author_repository.save(author1)

author2 = Author("Steve Jackson")
author_repository.save(author2)

book1 = Book("Lord of the Rings", 1942, author2)
book_repository.save(book1)

book2 = Book("A Beautiful Morning", 2019, author1)
book_repository.save(book2)

