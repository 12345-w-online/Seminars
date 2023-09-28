# Задача 61
import numpy as np

n = float(input())
a = np.asarray(np.random.rand(16, 16))
i = (np.abs(a - n)).argmin()
print(i)
