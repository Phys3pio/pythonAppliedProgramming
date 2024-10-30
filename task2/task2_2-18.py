import numpy as np
import matplotlib.pyplot as plt
def mixed(z, *args):
    return np.sum(neg_gauss(z, *params) for params in args)
neg_gauss = lambda z, sigma, x0, y0: -mixed(z, sigma, x0, y0)
x = np.linspace(-20, 20, 100)
y = np.linspace(-20, 20, 100)
X, Y = np.meshgrid(x, y)

Z = mixed((X, Y), (10, -5, -12), (7, 5, 5), (9, -5, 10))
fig, ax = plt.subplots(1, 1, figsize=(8, 8))
contours = ax.contour(X, Y, Z, 16, colors="black", linewidths=2,
linestyles='-.')
ax.clabel(contours, inline=True, fontsize=16)
contours = ax.contourf(X, Y, Z, 200, cmap=plt.cm.jet)
plt.show()