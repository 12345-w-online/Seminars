# Задача
# 1

a, b = map(int, input().split())
print(a + b)
print(a - b)
print(a * b)

# Задача
# 2

a = int(input())
print(a // 10)

# Задача
# 3

a = list(map(int, input().split()))
s = 1
for elem in a:
    s *= elem
print(s ** (1 / len(a)))

# Задача
# 4

import operator

ops = {
    '+': operator.add,
    '-': operator.sub,
    '*': operator.mul,
    '/': operator.truediv,  # use operator.div for Python 2
    '%': operator.mod,
    '^': operator.xor,
}

f = open("text.txt", "r")
a, b = map(int, f.readline().split())
e = open('output.txt', 'w')
e.write(ops[f.readline()](a, b))
e.close()
f.close()

# Задача
# 5

N, b, c = map(int, input().split())
N = int(str(N), b)
s = ''
while N > 0:
    s += str(N % c)
    N //= c
print(s[::-1])

# Задача
# 6
##
import operator

ops = {
    '+': operator.add,
    '-': operator.sub,
    '*': operator.mul,
    '/': operator.truediv,  # use operator.div for Python 2
    '%': operator.mod,
    '^': operator.xor,
}
f = open("text.txt", "r")
a, b = map(int, f.readline().split())
sign = f.readline()
base = int(f.readline())
f.close
operation = ops[sign.strip()](int(str(a), base), int(str(b), base))
s = ''
while operation > 0:
    s += str(operation % base)
    operation //= base
e = open('output.txt', 'w')
e.write(s[::-1])
e.close()
