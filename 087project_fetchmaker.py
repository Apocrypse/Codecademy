import numpy as np
import fetchmaker

rottweiler_tl = fetchmaker.get_tail_length("rottweiler")
mean_rottweiler_tl = np.mean(rottweiler_tl)
std_rottweiler_tl = np.std(rottweiler_tl)
print(mean_rottweiler_tl)
print(std_rottweiler_tl)

whippet_rescue = fetchmaker.get_is_rescue('whippet')
num_whippet_rescues = np.count_nonzero(whippet_rescue)
num_whippet = np.size(whippet_rescue)
print(num_whippet_rescues)
print(num_whippet)

from scipy.stats import binom_test
pval_bi = binom_test(num_whippet_rescues, n=num_whippet, p=0.08)
print(pval_bi)

whippets_weight = fetchmaker.get_weight('whippet')
terriers_weight = fetchmaker.get_weight('terrier')
pitbulls_weight = fetchmaker.get_weight('pitbull')
from scipy.stats import f_oneway
fstat, fpval = f_oneway(whippets_weight, terriers_weight, pitbulls_weight)
print('ANOVA: ' + str(fpval))
from statsmodels.stats.multicomp import pairwise_tukeyhsd
v = np.concatenate([whippets_weight, terriers_weight, pitbulls_weight])
labels = ['whippets_weight'] * len(whippets_weight) \
       + ['terriers_weight'] * len(terriers_weight) \
       + ['pitbulls_weight'] * len(pitbulls_weight)
tukey_results = pairwise_tukeyhsd(v, labels, 0.05)
print(tukey_results)

poodle_colors = fetchmaker.get_color("poodle")
shihtzu_colors = fetchmaker.get_color("shihtzu")
poodle_brown = np.count_nonzero(poodle_colors == "brown")
poodle_nonbrown = np.size(poodle_colors) - poodle_brown
shihtzu_brown = np.count_nonzero(shihtzu_colors == "brown")
shihtzu_nonbrown = np.size(shihtzu_colors) - shihtzu_brown
color_table = [[poodle_brown, poodle_nonbrown],
               [shihtzu_brown, shihtzu_nonbrown]]
from scipy.stats import chi2_contingency
chi2, chipval, df, expected = chi2_contingency(color_table)
print(chipval)
