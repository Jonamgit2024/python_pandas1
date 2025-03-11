AWS_Access_ID = ""
AWS_Access_password = ""
AWS_Access_region = "us-east-1"
AWS_S3_Bucket_Folder = "arn:aws:s3:::retaildatabase"
S3_BUCKET_NAME = "retaildatabase"
S3_FOLDER_NAME = "retail_db"
S3_CSV_FILE_NAME = "part-00000"
S3_RETAIL_DB_TYPE =["categories","customers","departments","order_items","orders","products"]
S3_BUCKET_SCHEMA_JSON_TITLE = "schemas.json"
S3_OUTPUT_FOLDER = "results"
S3_OUTPUT_FILE_NAME = "answer1.csv"
# we can use much easier approach as well or use these directly
S3_Retail_categroies = S3_RETAIL_DB_TYPE[0] #"categories"
S3_Retail_customers = S3_RETAIL_DB_TYPE[1] #"customers"
S3_Retail_departments = S3_RETAIL_DB_TYPE[2] #"departments"
S3_Retail_order_items = S3_RETAIL_DB_TYPE[3] #"order_items"
S3_Retail_orders = S3_RETAIL_DB_TYPE[4] #"orders"
S3_Retail_products = S3_RETAIL_DB_TYPE[5] #"products"
# or use a for loop


#---------------------------------------------------------------------
# Example
# aws configure
# AWS Access Key ID [None]: AKIAIOSFODNN7EXAMPLE
# AWS Secret Access Key [None]: EXAMPLEPROVIDEDBYAWSINCSV
# Default region name [None]: us-east-1
# Default output format [None]: json