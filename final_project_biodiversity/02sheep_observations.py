import pandas as pd
from matplotlib import pyplot as plt

species = pd.read_csv('species_info.csv')
species.fillna('No Intervention', inplace = True)
species['is_protected'] = species.conservation_status != 'No Intervention'

observations = pd.read_csv('observations.csv')
# print(observations.head())
# print(species.head())

find_sheep = lambda name: 'Sheep' in name
species['is_sheep'] = species.common_names.apply(find_sheep)
species_is_sheep = species[species.is_sheep == True]
# print(species_is_sheep)
# Many of the results are actually plants

sheep_species = species[(species.is_sheep == True) &
                          (species.category == 'Mammal')]
# print(sheep_species)

sheep_observations = pd.merge(sheep_species, observations)
# print(sheep_observations.head())

obs_by_park = sheep_observations.groupby('park_name').observations.sum().reset_index()
# print(obs_by_park)

# plt.figure(figsize=(16, 4))
# ax = plt.subplot()
# plt.bar(range(len(obs_by_park.observations)), obs_by_park.observations)
# ax.set_xticks(range(len(obs_by_park.park_name)))
# ax.set_xticklabels(obs_by_park.park_name)
# plt.ylabel('Number of Observations')
# plt.title('Observations of Sheep per Week')
# plt.show()
