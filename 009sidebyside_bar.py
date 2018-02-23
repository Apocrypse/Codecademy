from matplotlib import pyplot as plt

drinks = ["cappuccino", "latte", "chai", "americano", "mocha", "espresso"]
sales1 =  [91, 76, 56, 66, 52, 27]
sales2 = [65, 82, 36, 68, 38, 40]

def create_x(n, t, d, w):
    return [t*x + w*n for x in range(d)]

store1_x = create_x(1, 2, 6, 0.8)
plt.bar(store1_x, sales1)

store2_x = create_x(2, 2, 6, 0.8)
plt.bar(store2_x, sales2)

plt.show()
