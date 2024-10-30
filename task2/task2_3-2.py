from scipy.integrate import odeint
import numpy as np
from matplotlib import pyplot as plt
def func(y,t):
    u,f=y
    dydt=[2*u-f,u]
    return dydt
dt=1e-3
t=np.arange(0,1,dt)
res=odeint(func,y0=[1,1],t=t)
plt.plot(t,res[:,1])
plt.plot(t[::50],np.exp(t[::50]),'o')
plt.show()