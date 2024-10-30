import numpy as np
a = 2
mas = []
for i in range(a):
    mas.append( [0] * a)
print(mas)
d = np.full((2,2), 7)  # Создаёт матрицу (1, 2), заполненую заданным значением [1](https://cs.mipt.ru/advanced_python/lessons/lab16.html)
print(d)