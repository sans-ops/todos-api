from pynamodb.models import Model
from pynamodb.attributes import (
    UnicodeAttribute, UTCDateTimeAttribute
)
from models.utils import get_datastore_host

class Todo(Model):
    class Meta:
        table_name = "todos"
        host = get_datastore_host()

    id = UnicodeAttribute(hash_key=True)
    title = UnicodeAttribute(null=True)
    created_at = UTCDateTimeAttribute()
