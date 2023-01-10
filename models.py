from sqlalchemy import ARRAY, Column, Date, Integer, Text, text
from sqlalchemy.sql.schema import Column
from .database import Base

class Post(Base):
   __tablename__ = "posts"

   id = Column(Integer, primary_key=True)
   rubrics = Column(ARRAY(Text()), nullable=False)
   text= Column(Text, nullable=False)
   created_date = Column(Date, nullable=False)