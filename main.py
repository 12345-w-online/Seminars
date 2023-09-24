import numpy as np
a = np.arange(9)
gen = (x for x in a)
# print(np.fromiter(gen, int))
print(gen)
print(np.sum(np.fromiter(gen, int)))