from matplotlib import pyplot as plt

drinks = ["cappuccino", "latte", "chai", "americano", "mocha", "espresso"]
sales =  [91, 76, 56, 66, 52, 27]

ax = plt.subplot()
plt.bar(range(len(sales)), sales)
ax.set_xticks(range(len(drinks)))
ax.set_xticklabels(drinks)

plt.show()
