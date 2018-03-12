from scipy.stats import ttest_1samp
import numpy as np

ages = np.array([32,34,29,29,22,39,38,37,38,36,30,26,22,22])
ages_mean = np.mean(ages)
print(ages_mean)

tstat, pval = ttest_1samp(ages, 30)
print(pval)
