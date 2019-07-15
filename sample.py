


import boto3

s3 = boto3.client('s3')
#s3.download_file('shriram-test', 'Screenshot from 2019-07-04 16-38-20.png', 'pic1.png', ExtraArgs={'VersionId': ' 	ksVJKAUv0IOuiat29ror89P8z2RblZcY'})

response = s3.list_object_versions(
                    Bucket='shriram-test',
                    Prefix='Screenshot from 2019-07-04 16-38-20.png'
                )

s3.download_file('shriram-test', 'Screenshot from 2019-07-04 16-38-20.png', 'pic2.png', ExtraArgs={'VersionId': response["Versions"][1]["VersionId"] })
