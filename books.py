from typing import Optional
from pydantic import BaseModel, Field # Field => será responsável pelas autentificações

class Book:
    id: int
    title: str
    author: str
    rating: float

    def __init__(self, id, title, author, rating):
        self.id = id
        self.title = title
        self.author = author
        self.rating = rating

class BookRequest(BaseModel):
    id: Optional[int] = None  # Pode acontecer situações que você não sabe o id
    title: str = Field(min_length=3)
    author: str = Field(min_length=1)
    rating: float= Field(gt=0)

    class Config:
        json_schema_extra = {   # schema_extra
            'example': {
                "title": "fastApi",
                "author": "Renato Costa",
                "rating": 10
            }
        }