import numpy as np
import matplotlib as mpl
import matplotlib.pyplot as plt
y=np.random.standard_cauchy(10**7)
plt.hist(y,range=(0, 5),bins=50,density=True)
plt.show()