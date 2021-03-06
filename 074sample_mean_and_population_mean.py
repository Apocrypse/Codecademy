import numpy as np

population = np.random.normal(loc=65, scale=3.5, size=300)
population_mean = np.mean(population)

print("Population Mean: {}".format(population_mean))

sample_1 = np.random.choice(population, size=30, replace=False)
sample_2 = np.random.choice(population, size=30, replace=False)
sample_3 = np.random.choice(population, size=30, replace=False)
sample_4 = np.random.choice(population, size=30, replace=False)
sample_5 = np.random.choice(population, size=30, replace=False)

sample_1_mean = np.mean(sample_1)
sample_2_mean = np.mean(sample_2)
sample_3_mean = np.mean(sample_3)
sample_4_mean = np.mean(sample_4)
sample_5_mean = np.mean(sample_5)

print("Sample 1 Mean: {}".format(sample_1_mean))
print("Sample 2 Mean: {}".format(sample_2_mean))
print("Sample 3 Mean: {}".format(sample_3_mean))
print("Sample 4 Mean: {}".format(sample_4_mean))
print("Sample 5 Mean: {}".format(sample_5_mean))
