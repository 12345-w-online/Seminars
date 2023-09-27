# Задача 19
import numpy as np

print(np.reshape(([i % 2 if i // 8 % 2 == 0 else (i + 1) % 2 for i in np.arange(64)]), (8, 8)))
