import pandas as pd

inventory = pd.read_csv('inventory.csv')

staten_island = inventory.head(10)
product_request = staten_island.product_description

seed_request = inventory[(inventory.location == 'Brooklyn') & (inventory.product_type == 'seeds')]

stock = lambda quantity: True if quantity > 0 else False
inventory['in_stock'] = inventory.quantity.apply(stock)

value = lambda row: row.price * row.quantity
inventory['total_value'] = inventory.apply(value, axis=1)

combine = lambda row: '{} - {}'.format(row.product_type, row.product_description)
inventory['full_description'] = inventory.apply(combine, axis=1)

print(inventory.head(10))
