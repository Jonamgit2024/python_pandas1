import pandas as pd
import read_data_from_s3_bucket as s3_reader
import transform_data_in_python as python_transform
import io
import json
import boto3
import credentials

# Convert dataframe into csv file
def dataframe_to_csv():
    try :
        csv_buffer = io.StringIO()
        python_transform.final_df.to_csv(csv_buffer, index=False, header=True) #if we don't want header we can make it false
        csv_content = csv_buffer.getvalue()
        return csv_content

    except Exception as e:
        print(f"Error with DataFrame : {e}")

#loading data into s3 bucket
def load_data_to_s3_bucket(csv_content):
    try:
    # Create an S3 client using the credentials
        s3 = boto3.client(
            's3',
            aws_access_key_id=credentials.AWS_Access_ID,
            aws_secret_access_key=credentials.AWS_Access_password,
            region_name=credentials.AWS_Access_region,
        )

        s3_key = f"{credentials.S3_FOLDER_NAME}/{credentials.S3_OUTPUT_FOLDER}/{credentials.S3_OUTPUT_FILE_NAME}"
        # Upload CSV to S3, overwriting if it exists
        s3.put_object(Bucket=credentials.S3_BUCKET_NAME, Key=s3_key, Body=csv_content)
        print(f"CSV file uploaded to s3://{credentials.S3_BUCKET_NAME}/{s3_key}")

    except Exception as e :
        print(f"Error with accessing S3 Bucket : {e}")


load_data_to_s3_bucket(dataframe_to_csv())