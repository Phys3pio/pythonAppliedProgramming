import numpy as np
import matplotlib as mpl
import matplotlib.pyplot as plt
counts = [17, 3]
plt.figure(figsize=(5, 5))
plt.pie(counts, colors=['royalblue', 'gold'], labels=['Dogs', 'Cats'],startangle=120, autopct='%.3f%%')
plt.show()