import json
import common.security
from common.counter import Counter

counter = Counter()

def hello(event, context):
    counter.increment()
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

    # Use this code if you don't use the http event with the LAMBDA-PROXY
    # integration
    """
    return {
        "message": "Go Serverless v1.0! Your function executed successfully!",
        "event": event
    }
    """


