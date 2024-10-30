from scipy.integrate import odeint
import numpy as np
fl=float(input())
dt=0.001
t=np.arange(0,1,dt)
func=lambda f,t:f+t
res=odeint(func,y0=fl,t=t)
print(res)