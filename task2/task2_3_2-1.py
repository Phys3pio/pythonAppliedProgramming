import numpy as np
import matplotlib.pyplot as plt
import warnings
from scipy.optimize import minimize
warnings.filterwarnings('ignore')
dx=0.001
x=np.arange(-10,10,dx)
f0=lambda x:(x-0.5)**2
plt.plot(x,f0(x))
plt.show()
print(minimize(f0,x0=1))