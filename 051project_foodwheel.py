import pandas as pd
from matplotlib import pyplot as plt

restaurants = pd.read_csv('restaurants.csv')
print(restaurants.head()

cuisine_options_count = restaurants.cuisine.nunique()
cuisine_counts = \
restaurants.groupby('cuisine').name.count().reset_index()

cuisines = cuisine_counts.cuisine.values
counts =  cuisine_counts.name.values
plt.pie(counts, labels=cuisines, autopct='%d%%')
plt.title('Cuisines')
plt.axis('equal')
plt.show()

orders = pd.read_csv('orders.csv')
print(orders.head())

orders['month'] = orders.date.apply(
                  lambda date: date.split('-')[0])
avg_order = orders.groupby('month').price.mean().reset_index()
std_order = orders.groupby('month').price.std().reset_index()

bar_heights = avg_order.price.values
bar_errors = std_order.price.values
months = ['April', 'May', 'June', 'July', 'August', 'September']
ax = plt.subplot()
plt.bar(range(len(bar_heights)), bar_heights, yerr=bar_errors, capsize=5)
ax.set_xticks(range(len(bar_heights)))
ax.set_xticklabels(months)
plt.ylabel('Average Price')
plt.title('Order Price over Time')
plt.show()

customer_amount = \
orders.groupby('customer_id').price.sum().reset_index()
print(customer_amount.head())

plt.hist(customer_amount.price.values, range=(0, 200), bins=40)
plt.xlabel('Total Spent')
plt.ylabel("Number of Customers")
plt.title('Customer Expenditure Over 6 Months')
plt.show()
