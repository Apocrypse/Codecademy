import numpy as np

small_set = [10100, 35500, 105000, 85000, 25500, 40500, 65000]
large_set = np.genfromtxt('household_income.csv', delimiter=',')

small_set_median = sorted(small_set)[3]
large_set_median = np.median(large_set)

print(small_set_median)
print(large_set_median)
