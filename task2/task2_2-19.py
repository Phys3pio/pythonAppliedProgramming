from scipy.optimize import minimize
import numpy as np

def f(x):
    return x**2 * (x - 4)**2 * np.exp(-x**2)

x0 = float(input())  # Начальное предположение
dx = 0.001
x = np.arange(-4,4,dx)

result = minimize(f, x0, method='BFGS')

print(result)