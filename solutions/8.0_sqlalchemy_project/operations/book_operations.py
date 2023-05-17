from models.book import Book


def add_book(session, title, author, isbn):
    book = Book(title=title, author=author, isbn=isbn)
    session.add(book)
    session.commit()


def get_all_books(session):
    return session.query(Book).all()


def get_book_by_id(session, book_id):
    return session.query(Book).get(book_id)


def update_book_availability(session, book_id, available):
    book = session.query(Book).get(book_id)
    book.available = available
    session.commit()


def delete_book(session, book_id):
    book = session.query(Book).get(book_id)
    session.delete(book)
    session.commit()
