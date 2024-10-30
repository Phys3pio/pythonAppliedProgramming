import numpy as np
import matplotlib as mpl
import matplotlib.pyplot as plt
r=np.random.uniform(0,2,150)
theta=np.random.uniform(0,360,150)
plt.figure(figsize=(6, 6))
plt.axes(projection='polar')
plt.scatter(theta, r, s=400*r**2,c=theta,cmap='hsv',alpha=0.8)
plt.show()