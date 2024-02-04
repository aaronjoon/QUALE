import numpy as np
import matplotlib.pyplot as plt

data = np.load("data.npy")

plt.scatter(range(100), data[0:100, 0])
plt.show()