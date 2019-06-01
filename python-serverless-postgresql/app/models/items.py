from sqlalchemy import Column, String, DateTime, ForeignKey
from sqlalchemy.dialects.postgresql import UUID
from sqlalchemy import func, text
from .base import Base

class Item(Base):
    __tablename__ = "items"
    id = Column(UUID(as_uuid=True), unique=True, nullable=False, primary_key=True, server_default=text("gen_random_uuid()"))
    todo_id = Column(UUID(as_uuid=True), ForeignKey("todos.id"))
    name = Column(String)
    created_at = Column(DateTime, server_default=func.now())

    def __init__(self, todo_id, name):
        self.todo_id = todo_id
        self.name = name
