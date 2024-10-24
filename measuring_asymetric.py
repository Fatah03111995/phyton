import numpy as np
import matplotlib.pyplot as plt

symmetric = np.array([1,2,2,3,3,3,4,4,5])

plt.hist(symmetric, bins = 5)
plt.show()