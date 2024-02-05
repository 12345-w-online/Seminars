import itertools

data_s = ['u', 'l']
a = 1
while a == 1:
#     print(*itertools.product('ABCD', repeat=2))
    s = int(input())
    if s == 0:
        break
    count = 0
    data = list(map(''.join, itertools.product(data_s, repeat=s)))
#     print(data)
    for i in data:
        if 'uuu' in i:
            count += 1
    print(count)
