from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from models.base import Base


def init_db(db_name):
    engine = create_engine(f"sqlite:///{db_name}.db", echo=True)
    Base.metadata.create_all(bind=engine)
    return engine


def get_session(engine):
    Session = sessionmaker(bind=engine)
    return Session()
