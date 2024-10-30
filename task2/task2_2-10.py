from matplotlib import pyplot as plt
import numpy as np
def func(x,y):
    return np.sin(x**2+y**2)/(x**2+y**2)
x=np.linspace(-4,4,200)
y=np.linspace(-4,4,200)
X,Y=np.meshgrid(x,y)
Z=func(X,Y)
fig=plt.figure()
ax=plt.axes(projection='3d')
ax.plot_surface(X,Y,Z)
ax.view_init(30,60)
plt.show()