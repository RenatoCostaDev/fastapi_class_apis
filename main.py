from fastapi import FastAPI
from data import Books
from apiTools import *
from books import *

app = FastAPI(    
   title='Api Biblioteca',
   version='0.0.1',
   description="Api para uma biblioteca,Obs: Pydantic",
)

@app.get('/books')
async def get_books():
    return Books

@app.get('/books/{id}')
async def get_book_by_id(id: int):
    return get_book_id(id, Books)

@app.post('/create-book')
async def create_book(book_request: BookRequest):
    new_book = Book(**book_request.model_dump())
    Books.append(update_id(Books, new_book))
    return Books

@app.put('/update-book')
async def update_book(book_request: BookRequest):
    book_to_update(book_request, Books)
    return Books

@app.delete('/books/{id}')
async def delete_book(id: int):
    book_to_delete(id, Books)
    return Books