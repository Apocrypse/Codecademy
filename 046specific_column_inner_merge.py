import pandas as pd

orders = pd.read_csv('orders.csv')

products = pd.read_csv('products.csv')

orders_products = pd.merge(
                  orders,
                  products,
                  left_on='product_id',
                  right_on='id',
                  suffixes=['_orders', '_products']
)
print orders_products
