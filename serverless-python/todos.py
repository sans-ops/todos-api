import json
import common.security

def list(event, context):
    status_code: int = 200
    result: str = "OK"
    data = []
    body = {
        "data": data,

        "result": result
    }

    response = {
        "statusCode": status_code,
        "body": json.dumps(body)
    }

    return response

def get(event, context):
    status_code: int = 200
    result: str = "OK"
    data = []
    body = {
        "data": data,

        "result": result,

        "event": event
    }

    response = {
        "statusCode": status_code,
        "body": json.dumps(body)
    }

    return response
