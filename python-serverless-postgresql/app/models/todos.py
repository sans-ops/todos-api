from sqlalchemy import Column, String, DateTime
from sqlalchemy.orm import relationship
from sqlalchemy.dialects.postgresql import UUID
from sqlalchemy import func, text
from .base import Base

class Todo(Base):
    __tablename__ = "todos"
    id = Column(UUID(as_uuid=True), unique=True, nullable=False, primary_key=True, server_default=text("gen_random_uuid()"))
    title = Column(String)
    created_at = Column(DateTime, server_default=func.now())
    items = relationship('Item')

    def __init__(self, title):
        self.title = title
