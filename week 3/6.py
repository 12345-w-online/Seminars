import numpy as np

s1 = input().split()
s = np.array([[int(s1[i]), int(s1[i + 1])]for i in range(0, len(s1), 2)])
print(s)
sum_x = np.sum([i[0] for i in s])
sum_y = np.sum([i[1] for i in s])
sum_xy = np.sum([i[0] * i[1] for i in s])
sum_xx = np.sum([i[0] * i[0] for i in s])

a = ((len(s) * sum_xy) - (sum_x * sum_y)) / ((len(s) * sum_xx) - sum_x ** 2)

b = (sum_y - (a * sum_x)) / len(s)

print(a, b)
