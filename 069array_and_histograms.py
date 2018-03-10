import numpy as np
from matplotlib import pyplot as plt

commutes = np.genfromtxt('commutes.csv', delimiter=',')

plt.hist(commutes, bins=6 ,range=(20,50))
plt.show()
