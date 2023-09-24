import numpy as np

n, m = map(int,input().split())

s = np.zeros((n, m))
i, j = 0, 0
l = 1
print(s)
while l != n*m :
    while j+1 < m and s[i, j + 1] == 0:
        s[i, j] = l
        l += 1
        j += 1
    while i + 1 < n and s[i + 1, j] == 0:
        s[i, j] = l
        l += 1
        i +=1
    while j-1 > -1 and s[i, j - 1] == 0:
        s[i, j] = l
        l += 1
        j -= 1
    while i - 1 > -1 and s[i - 1, j] == 0:
        s[i, j] = l
        l += 1
        i -= 1
    print(s)
s[i, j] = l
print(s)
