import uuid
from datetime import datetime


def make_create_item(table_name, data):
    timestamp = str(datetime.utcnow().timestamp())
    partition_attribute = table_name + 'Id'
    item = {
        partition_attribute: str(uuid.uuid4()),
        'name': data['name'],
        'color': data['color'],
        'createdAt': timestamp,
        'updatedAt': timestamp,
    }
    return item
