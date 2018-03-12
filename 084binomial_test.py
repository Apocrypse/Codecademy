from scipy.stats import binom_test

pval = binom_test(510, n=10000, p=0.06)
print(pval)

pval2 = binom_test(590, n=10000, p=0.06)
print(pval2)
