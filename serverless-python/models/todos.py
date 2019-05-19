from pynamodb.models import Model
from pynamodb.attributes import (
    UnicodeAttribute, UTCDateTimeAttribute
)

class Todo(Model):
    class Meta:
        table_name = "todos"

    id = UnicodeAttribute(hash_key=True)
    title = UnicodeAttribute(null=True)
    created_at = UTCDateTimeAttribute()
