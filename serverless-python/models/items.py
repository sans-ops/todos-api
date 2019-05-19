from pynamodb.models import Model
from pynamodb.attributes import (
    UnicodeAttribute, UTCDateTimeAttribute
)

class Item(Model):
    class Meta:
        table_name = "items"

    id = UnicodeAttribute(hash_key=True)
    todo_id = UnicodeAttribute(hash_key=True)
    name = UnicodeAttribute(null=True)
    created_at = UTCDateTimeAttribute()
