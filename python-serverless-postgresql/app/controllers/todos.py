from sqlalchemy.orm import Session
from app.models import (
    Todo
)


def list(session: Session):
    data = session.query(Todo).all()
    return data


def create(session: Session, title: str):
    pass
