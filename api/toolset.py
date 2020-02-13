import uuid
from datetime import datetime

import constants


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


def assess_job_status(successful_records, failed_records):
    if successful_records >= 0 and failed_records == 0:
        return constants.statusCode_success
    if successful_records >= 0 and failed_records > 0:
        return constants.statusCode_warning
    if successful_records == 0 and failed_records > 0:
        return constants.statusCode_failure
