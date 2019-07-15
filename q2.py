# Assuming you have a versioning enabled S3 bucket and multiple versions of the same object, Write a python script which takes the bucket name and object path as parameters and downloads the 2nd latest version of this object i.e the one prior to the latest version.

#IMport the boto3 module and logging module
import boto3
import logging

#Initialize the logger
logging.basicConfig(filename="newfile.log", 
                    format='%(asctime)s %(message)s', 
                    filemode='w') 
#Creating an object 
logger=logging.getLogger() 
#set logger to debug
logger.setLevel(logging.DEBUG) 

#INitialize the s3 client
s3 = boto3.client('s3')
#s3.download_file('shriram-test', 'Screenshot from 2019-07-04 16-38-20.png', 'pic1.png', ExtraArgs={'VersionId': ' 	ksVJKAUv0IOuiat29ror89P8z2RblZcY'})


#list_object_versions method returns the Json response with all informations of versions of the objected requested
logger.info("requesting response")
response = s3.list_object_versions(
                    Bucket='shriram-test',
                    Prefix='Screenshot from 2019-07-04 16-38-20.png'
                )

#Download the file with the second last version, retrieved from the JSON response
#WE pass the EXtra Args
logger.info("Downloading file")
s3.download_file('shriram-test', 'Screenshot from 2019-07-04 16-38-20.png', 'pic2.png', ExtraArgs={'VersionId': response["Versions"][1]["VersionId"] })
