from sqlalchemy import Column, Integer, ForeignKey, Date
from sqlalchemy.orm import relationship
from .base import Base


class Loan(Base):
    __tablename__ = "loans"

    id = Column(Integer, primary_key=True)
    book_id = Column(Integer, ForeignKey("books.id"), nullable=False)
    member_id = Column(Integer, ForeignKey("members.id"), nullable=False)
    start_date = Column(Date, nullable=False)
    due_date = Column(Date, nullable=False)
    return_date = Column(Date, nullable=True)

    book = relationship("Book")
    member = relationship("Member")
