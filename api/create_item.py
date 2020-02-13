import json
import pprint

import aws_operations as awsops
import aws_resources as awsres
import constants
import toolset as tools


def put_handler(event, context):
    pp = pprint.PrettyPrinter(indent=4)
    session = awsres.get_session(constants.region)
    ddb_table_name = awsops.get_ssm_parameter_value(session, constants.ssm_parameter_ddb_table_name)
    ddb = awsres.ddb_resource(session, ddb_table_name)
    pp.pprint('Target DDB Object: ' + ddb_table_name)
    event_body = event['body']
    pp.pprint('Raw Event Body String:' + event_body)
    dict_body = json.loads(event_body)
    dict_len = len(dict_body)
    pp.pprint('Item count: ' + str(dict_len))
    success_count = 0
    failure_count = 0
    for i in range(0, dict_len):
        item = dict_body[i]
        pp.pprint(json.dumps(item))
        try:
            awsops.create_ddb_item(ddb, tools.make_create_item(ddb_table_name, item))
            success_count = success_count + 1
        except KeyError as err:
            print('Handling run-time error, KeyError: ', err)
            failure_count = failure_count + 1

    status_code = tools.assess_job_status(success_count, failure_count)
    pp.pprint('Calculated Job Status: ' + str(status_code))

    return {
        "statusCode": status_code,
        "body": json.dumps({
            "successful_requests": str(success_count),
            "failed_requests": str(failure_count)
        }),
    }
