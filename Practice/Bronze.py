from datetime import datetime
import pandas as pd


df=pd.read_csv('CustData1.csv')

noofrows=len(df)
print(f"No of Rows in CSV file is{noofrows}")

#importing datetime to add time stamp
timestamp = datetime.now().strftime('%Y-%m-%d %H:%M:%S')

df['Audit_Bronze'] = timestamp

new_csv_file = 'Audit_Bronze_updated_timestamp_column.csv'
df.to_csv(new_csv_file, index=False)

print(f"New column with timestamp added and saved to {new_csv_file}")


# for i in range(1,noofrows):
#     new_column ={
#         'columni'='timestamp'
#     }
