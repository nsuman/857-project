import numpy as np
import matplotlib
matplotlib.use('TkAgg')
import matplotlib.pyplot as plt
import matplotlib.colors as mcolors
from numpy.random import multivariate_normal
from sklearn.preprocessing import normalize

# np.random.seed(19680801)
# data = np.random.randn(2, 100)

# fig, axs = plt.subplots(2, 2, figsize=(5, 5))
# axs[0, 0].hist(data[0])
# axs[1, 0].scatter(data[0], data[1])
# axs[0, 1].plot(data[0], data[1])
# axs[1, 1].hist2d(data[0], data[1])

# plt.show()

# data = np.vstack([
#     multivariate_normal([10, 10], [[3, 2], [2, 3]], size=100000),
#     multivariate_normal([30, 20], [[2, 3], [1, 3]], size=1000)
# ])
# print(data)
# gammas = [0.8, 0.5, 0.3]

# fig, axes = plt.subplots(nrows=2, ncols=2)

# axes[0, 0].set_title('Linear normalization')
# axes[0, 0].hist2d(data[:, 0], data[:, 1], bins=100)

# for ax, gamma in zip(axes.flat[1:], gammas):
#     ax.set_title(r'Power law $(\gamma=%1.1f)$' % gamma)
#     ax.hist2d(data[:, 0], data[:, 1],
#               bins=100, norm=mcolors.PowerNorm(gamma))

# fig.tight_layout()

# plt.show()

a = np.array([1, 2, 3])
b = np.array([2, 3, 4])
x=np.vstack((a,b))
print(x)
print(x[0,]
)
# x = np.random.rand(1000)*10
# print()
# norm1 = x / np.linalg.norm(x)
# norm2 = normalize(x[:,np.newaxis], axis=0).ravel()
# print np.all(norm1 == norm2)