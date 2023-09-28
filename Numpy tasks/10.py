# Задача 96
import numpy as np

a = np.array([[1, 1, 1], [1, 1, 1], [1, 1, 2]])
# a = np.random.rand(16, 16)
# [i if np.count_nonzero(a == i) == 2 else None for i in a]
a_new = np.unique(a, axis=0, return_counts=True)
print(*(a_new[0][i] if a_new[1][i] == 1 else '' for i in range(len(a_new[1]))))
