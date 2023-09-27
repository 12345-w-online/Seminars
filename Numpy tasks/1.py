# задача 10
import numpy as np

a = np.array([1, 2, 0, 0, 4, 0])
print(*[i for i in range(len(a)) if a[i] > 0])