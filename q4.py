#     Create API Gateway which triggers lambda Function and prints the name of the user passed in the request.

# Deliverable: Python Code.

import json

def lambda_handler(event, context):
    # TODO implement
    return {
        'statusCode': 200,
        'name' : event['name'],
    }

 # GATEWAY URL
 # https://ih9r9ahmtc.execute-api.us-east-1.amazonaws.com/prod/getname?name=shriram