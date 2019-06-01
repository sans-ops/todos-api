from app.models import (
    Todo
)

def list(session):
    data = session.query(Todo).all()
    return data
