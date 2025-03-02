import pandas as pd

file_path =r"D:\Python\practice1\data\retail_db\orders\part-00000"
#r"data\retail_db\orders\part-00000"  # Corrected file path
relative_path = r"data\retail_db\orders\part-00000"

try:
    orders_columns=['order_id','order_date','order_customer_id','order_status']
    orders = pd.read_csv(file_path, names=orders_columns)
    # --------- To get all orders ----------------------
    print(orders) 
    # --------- To get unique values in order_status ----------------------
    print(orders['order_status'].unique())
    # --------- To get all orders with status COMPLETE----------------------
    print(orders.query('order_status=="COMPLETE"'))
    # --------- To get all orders happened on 2014/01/01 and status COMPLETE ----------------------
    #print(orders.query('order_date == "2014-01-01 00:00:00.0" and order_status == "COMPLETE"')) date-time is better checked by pin-pointing the exact or use datatime operation
    # --------- To get all orders which are either complete or close ----------------------
    print(orders.query('order_status in ["COMPLETE","CLOSED"]'))
    # --------- To get aggregate/count of orders bu their status i.e.., Noof Complete, Closed,Canceled,hold, processing ----------------------
    print(orders.\
     groupby('order_status')['order_id'].\
     agg('count')
    )
    # -------------- To get aggregate/count by order month and then by order_status-----------------------
    orders['order_month'] =orders.apply(lambda order:order.order_date[:7], axis=1)
    print(orders)
    print(orders.\
     groupby(['order_month','order_status'])['order_id'].\
     agg('count')
    )

    
except FileNotFoundError:
    print(f"Error: File not found at {file_path}")
except pd.errors.EmptyDataError:
    print(f"Error: The file at {file_path} is empty.")
except Exception as e:
    print(f"An error occurred: {e}")