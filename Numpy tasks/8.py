# Задача 72
import numpy as np

a = np.array([[1, 1, 1], [1, 1, 1], [1, 1, 2]])
a[[0, 2]] = a[[2, 0]]
print(a)
