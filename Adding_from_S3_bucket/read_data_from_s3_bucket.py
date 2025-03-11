# Before reading the file from s3 bucket check following in terminal
# 1. AWS CLI installed in your computer using aws --version
# 2. AWS access key and password are generated for you 
# 3. AWS S3 Bucket location and it accessbility permissions

import io
import json
import boto3
import credentials  # Import your credentials module
import pandas as pd

# Create an S3 client using the credentials
s3 = boto3.client(
    's3',
    aws_access_key_id=credentials.AWS_Access_ID,
    aws_secret_access_key=credentials.AWS_Access_password,
    region_name=credentials.AWS_Access_region,
)

try:
    # Example: List buckets
    response = s3.list_buckets()
    buckets = [bucket['Name'] for bucket in response['Buckets']]
    print("Buckets:", buckets)

    # Your S3 read operations here...

    # 1. Read Schema
    s3_key = f"{credentials.S3_FOLDER_NAME}/{credentials.S3_BUCKET_SCHEMA_JSON_TITLE}"
    try:
        obj = s3.get_object(Bucket=credentials.S3_BUCKET_NAME, Key=s3_key)
        json_content = obj['Body'].read().decode('utf-8')  # Decode bytes to string
        data = json.loads(json_content)
        json_file = data
    except Exception as e:
        print(f"Error reading JSON from S3: {e}")

    # Function to get column names from Schema
    def get_column_names(Schemas,ds_name,sorting_key='column_position'):
        column_details = Schemas[ds_name]
        columns = sorted(column_details, key=lambda col:col[sorting_key])
        return [col['column_name'] for col in columns]
    Schemas = json_file

    # 2. Read data Frames 
    try :
        dfs =[]
        for db_type in credentials.S3_RETAIL_DB_TYPE:
            s3_key = f"{credentials.S3_FOLDER_NAME}/{db_type}/{credentials.S3_CSV_FILE_NAME}"
            # Get the object from S3
            obj = s3.get_object(Bucket=credentials.S3_BUCKET_NAME, Key=s3_key)
            csv_content = obj['Body'].read()
            # Read the CSV data into a pandas DataFrame and assign column names from Json/Schema
            df = pd.read_csv(io.BytesIO(csv_content), names =(get_column_names(Schemas,db_type)))
            dfs.append(df)
        df_categories = dfs[0]
        df_customers =dfs[1]
        df_departments =dfs[2]
        df_order_items=dfs[3]
        df_orders=dfs[4]
        df_products=dfs[5]
    except Exception as e:
        print(f"Error reading data files from S3: {e}")

except Exception as e:
    print(f"Error: No Access to buckets {e}")