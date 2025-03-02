import json
import pandas as pd

Json_path = r"D:\Python\practice1\data\retail_db\schemas.json"
customers_path = r"D:\Data-Engineering\Python-for-Data-Engineering\035 Python Essentials for Data Engineers\04 Data Processing using Pandas\data\retail_db\customers\part-00000"
orders_path =r"D:\Python\practice1\data\retail_db\orders\part-00000"

Schemas = json.load(open(Json_path))

def get_column_names(Schemas,ds_name,sorting_key='column_position'):
    column_details = Schemas[ds_name]
    columns = sorted(column_details, key=lambda col:col[sorting_key])
    return [col['column_name'] for col in columns]

print(get_column_names(Schemas,'orders')) 
#['order_id', 'order_date', 'order_customer_id', 'order_status']
print(get_column_names(Schemas,'customers'))
#['customer_id', 'customer_fname', 'customer_lname', 'customer_email', 'customer_password', 'customer_street', 'customer_city', 'customer_state', 'customer_zipcode']
orders = pd.read_csv(orders_path, names=(get_column_names(Schemas,'orders')) ) 
customers = pd.read_csv(customers_path, names=(get_column_names(Schemas,'customers')) ) 
# Before joining setting index
customers = customers.set_index('customer_id')
orders = orders.set_index('order_customer_id')
#Joining Customers and orders
customers_orders = customers.join(orders,how='inner')
print(customers_orders)
customers_orders = customers_orders.reset_index(names='customer_id')
customer_order_count =(customers_orders. \
      groupby('customer_id')['customer_id'] .\
      agg(order_count ='count').reset_index()
      )
print(customer_order_count)
customers_with_more_than_10_orders =customer_order_count.query('order_count >= 10')
print(customers_with_more_than_10_orders)
customers_with_more_than_10_orders = customers_with_more_than_10_orders.set_index('customer_id')
customers_with_more_than_10_orders_list = customers.join(customers_with_more_than_10_orders, how='inner')
print(customers_with_more_than_10_orders_list)