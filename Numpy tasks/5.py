# Задача 47
import numpy as np
from random import randint
import itertools
i = randint(10, 100)
j = randint(10, 100)
x = np.reshape(np.repeat(np.array([1 / randint(1, 100) for k in range(i)]), j), (i, j))
y = np.transpose(np.reshape(np.repeat(np.array([-1 / randint(1, 100) for l in range(j)]), i), (j, i)))

print(x + y)
