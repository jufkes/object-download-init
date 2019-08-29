import boto3
import os

access_key = os.getenv('ACCESS_KEY')
secret_key = os.getenv('SECRET_KEY')
host = os.getenv('OBJECTHOST')
bucket = os.getenv('BUCKET')
destination = os.getenv('HOST_DESTINATION') + "/"

s3 = boto3.client('s3',
                  endpoint_url=host,
                   aws_access_key_id=access_key,
                   aws_secret_access_key=secret_key)

response = s3.list_objects_v2(Bucket=bucket)

for item in response['Contents']:
    file = destination + item['Key']
    print (file)
    s3.download_file(bucket, item['Key'], file)