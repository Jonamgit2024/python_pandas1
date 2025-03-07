import glob
import json
import os
import re
import pandas as pd

# Program to read schema and return column_names
def get_column_names(schemas, ds_name, sorting_key='column_position'):
    column_details = schemas[ds_name]
    columns =sorted(column_details, key=lambda col:col[sorting_key])
    return [col['column_name'] for col in columns]

def read_csv(file, schemas):
    ds_name = file.split("\\")[-2]
    columns = get_column_names(schemas, ds_name)
    df = pd.read_csv(file, names=columns)
    return df

def to_json(df, tgt_base_dir, ds_name, file_name):
    json_file_path = tgt_base_dir+"\\"+ds_name+"\\"+file_name
    os.makedirs(tgt_base_dir+"\\"+ds_name, exist_ok=True)
    df.to_json(
        json_file_path,
        orient='records',
        lines=True
    )

def file_converter(src_base_dir, tgt_base_dir,ds_name):
    print(f"File Converter open working on : {ds_name}")
    schemas = json.load(open(src_base_dir+"\\"+"schemas.json"))
    files = glob.glob(src_base_dir+"\\"+"*"+"\\"+"part-*") #Project1\data\retail_db\*\part-*'
    for file in files:
        df = read_csv(file, schemas)
        file_name = file.split("\\")[-1]
        to_json(df, tgt_base_dir, ds_name, file_name)

def process_files(ds_names=None):
    src_base_dir = r'Project1\data\retail_db'
    tgt_base_dir = r'Project1\data\retail_db_json'
    schemas = json.load(open(src_base_dir+"\\"+"schemas.json"))#r"Project1\data\retail_db\schemas.json"
    if not ds_names:
        ds_names = schemas.keys()
    for ds_name in ds_names:
        print(f'Processing {ds_name}')
        file_converter(src_base_dir, tgt_base_dir, ds_name)

process_files()
# To enhance and avoid hard coding the src_base_dir and tgt_base_dir as enivornment varaible 

#-----------------------Environment Variables ----------------------------------------
