import datetime
import json
import uuid
import common.security
from common.response import (
    data_response, error_response
)
from models import (
    Todo, Item
)

def list(event, context):
    data = []
    for item in Todo.scan():
        d = {
            "id": item.id,
            "title": item.title,
            "created_at": str(item.created_at)
        }
        data.append(d)
    return data_response(200, data)



def set(event, context):
    if not event["body"]:
        return error_response(500, "empty body")
    body = json.loads(event["body"])
    if "title" not in body:
        return error_response(500, "no title given")
    title = body["title"]
    todo = Todo(
        id=str(uuid.uuid4()),
        title=title,
        created_at=datetime.datetime.now()
    )
    data = todo.save()
    d = {
        "id": todo.id,
        "title": todo.title,
        "created_at": str(todo.created_at)
    }
    return data_response(200, d)



def get(event, context):
    data = []
    id = event["pathParameters"]["id"]
    for todo in Todo.batch_get([id]):
        d = {
            "id": todo.id,
            "title": todo.title,
            "created_at": str(todo.created_at)
        }
        data.append(d)
    return data_response(200, data)


def delete(event, context):
    id = event["pathParameters"]["id"]
    for todo in Todo.batch_get([id]):
        todo.delete()
    return data_response(200, [])
