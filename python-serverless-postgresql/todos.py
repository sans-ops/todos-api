import os
import json
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
import app.common.security
from app.common.response import (
    data_response, error_response
)
import app.controllers.todos

engine = create_engine(os.getenv(
            "DATABASE_URL", ""),
            json_serializer=json.dumps
        )
connection = engine.connect()
Session = sessionmaker(bind=engine)
session = Session()



def list(event, context):
    data = []
    code = 500
    try:
        data = app.controllers.todos.list(session)
        code = 200
    except Exception as e:
        return error_response(code, str(e))
    return data_response(code, data)



def create(event, context):
    if not event["body"]:
        return error_response(500, "empty body")
    body = json.loads(event["body"])
    if "title" not in body:
        return error_response(500, "no title given")
    title = body["title"]
    todo = app.controllers.todos.create(session, title)
    return data_response(201, todo)



def retrieve(event, context):
    data = []
    code = 500
    id = event["pathParameters"]["id"]
    try:
        data = app.controllers.todos.retrieve(session, id)
        code = 200
    except Exception as e:
        return error_response(code, str(e))
    return data_response(code, data)



def update(event, context):
    data = []
    code = 500
    if not event["body"]:
        return error_response(500, "empty body")
    body = json.loads(event["body"])
    if "title" not in body:
        return error_response(500, "no title given")
    id = event["pathParameters"]["id"]
    try:
        data = app.controllers.todos \
            .update(session, id, {"title": body["title"]})
        code = 200
    except Exception as e:
        return error_response(code, str(e))
    return data_response(code, data)


#def create(event, context):
#    if not event["body"]:
#        return error_response(500, "empty body")
#    body = json.loads(event["body"])
#    if "title" not in body:
#        return error_response(500, "no title given")
#    title = body["title"]
#    todo = Todo(
#        id=str(uuid.uuid4()),
#        title=title,
#        created_at=datetime.datetime.now()
#    )
#    data = todo.save()
#    d = {
#        "id": todo.id,
#        "title": todo.title,
#        "created_at": str(todo.created_at)
#    }
#    return data_response(200, d)
#
#
#
#def retrieve(event, context):
#    data = []
#    id = event["pathParameters"]["id"]
#    for todo in Todo.batch_get([id]):
#        d = {
#            "id": todo.id,
#            "title": todo.title,
#            "created_at": str(todo.created_at)
#        }
#        data.append(d)
#    return data_response(200, data)
#
#
#
#def update(event, context):
#    data = []
#    if not event["body"]:
#        return error_response(500, "empty body")
#    body = json.loads(event["body"])
#    if "title" not in body:
#        return error_response(500, "no title given")
#    id = event["pathParameters"]["id"]
#    for todo in Todo.batch_get([id]):
#        todo.title = body["title"]
#        todo.update({
#            "title": {
#                "value": body["title"],
#                "action": "PUT"
#            }
#        })
#        d = {
#            "id": todo.id,
#            "title": todo.title,
#            "created_at": str(todo.created_at)
#        }
#        data.append(d)
#    return data_response(200, data)
#
#
#
#def delete(event, context):
#    id = event["pathParameters"]["id"]
#    for todo in Todo.batch_get([id]):
#        todo.delete()
#    return data_response(200, [])
