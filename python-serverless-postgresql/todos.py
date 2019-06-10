import os
import json
from http import HTTPStatus
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
import app.common.security
from app.common.counter import Counter
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
counter = Counter()


def metadata(event, context):
    body = {
        "message": "Go Serverless v1.0! Your function executed successfully!",
        "input": event,
        "counter": counter.identify()
    }
    response = {
        "statusCode": 200,
        "body": json.dumps(body)
    }
    return response



def list(event, context):
    data = []
    code = HTTPStatus.INTERNAL_SERVER_ERROR
    try:
        data = app.controllers.todos.list(session)
        code = HTTPStatus.OK
    except Exception as e:
        return error_response(code, str(e))
    return data_response(code, data)



def create(event, context):
    data = []
    code = HTTPStatus.INTERNAL_SERVER_ERROR
    if not event["body"]:
        return error_response(code, "empty body")
    body = json.loads(event["body"])
    if "title" not in body:
        return error_response(code, "no title given")
    title = body["title"]
    data = app.controllers.todos.create(session, title)
    code = HTTPStatus.CREATED
    return data_response(code, data)



def retrieve(event, context):
    data = []
    code = HTTPStatus.INTERNAL_SERVER_ERROR
    id = event["pathParameters"]["id"]
    try:
        data = app.controllers.todos.retrieve(session, id)
        code = HTTPStatus.OK
    except Exception as e:
        return error_response(code, str(e))
    return data_response(code, data)



def update(event, context):
    data = []
    code = HTTPStatus.INTERNAL_SERVER_ERROR
    if not event["body"]:
        return error_response(code, "empty body")
    body = json.loads(event["body"])
    if "title" not in body:
        return error_response(code, "no title given")
    id = event["pathParameters"]["id"]
    try:
        data = app.controllers.todos \
            .update(session, id, {"title": body["title"]})
        code = HTTPStatus.OK
    except Exception as e:
        return error_response(code, str(e))
    return data_response(code, data)



def delete(event, context):
    data = []
    code = HTTPStatus.INTERNAL_SERVER_ERROR
    id = event["pathParameters"]["id"]
    try:
        data = app.controllers.todos \
            .delete(session, id)
        code = HTTPStatus.OK
    except Exception as e:
        return error_response(code, str(e))
    return data_response(code, data)
