import os

def get_datastore_host():
    return os.getenv("DYNAMODB_HOST", None)
