# Задача 24
import numpy as np

print(np.reshape(np.arange(15), (5, 3)) @ np.reshape(np.arange(15, 15+6), (3, 2)))
