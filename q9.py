#     Write a program that creates your table “Games” in your AWS DynamoDB and adds certains items in the dynamo db. Example schema: 

# Schema “Games” :

# gid {Number}

# gname {String}

# publisher {String} 

# rating {Number}

# release_date {String}

# genres {String Set}



import boto3

import logging

#Initialize the logger
logging.basicConfig(filename="q9.log", 
                    format='%(asctime)s %(message)s', 
                    filemode='w') 
#Creating an object 
logger=logging.getLogger() 
#set logger to debug
logger.setLevel(logging.DEBUG) 


# Get the service resource.
dynamodb = boto3.resource('dynamodb' , region_name='us-east-1')

# Create the DynamoDB table.
logger.info("creating table")
table = dynamodb.create_table(
    TableName='shriram_games',
    KeySchema=[
        {
            'AttributeName': 'gid',
            'KeyType': 'HASH'
        },
        {
            'AttributeName': 'gname',
            'KeyType': 'RANGE'
        }
    ],
    AttributeDefinitions=[
        {
            'AttributeName': 'gid',
            'AttributeType': 'N'
        },
        {
            'AttributeName': 'gname',
            'AttributeType': 'S'
        },
    ],
    ProvisionedThroughput={
        'ReadCapacityUnits': 5,
        'WriteCapacityUnits': 5
    }
)
logger.info("initializing table")
table = dynamodb.Table('shriram_games')

#Adding items to the table
logger.info("putting data in table")
table.put_item(
   Item={
        'gid': 1,
        'gname': 'shri',
        'publisher': 'Doe',
        'rating': 7,
        'release_date': '10/1/2019',
        'genres': {
        	'genre1' : 'fiction',
        	'genre2' : 'lit',
        },
    }
)


table.put_item(
   Item={
        'gid': 2,
        'gname': 'shriram',
        'publisher': 'Doe',
        'rating': 7,
        'release_date': '10/1/2019',
        'genres': {
        	'genre1' : 'fiction',
        	'genre2' : 'lit',
        },
    }
)


table.put_item(
   Item={
        'gid': 3,
        'gname': 'avinash',
        'publisher': 'Doe',
        'rating': 7,
        'release_date': '10/1/2019',
        'genres': {
        	'genre1' : 'fiction',
        	'genre2' : 'lit',
        },
    }
)
