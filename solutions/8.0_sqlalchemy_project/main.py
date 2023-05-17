from database import init_db, get_session
from operations.book_operations import (
    add_book,
    get_all_books,
    get_book_by_id,
    update_book_availability,
    delete_book,
)
from operations.member_operations import (
    add_member,
    get_all_members,
    get_member_by_id,
    update_member_info,
    delete_member,
)
from operations.loan_operations import (
    add_loan,
    get_all_loans,
    get_loan_by_id,
    return_loan,
    delete_loan,
)

if __name__ == "__main__":
    db_name = "library_management_system"
    engine = init_db(db_name)
    session = get_session(engine)

    # Use the functions from book_operations, member_operations, and loan_operations to perform CRUD operations
    # add_book(
    #     session, "The Catcher in the Rye", "J.D. Salinger", "9780316769488"
    # )
    # for book in get_all_books(session):
    #     print(book.title, book.author, book.isbn, book.available)
