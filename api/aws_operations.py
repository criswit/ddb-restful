import aws_resources as aws


def get_ssm_parameter_value(session, parameter_path):
    ssm = aws.ssm_client(session)
    parameter_details = ssm.get_parameter(Name=parameter_path, WithDecryption=True)
    parameter_value = parameter_details['Parameter']['Value']
    return parameter_value


def create_ddb_item(ddb, item):
    resp = ddb.put_item(Item=item)
    return resp
