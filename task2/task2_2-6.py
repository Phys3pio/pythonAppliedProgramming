import numpy as np
import matplotlib.pyplot as plt
x=np.linspace(-5,5,40)
y=np.sin(x)+np.tan(2*(x-2))
yerr=np.random.sample(y)
plt.figure(figsize=(10, 5))
plt.errorbar(x, y,yerr=yerr,ecolor='forestgreen',capsize=10,elinewidth=1.5)
plt.show()