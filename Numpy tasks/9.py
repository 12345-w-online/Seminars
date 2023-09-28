# Задача 87
import numpy as np
import random

a = np.random.rand(16, 16)
print(np.array([[np.sum(a[i: i+4, j: j+4]) for i in range(12)] for j in range(12)]))
