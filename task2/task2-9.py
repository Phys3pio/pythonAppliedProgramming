import numpy as np
import matplotlib as mpl
import matplotlib.pyplot as plt
x=np.arange(-10,10,0.02)
#y=np.array([])
#for x in range(-10,10):
y=(np.sin(2*x)**2) * np.exp(((x+2)/10)**2)
plt.plot(x,y)
plt.grid(lw=0.5, ls='--')
plt.plot(x,y, lw = 4.0, color='red')
plt.show()