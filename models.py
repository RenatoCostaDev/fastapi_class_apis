from database import Base
from sqlalchemy import Column, Float, Integer, String
from pydantic import BaseModel


class Books(Base):
    __tablename__ = 'books'

    id = Column(Integer, primary_key=True, index=True)
    title = Column(String)
    author = Column(String)
    rating = Column(Float)

class BookRequest (BaseModel):
    title: str
    author: str
    rating: float

    class Config:
        json_schema_extra = {   # schema_extra
            'example': {
                "title": "fastApi",
                "author": "Renato Costa",
                "rating": 10
            }
        }