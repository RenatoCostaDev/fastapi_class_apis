from fastapi import FastAPI
import models
from database import engine

#  2nd part
from typing import Annotated
from fastapi import Depends, HTTPException
from sqlalchemy.orm import Session
from database import get_db


# 3rd part
from models import Books, BookRequest

app = FastAPI()

models.Base.metadata.create_all(bind=engine)

db_dependency = Annotated[Session, Depends(get_db)]

@app.get('/')
async def read_all(db: db_dependency):
    return db.query(Books).all()

@app.get('/book/{id}')
async def read_book(db: db_dependency, id: int):
    book_model = db.query(Books).filter(Books.id == id).first()
    if book_model is not None:
        return book_model
    raise HTTPException(status_code=404, detail='Book not found')

@app.post('/book')
async def create_book(db: db_dependency, book_request: BookRequest):
    book_model = Books(**book_request.model_dump())
    db.add(book_model)
    db.commit()

@app.put('/book/{id}')
async def update_book(db: db_dependency, book_request: BookRequest, id: int):
    book_model = db.query(Books).filter(Books.id == id).first()
    if book_model is None:
        raise HTTPException(status_code=404, detail='Book not found')
    book_model.title = book_request.title
    book_model.author = book_request.author
    book_model.rating = book_request.rating

    db.add(book_model)
    db.commit()

@app.delete('/book/{id}')
async def delete_book(db: db_dependency,id: int):
    book_model = db.query(Books).filter(Books.id == id).first()
    if book_model is None:
        raise HTTPException(status_code=404, detail='Book not found')    
    db.query(Books).filter(Books.id == id).delete()
    db.commit()