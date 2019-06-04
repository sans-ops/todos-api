from sqlalchemy.orm import Session
from app.models import (
    Todo
)


def list(session: Session):
    data = session.query(Todo).all()
    return data


def create(session: Session, title: str):
    todo = Todo(title)
    session.add(todo)
    session.commit()
    return todo


def retrieve(session: Session, id: str):
    data = session.query(Todo) \
            .filter(Todo.id == id) \
            .all()
    return data
