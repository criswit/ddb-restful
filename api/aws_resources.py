import boto3


def get_session(region_name):
    session = boto3.session.Session(region_name=region_name)
    return session


def ssm_client(session):
    ssm = session.client('ssm')
    return ssm


def ddb_resource(session, ddb_table_name):
    dynamo = session.resource('dynamodb')
    ddb = dynamo.Table(ddb_table_name)
    return ddb
