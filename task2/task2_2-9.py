from matplotlib import pyplot as plt
import numpy as np
def func(x,y):
    return 1/4*np.sin(1/2*x**2-y)-np.exp(-((x-5)**2+(y-2)**2))
x=np.linspace(2,8,200)
y=np.linspace(0,5,200)
X,Y=np.meshgrid(x,y)
Z=func(X,Y)
fig=plt.figure()
ax=plt.axes(projection='3d')
ax.plot_surface(X,Y,Z)
ax.view_init(30,60)
plt.show()