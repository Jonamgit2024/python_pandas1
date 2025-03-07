import glob
import json
import os
import pandas as pd
#print(glob.glob(r'Project1\data\retail_db\**', recursive= True))

json_path= r"Project1\data\retail_db\schemas.json"
Schemas = json.load(open(json_path))

def get_column_names(Schemas,ds_name,sorting_key='column_position'):
    column_details = Schemas[ds_name]
    columns = sorted(column_details, key=lambda col:col[sorting_key])
    return [col['column_name'] for col in columns]

src_file_names = (glob.glob(r'Project1\data\retail_db\*\part-*'))#To Print each file name in the folder
total_files =len(src_file_names)
tgt_file_folder=r'Project1\data\retail_db_json'

for file_name in src_file_names:
  file_name_division =file_name.split("\\") # We can get the ds_name from this file names and splitting 
  # Project1\data\retail_db\*\part-*
  desired_name=file_name_division[3]
  file =pd.read_csv(file_name, names=(get_column_names(Schemas,desired_name)))
  final_file_name=file_name_division[2]
  target_file=tgt_file_folder+"\\"+desired_name
  os.makedirs((tgt_file_folder+"\\"+desired_name),exist_ok=True)
  print((tgt_file_folder+"\\"+desired_name))
  file.to_json(
      target_file,
      orient='records',
      lines= True )
# Much Rustic better follow App.py for clear interpretation