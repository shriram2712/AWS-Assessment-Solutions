#     Write a program that reads your table “Games” from your AWS DynamoDB and 

# Returns only the game where ‘gid=2’ (“Query” Feature DynamoDB).

# Prints out the ‘gname’ and the ‘rating’ only.

import boto3
from boto3.dynamodb.conditions import Key, Attr

import logging

#Initialize the logger
logging.basicConfig(filename="q8.log", 
                    format='%(asctime)s %(message)s', 
                    filemode='w') 
#Creating an object 
logger=logging.getLogger() 
#set logger to debug
logger.setLevel(logging.DEBUG) 

# Get the service resource.
dynamodb = boto3.resource('dynamodb' , region_name='us-east-1')
logger.info("initializing table")
table = dynamodb.Table('shriram_games')

# query with condition
logger.info("initializing query")
response = table.query(
    KeyConditionExpression=Key('gid').eq(2))

# Displaying only gname and rating
logger.info("displaying data")
for i in response['Items']:
	print(i['gname'] , i['rating'])