import json
import datetime
import uuid
from typing import List
from sqlalchemy.ext.declarative import DeclarativeMeta

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
        }, cls=AlchemyEncoder)
    }


class AlchemyEncoder(json.JSONEncoder):

    def default(self, obj):
        if isinstance(obj.__class__, DeclarativeMeta):
            # an SQLAlchemy class
            fields = {}
            for field in [x for x in dir(obj) if not x.startswith('_') and x != 'metadata']:
                data = obj.__getattribute__(field)
                try:
                    if isinstance(data, datetime.datetime):
                        fields[field] = data.isoformat()
                    elif isinstance(data, uuid.UUID):
                        fields[field] = str(data)
                    else:
                        json.dumps(data) # this will fail on non-encodable values, like other classes
                        fields[field] = data
                except TypeError as e:
                    fields[field] = str(e)
            # a json-encodable dict
            return fields

        return json.JSONEncoder.default(self, obj)
