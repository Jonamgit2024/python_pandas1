# Now Question 1 - a python program to create a csv file showing total amount earned from each department
import pandas as pd
import read_data_from_s3_bucket as s3_reader

# To get total amount earned from each department we need 4 data tables 1. Departments , 2. Categories , 3. Products, 4. Order_items
departments = s3_reader.df_departments
categories = s3_reader.df_categories
products = s3_reader.df_products
order_items =s3_reader.df_order_items

# The Column names are also assigned from schemas.json during read

departments = departments.set_index('department_id')
categories = categories.set_index('category_department_id')

# Adding Departments and Categories and reset_index to keep department id till end
departments_categories = departments.join(categories,how='inner')
departments_categories = departments_categories.reset_index(names='department_id')

# now, adding products as well into the combination
departments_categories =departments_categories.set_index('category_id')
products = products.set_index('product_cateogry_id')
departments_categories_products = departments_categories.join(products,how='inner')
#removing unwanted columns category_name, category_id is unwated as well but kept for reference
columns_to_delete =['product_image','product_description','product_name']
departments_categories_products = departments_categories_products.drop(columns_to_delete,axis=1)
departments_categories_products = departments_categories_products.reset_index(names='category_id')

#now, adding order_items into the combination
departments_categories_products = departments_categories_products.set_index('product_id')
order_items = order_items.set_index('order_item_product_id')
departments_categories_products_order_items = departments_categories_products.join(order_items,how='inner')

# now, going further we can compare if the product_price in products and order_items are same
columns_equal =departments_categories_products_order_items['order_item_product_price'].equals (departments_categories_products_order_items['product_price'])
print(f"Product price in Products and order_items is same :{columns_equal}")
departments_categories_products_order_items = departments_categories_products_order_items.reset_index('product_id')

# Dropping all unwanted columns
columns_to_delete =['product_id','category_id','product_price','order_item_product_price','category_name','order_item_id','order_item_order_id','order_item_quantity']
departments_total_price_obtained  = departments_categories_products_order_items.drop(columns_to_delete,axis=1)

# Providing Cumulative sum
departments_total_price_obtained ['cumulative_price'] = departments_total_price_obtained.groupby(['department_id','department_name'])['order_item_subtotal'].cumsum()
departments_total_price_obtained = departments_total_price_obtained.drop('order_item_subtotal',axis=1)
final_df = departments_total_price_obtained.groupby(['department_id','department_name'])['cumulative_price'].max().reset_index()
final_df = final_df.rename(columns={'cumulative_price': 'total_cumulative_price'})

print(final_df)