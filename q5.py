#     Write a lambda function to copy an object from one s3 bucket to another.

# Deliverable: Python Code.

#Import the json module
import json

def lambda_handler(event, context):
    # TODO implement
    s3 = boto3.resource("s3")
    # Retrieving the data from the request
    source, destination = event["source"], event["destination"]
    src_d = {}
    src_d["Bucket"] = source
    #Copying all objects from one bucket to another
    for obj1 in s3.Bucket(source).objects.all():
        src_d["Key"] = obj1.key
        dest_b = s3.Bucket(destination)
        dest_b.copy(src_d, obj1.key)