from pynamodb.models import Model
from pynamodb.attributes import (
    UnicodeAttribute, UTCDateTimeAttribute
)
from models.utils import get_datastore_host

class Item(Model):
    class Meta:
        table_name = "items"
        host = get_datastore_host()

    id = UnicodeAttribute(hash_key=True)
    todo_id = UnicodeAttribute(hash_key=True)
    name = UnicodeAttribute(null=True)
    created_at = UTCDateTimeAttribute()
