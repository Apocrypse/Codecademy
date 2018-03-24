import pandas as pd
from matplotlib import pyplot as plt

species = pd.read_csv('species_info.csv')
# print(species.head())

# number of different species
species_count = species.scientific_name.nunique()
# print(species_count)

# different category
species_type = species.category.unique()
# print(species_type)

# different conservation status
conservation_statuses = species.conservation_status.unique()
# print(conservation_statuses)

# Analyze Species Conservation Status
conservation_counts = species.groupby('conservation_status').scientific_name.nunique().reset_index()
# print(conservation_counts)

species.fillna('No Intervention', inplace = True)
conservation_counts_fixed = species.groupby('conservation_status').scientific_name.nunique().reset_index()
# print(conservation_counts_fixed)

# Plotting Conservation Status by Species
species.fillna('No Intervention', inplace = True)
protection_counts = species.groupby('conservation_status') \
                    .scientific_name.nunique() \
                    .reset_index().sort_values(by='scientific_name')

# num_species = protection_counts.scientific_name
# status = protection_counts.conservation_status

# plt.figure(figsize=(10, 4))
# ax = plt.subplot()
# plt.bar(range(len(num_species)), num_species)
# ax.set_xticks(range(len(status)))
# ax.set_xticklabels(status)
# plt.xlabel('Conservation Status')
# plt.ylabel('Number of Species')
# plt.title('Conservation Status by Species')
# plt.show()

species['is_protected'] = species.conservation_status \
                          .apply(lambda status: True
                                 if status != 'No Intervention'
                                 else False)
category_counts = species.groupby(['category', 'is_protected']) \
                  .scientific_name.nunique().reset_index()
# print(category_counts)

category_pivot = category_counts.pivot(
                 columns = 'is_protected',
                 index = 'category',
                 values = 'scientific_name').reset_index()
category_pivot.columns = ['category', 'not_protected', 'protected']
# print(category_pivot)

category_pivot['percent_protected'] = category_pivot.protected / (category_pivot.protected + category_pivot.not_protected)
print(category_pivot)

from scipy.stats import chi2_contingency

contingency_bird_mammal = [[category_pivot.iat[3,2], category_pivot.iat[3,1]],
                           [category_pivot.iat[1,2], category_pivot.iat[1,1]]]


pval_bird_mammal = chi2_contingency(contingency_bird_mammal)[1]
print('{:.2f}%'.format(pval_bird_mammal*100))

contingency_reptile_mammal = [[category_pivot.iat[3,2], category_pivot.iat[3,1]],
                              [category_pivot.iat[5,2], category_pivot.iat[5,1]]]
pval_reptile_mammal = chi2_contingency(contingency_reptile_mammal)[1]
print('{:.2f}%'.format(pval_reptile_mammal*100))
