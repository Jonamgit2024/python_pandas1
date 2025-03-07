import boto3
import botocore
import json
import os
import logging
logger = logging.getLogger()
logger.setLevel(logging.INFO)

s3 = boto3.resource('s3')

def lambda_handler(event, context):
    logger.info("New files uploaded to the source bucket.")
        
    key = event['Records'][0]['s3']['object']['key']
        
    source_bucket = event['Records'][0]['s3']['bucket']['name']
    destination_bucket = os.environ['destination_bucket']
    
    source = {'Bucket': source_bucket, 'Key': key}
        
    try:
        response = s3.meta.client.copy(source, destination_bucket, key)
        logger.info("File copied to the destination bucket successfully!")
        
    except botocore.exceptions.ClientError as error:
        logger.error("There was an error copying the file to the destination bucket")
        print('Error Message: {}'.format(error))
        
    except botocore.exceptions.ParamValidationError as error:
        logger.error("Missing required parameters while calling the API.")
        print('Error Message: {}'.format(error))



import boto3
import csv

def lambda_handler(event, context):
    s3 = boto3.client('s3')
    print(f"S3 names is :{s3}")
    print("In LAMBDA")
    bucket = event['Records'][0]['s3']['bucket']['name']
    key = event['Records'][0]['s3']['object']['key']
    print("bucket Name: ", bucket)
    print("Key Value is: ",key)
    # print(event)    
    
    # # Read the CSV file from S3
    obj = s3.get_object(Bucket=bucket, Key=key)
    rows = obj['Body'].read().decode('utf-8').split('\n')
    
    for row in csv.reader(rows):
        print(rows)
        
        