import numpy as np
import matplotlib.pyplot as plt
from mpl_toolkits.mplot3d import Axes3D


def torus(R, r, n_theta=50, n_phi=50):
    theta = np.linspace(0, 2 * np.pi, n_theta)
    phi = np.linspace(0, 2 * np.pi, n_phi)
    theta, phi = np.meshgrid(theta, phi)

    x = (R + r * np.cos(phi)) * np.cos(theta)
    y = (R + r * np.sin(phi)) * np.sin(theta)
    z = r * np.sin(phi)

    return x, y, z


def plot_torus(ax, R, r, n_theta=50, n_phi=50):
    x, y, z = torus(R, r, n_theta=n_theta, n_phi=n_phi)
    ax.plot_surface(x, y, z, cmap="viridis", edgecolors=None)


fig = plt.figure(figsize=(12, 9))
ax = fig.add_subplot(111, projection='3d')

R = 3  
r = 1

plot_torus(ax, R, r)

plt.show()