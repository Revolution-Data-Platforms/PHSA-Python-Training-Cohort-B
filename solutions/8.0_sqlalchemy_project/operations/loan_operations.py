from datetime import datetime, timedelta
from models.loan import Loan
from operations.book_operations import update_book_availability


def add_loan(session, book_id, member_id, days=14):
    start_date = datetime.now().date()
    due_date = start_date + timedelta(days=days)
    loan = Loan(
        book_id=book_id,
        member_id=member_id,
        start_date=start_date,
        due_date=due_date,
    )
    session.add(loan)
    update_book_availability(session, book_id, 0)
    session.commit()


def get_all_loans(session):
    return session.query(Loan).all()


def get_loan_by_id(session, loan_id):
    return session.query(Loan).get(loan_id)


def return_loan(session, loan_id):
    loan = session.query(Loan).get(loan_id)
    loan.return_date = datetime.now().date()
    update_book_availability(session, loan.book_id, 1)
    session.commit()


def delete_loan(session, loan_id):
    loan = session.query(Loan).get(loan_id)
    session.delete(loan)
    session.commit()
