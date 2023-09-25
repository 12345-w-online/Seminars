import numpy as np


def kramer(n, m, s):
    if n != (m - 1):
        return 'No'

    det_o = np.linalg.det([k[:len(k) - 1] for k in s])
    if det_o == 0:
        return 'No'

    otv = np.zeros(n)
    for i in range(n):
        otv[i] = (np.linalg.det([j[i] + j[len(j) - 1] + j[i + 1:len(j) - 1] for j in s])) / det_o
    return otv


n, m = map(int, input().split())
s = np.zeros((n, m))
for i in range(n):
    s[i] = np.array(list(map(int, input().split())), int)

print(kramer(n, m, s))
int)))