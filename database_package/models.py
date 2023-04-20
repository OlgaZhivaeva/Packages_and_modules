import sqlalchemy as sq
from sqlalchemy.orm import declarative_base

Base = declarative_base()

def create_tables(engine):
    Base.metadata.drop_all(engine)
    Base.metadata.create_all(engine)

class People(Base):
    __tablename__ = "people"
    id = sq.Column(sq.Integer, primary_key=True)
    name = sq.Column(sq.String(length=40))
    surname = sq.Column(sq.String(length=40))