import pandas as pd

sales = pd.read_csv('sales.csv')
print(sales)
targets = pd.read_csv('targets.csv')
print(targets)

sales_vs_targets = pd.merge(sales, targets)
print(sales_vs_targets)
