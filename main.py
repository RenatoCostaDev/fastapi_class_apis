from fastapi import FastAPI
import models
from database import engine

#  2nd part
from typing import Annotated
from fastapi import Depends, HTTPException
from sqlalchemy.orm import Session
from database import get_db


# 3rd part
from models import Todos, TodoRequest

app = FastAPI()

models.Base.metadata.create_all(bind=engine)

db_dependency = Annotated[Session, Depends(get_db)]

@app.get('/')
async def read_all(db: db_dependency):
    return db.query(Todos).all()

@app.get('/todo/{id}')
async def read_todo(db: db_dependency, id: int):
    todo_model = db.query(Todos).filter(Todos.id == id).first()
    if todo_model is not None:
        return todo_model
    raise HTTPException(status_code=404, detail='Todo not found')

# 3rd part
@app.post('/todo')
async def create_todo(db: db_dependency, todo_request: TodoRequest):
    todo_model = Todos(**todo_request.model_dump())
    db.add(todo_model)
    db.commit()

@app.put('/todo/{id}')
async def update_todo(db: db_dependency, todo_request: TodoRequest, id: int):
    todo_model = db.query(Todos).filter(Todos.id == id).first()
    if todo_model is None:
        raise HTTPException(status_code=404, detail='Todo not found')
    todo_model.title = todo_request.title
    todo_model.description = todo_request.description
    todo_model.priority = todo_request.priority
    todo_model.complete = todo_request.complete

    db.add(todo_model)
    db.commit()

@app.delete('/todo/{id}')
async def delete_todo(db: db_dependency,id: int):
    todo_model = db.query(Todos).filter(Todos.id == id).first()
    if todo_model is None:
        raise HTTPException(status_code=404, detail='Todo not found')    
    db.query(Todos).filter(Todos.id == id).delete()
    db.commit()