import json
from typing import List

def error_response(status: int, message: str):
    return {
        "statusCode": status,
        "body": json.dumps({
            "message": message
        })
    }

def data_response(status: int, data: List[object]):
    return {
        "statusCode": status,
        "body": json.dumps({
            "data": data
        })
    }
