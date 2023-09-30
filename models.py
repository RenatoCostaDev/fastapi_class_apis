from database import Base
from sqlalchemy import Column, Integer, String, Boolean

# 3rd part
from pydantic import BaseModel

class Todos(Base):
    __tablename__ = 'todos'

    id = Column(Integer, primary_key=True, index=True)
    title = Column(String)
    description = Column(String)
    priority = Column(Integer)
    complete = Column(Boolean, default=False)

# 3rd part
class TodoRequest(BaseModel):
    title: str
    description: str
    priority: int
    complete: bool