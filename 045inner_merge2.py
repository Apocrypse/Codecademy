import pandas as pd

sales = pd.read_csv('sales.csv')

targets = pd.read_csv('targets.csv')

men_women = pd.read_csv('men_women_sales.csv')

all_data = sales.merge(targets)\
	.merge(men_women)

results = all_data[(all_data.revenue > all_data.target) & (all_data.women > all_data.men)]
print(results)
