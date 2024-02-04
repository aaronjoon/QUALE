import numpy as np
import matplotlib.pyplot as plt

data = np.load("data.npy")
data2 = np.load("data2.npy")
data3 = np.load("data3.npy")
data4 = np.load("data4.npy")
data5 = np.load("data5.npy")


# plt.scatter(range(100), data[0:300, 0])
# plt.show()

# plt.scatter(range(np.shape(data2)[0]), data2[:, 0])
# plt.show()

plt.plot(range(np.shape(data5)[0]), data5[:, 1], label="Tr[M*P]")
plt.plot(range(np.shape(data5)[0]), data5[:, 2], label="Tr[M*tau]")

plt.xlabel("iteration")
plt.show()

# # deg=1 means linear fit (i.e. polynomial of degree 1)
# b, a = np.polyfit(range(np.shape(data4)[0]), data4[:, 0], deg=1)
# print(b, a)

# # Plot regression line
# plt.plot(range(np.shape(data4)[0]), a + b * range(np.shape(data4)[0]), color="k", lw=2.5)

# plt.show()
