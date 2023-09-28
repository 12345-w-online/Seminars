# Задача 59
import numpy as np
import random

n = 5
a = np.random.rand(random.randint(10, 30), random.randint(10, 30))

print(a[a[:, n].argsort()])