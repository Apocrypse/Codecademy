# familiar is a data interface that a previous software engineer wrote for you
# import familiar

# vein_pack_lifespans = familiar.lifespans(package='vein')
vein_pack_lifespans = [76.93767431371617, 75.99335913014681, 74.79815012354048, 74.50202147158551, 77.48888897587436, 72.14256573154043, 75.99303167191182, 76.34155048095228, 77.48475562999882, 76.5321014800867, 76.25508955276418, 77.58398316566651, 77.04737034962294, 72.87475174594711, 77.43504547002844, 77.4923414107892, 78.32672046879952, 73.34370246887067, 79.96915765236346, 74.83800583300325]

from scipy.stats import ttest_1samp

vein_tstat, vein_pval = ttest_1samp(vein_pack_lifespans, 71)
if vein_pval < 0.05:
  print("The Vein Pack Is Proven To Make You Live Longer!")
else:
  print("The Vein Pack Is Probably Good For You Somehow!")

# artery_pack_lifespans = familiar.lifespans(package='artery')
artery_pack_lifespans = [76.33537008426835, 76.92308231559062, 75.9524416448778, 74.5449834807203, 76.4045042754472, 73.07924888636576, 77.02354461052992, 74.1174204200688, 77.38650656208344, 73.04476583718993, 74.96311850866167, 73.31954301933486, 75.85740137696862, 76.15265351351255, 73.3551028632267, 73.90221256458788, 73.77121195092475, 68.31489830285578, 74.63975717775328, 78.38547730843979]

from scipy.stats import ttest_ind

artery_tstat, artery_pval = ttest_ind(vein_pack_lifespans, artery_pack_lifespans)
if artery_pval < 0.05:
  print("The Artery Package guarantees even stronger results!")
else:
  print("The Artery Package is also a great product!")

# iron_contingency_table = familiar.iron_counts_for_package()
iron_contingency_table = [[140, 29], [40, 87], [20, 29]]

from scipy.stats import chi2_contingency

iron_chi2, iron_pval, iron_df, iron_expected = chi2_contingency(iron_contingency_table)
if iron_pval < 0.05:
  print("The Artery Package Is Proven To Make You Healthier!")
else:
  print("While We Can't Say The Artery Package Will Help You, I Bet It's Nice!")
