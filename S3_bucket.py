import boto3
from zipfile import ZipFile
from botocore.exceptions import ClientError

region = 'eu-west-1'

s3_Client = boto3.client("s3", region)
s3_Client.create_bucket(Bucket = 'my-bucket')
#s3Resource = boto3.resource('s3')
# created a ZipFile object
zipObj = ZipFile('sample.zip', 'w')
# Add multiple files to the zip
zipObj.write('Hello_word.py')
zipObj.write('happiness.py')
# close the Zip File
zipObj.close()
#Files to upload in s3
try:
    s3_Client.meta.client.upload_file(
        'C:/Users/AD00741/PycharmProjects/API_CloudFormatn/Hello_word.py',
        'my-bucket',
        'sample.zip')

except Exception as exp:
    print('exp: ', exp)



