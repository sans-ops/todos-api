import app.common.security
import json
import socket
from app.common.counter import Counter

counter = Counter()
hostname = socket.gethostname()
host_ip = socket.gethostbyname(hostname)

def hello(event, context):
    body = {
        "message": "Go Serverless v1.0! Your function executed successfully!",
        "input": event,
        "counter": counter.identify(),
        "host": {
            "host_name": hostname,
            "host_ip": host_ip
        }
    }

    response = {
        "statusCode": 200,
        "body": json.dumps(body)
    }

    return response

    # Use this code if you don't use the http event with the LAMBDA-PROXY
    # integration
    """
    return {
        "message": "Go Serverless v1.0! Your function executed successfully!",
        "event": event
    }
    """
