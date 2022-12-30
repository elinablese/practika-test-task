from sqlalchemy import create_engine, ARRAY, Column, Date, Integer, Text, text
from sqlalchemy.ext.declarative import declarative_base

DeclarativeBase = declarative_base()
metadata = DeclarativeBase.metadata


class Post(DeclarativeBase):
    __tablename__ = 'posts'

    id = Column(Integer, primary_key=True)
    rubrics = Column(ARRAY(Text()), nullable=False)
    text = Column(Text, nullable=False)
    created_date = Column(Date, nullable=False)

    def __repr__(self):
        return "".format(self.code)