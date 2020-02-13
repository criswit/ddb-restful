# Simple Serverless REST API

This project contains source code to create basic RESTful Web Services allowing for CRUD operations on DynamoDB table. 

## Structure

```bash
api/
   __init__.py
   aws_operations.py --> functions that operate on aws resources
   aws_resources.py --> functions that create boto sessions, clients, resources
   constants.py --> common static values used throughout app
   toolset.py --> functions that perform various non-aws specific operations
   create_item.py --> lambda for performing PUT on dynamo table 

events/
   req.json --> json which mimics proxy API gateway event for local testing

template.yaml --> cfn template for deploying all required resources
```

## Deploy

```bash
sam build
```

```bash
sam local invoke --event events/req.json
```

```bash
sam deploy 
```
